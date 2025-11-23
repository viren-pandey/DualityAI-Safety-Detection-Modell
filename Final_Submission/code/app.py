import streamlit as st
from ultralytics import YOLO
from PIL import Image
import numpy as np
import cv2
import os

# Load Model
model_path = "runs/detect/train5/weights/best.pt"
model = YOLO(model_path)

st.title("Space Station Safety Object Detector 🚀")
st.write("Upload an image to detect safety equipment on the space station.")

uploaded_file = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    # Display uploaded image
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image", use_column_width=True)

    # Run YOLO inference
    results = model.predict(image, conf=0.5)
    result = results[0]
    output = result.plot()

    st.subheader("Detection Output")
    st.image(output, caption="Detected Objects", use_column_width=True)

    # Download option
    output_path = "output_detected.jpg"
    cv2.imwrite(output_path, output)

    with open(output_path, "rb") as f:
        st.download_button("Download Result", f, file_name="detected.jpg")

# Falcon Updating Explanation
st.header("🔄 How Falcon Can Keep This Model Updated")
st.write("""
Falcon generates synthetic space-station environments with updated lighting, angles, 
occlusions, and new safety equipment.  
Whenever conditions or equipment change:

1. Falcon generates new synthetic training data.
2. We retrain the YOLO model using the same pipeline.
3. We update `best.pt` in the app — instantly upgrading detection accuracy.

This keeps the detection model always aligned with real-space station conditions.
""")
