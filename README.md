# Bakground_Removal
Project : remove background from image

# 🧼 Background Removal Web App using U²-Net (Flask + PyTorch)

This is a simple web application built with Flask that allows users to upload an image and get the background removed using a lightweight U²-Net (`u2netp`) deep learning model.
# Steps to use the repository

---
## Step 1: 📥 Download U-2-Net Folder

To download the `U-2-Net` folder (without model weights):

```bash
git clone https://github.com/xuebinqin/U-2-Net.git
```
## Step 2: Download Pretrained Model (u2netp.pth): 
After downloading 'u2netp.pth' move it in side 'U-2-Net folder'. 

## 🚀 Features

- Upload any image through a web interface
- Processes image with U²-Net model (lightweight `u2netp`)
- Outputs transparent PNG with background removed
- Clean and colorful UI with light blue and violet tones

---

## 📂 My Project Structure
           background-removal/ 
                    ├── app.py 
                    ├── background_removal.ipynb 
                    ├── static/ │ ├── uploads/ 
                                │ └── results/ 
                    ├── templates/ │ ├── home.html │ └── result.html 
                    ├── U-2_Net/ │ ├── model/ │ 
                                          │ └── u2net.py
                                 │ └── u2netp.pth 
                    ├─requirements.txt


## 🧠 Model Info

We use the **U²-Net** architecture from the paper:  
> [U²-Net: Going Deeper with Nested U-Structure for Salient Object Detection](https://arxiv.org/abs/2005.09007)

This project uses the smaller version: `u2netp.pth` (~4.7MB) which is fast and lightweight for background removal.

---
