# Bakground_Removal
Project : remove background from image

# 🧼 Background Removal Web App using U²-Net (Flask + PyTorch)

This is a simple web application built with Flask that allows users to upload an image and get the background removed using a lightweight U²-Net (`u2netp`) deep learning model.
# Steps to use the repository
Remember to have the folder structure given below without the folder structure 'app.py' will not run properly.

---
## Step 1: 📥 Download U-2-Net Folder

To download the `U-2-Net` folder (without model weights):

```bash
git clone https://github.com/xuebinqin/U-2-Net.git
```
## Step 2: Download Pretrained Model (u2netp.pth): Download from here 👉 https://drive.google.com/file/d/1rbSTGKAE-MTxBYHd-51l2hMOQPT_7EPy/view?usp=sharing

After downloading 'u2netp.pth' move it in side 'U-2-Net folder'. 

## Step 3: 
``` 
pip install -r requirements.txt
```
then 
```
python app.py
```
## 🚀 Features

- Upload any image through a web interface
- Processes image with U²-Net model (lightweight `u2netp`)
- Outputs transparent PNG with background removed
- Clean and colorful UI with light blue and violet tones

---

## 📂 My Project Structure
```
background removal/
├── app.py                  # Flask backend
├── static/
│   ├── uploads/            # Original images
│   └── results/            # Background-removed outputs
├── templates/              # HTML pages
│   ├── home.html           # Upload interface
│   └── result.html         # Results viewer
└── U-2-Net/                # Model code
    ├── model/
    │   ├── u2net.py        # Architecture
    └── u2netp.pth          # Pretrained weights
```
Note: static folder is not necessary as it will be created when app.py will run. 

## 🧠 Model Info

We use the **U²-Net** architecture from the paper:  
> [U²-Net: Going Deeper with Nested U-Structure for Salient Object Detection](https://arxiv.org/abs/2005.09007)

This project uses the smaller version: `u2netp.pth` (~4.7MB) which is fast and lightweight for background removal.
It won't not work well with scenery image where the definition of object is very broad , works well with objects and people image. 
---
