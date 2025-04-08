from flask import Flask, render_template, request, redirect, url_for,send_file
import os
import torch
import numpy as np
from PIL import Image
from torchvision import transforms
from torch.autograd import Variable
import sys
sys.path.append('c:/Users/rajki/OneDrive/Desktop/Background removal/U-2-Net')
from model.u2net import U2NETP 
import warnings
warnings.filterwarnings("ignore", category=UserWarning)


# app setup
app=Flask(__name__)
upload_folder='static/uploads'
result_folder='static/results'
os.makedirs(upload_folder, exist_ok=True)
os.makedirs(result_folder,exist_ok=True)

# uploading the model
model=U2NETP(3,1)
model.load_state_dict(torch.load(r'C:\Users\rajki\OneDrive\Desktop\Background removal\U-2-Net\u2netp.pth',map_location='cpu'))
model.eval()

#preprocessing
def preprocess(image_path):
    image=Image.open(image_path).convert("RGB").resize((480,480))
    transform=transforms.Compose([
        transforms.ToTensor(),
        transforms.Normalize([0.485, 0.456, 0.406],
                             [0.229, 0.224, 0.225])
    ])
    image_tensor=transform(image).unsqueeze(0)
    return image,image_tensor

# post processing
def apply_mask(org_image,pred_mask,save_path):
    pred_mask=pred_mask.squeeze().cpu().data.numpy()
    pred_mask=(pred_mask-pred_mask.min()) / (pred_mask.max()-pred_mask.min())
    pred_mask=np.array(pred_mask*255).astype(np.uint8)
    pred_mask=Image.fromarray(pred_mask).resize(org_image.size)
    # Mask apply
    org_np=np.array(org_image)
    mask_np=np.array(pred_mask) / 255.0
    mask_np=np.expand_dims(mask_np,axis=2)

    result=org_np*mask_np+255*(1-mask_np)
    result=result.astype(np.uint8)
    Image.fromarray(result).save(save_path)

@app.route('/')
def home():
    return render_template("home.html")

@app.route('/upload',methods=['POST'])
def upload():
    if 'image' not in request.files:
        return redirect('/')
    file = request.files['image']
    if file.filename == '':
        return redirect('/')
    
    input_path = os.path.join(upload_folder, file.filename)
    file.save(input_path)

    # Background removal
    orig_img, tensor_img = preprocess(input_path)
    with torch.no_grad():
        d1, *_ = model(tensor_img)
    output_path = os.path.join(result_folder, f"result_{file.filename}")
    apply_mask(orig_img, d1, output_path)

    return render_template('result.html', image_url=url_for('static', filename=f'results/result_{file.filename}'))

@app.route("/download")
def download():
    filename=os.listdir(result_folder)[-1]
    return send_file(os.path.join(result_folder, filename),as_attachment=True)

if __name__ == "__main__":
    app.run(debug=True)