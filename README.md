

# **Space Station Safety Object Detector – DualityAI Hackathon Project**

**Team Members:**

* **Viren Pandey** (Team Lead)
* **Priyanshu Aryan**
* **Pratyush Ghosh**

---

## **📌 Overview**

This project was developed for the **DualityAI Space Station Safety Challenge** under the **BuildWithIndia 2.0 Hackathon**.
The goal is to detect **7 critical space-station safety objects** using a **custom-trained YOLOv8 model** powered by **Falcon’s synthetic dataset**.

### **Detected Classes**

1. OxygenTank
2. NitrogenTank
3. FirstAidBox
4. FireAlarm
5. SafetySwitchPanel
6. EmergencyPhone
7. FireExtinguisher

The project includes:

* A custom-trained YOLO model (`best.pt`)
* Full training and validation logs
* A working **Streamlit App** for real-time object detection
* Falcon-based model updating plan
* Complete report and documentation
* Prediction samples

---

## **📁 Project Structure**

```
Final_Submission/
│
├── models/
│   └── best.pt
│
├── runs/
│   └── train5/                # Complete YOLO training logs
│
├── predictions/
│   ├── images/                # Output images with bounding boxes
│   └── labels/                # YOLO-format prediction labels
│
├── code/
│   ├── train.py               # Training script
│   ├── predict.py             # Batch prediction script
│   ├── app.py                 # Streamlit App (bonus)
│   ├── yolo_params.yaml       # Dataset configuration
│   └── ENV_SETUP/             # Conda environment setup tools
│
├── docs/
│   ├── Report.pdf             # Final hackathon report
│   └── README.md              # This file
│
└── requirements.txt
```

---

## **⚙️ Installation & Setup**

### **1. Create the Conda Environment**

Navigate to:

```
code/ENV_SETUP/
```

Run:

```
setup_env.bat
conda activate EDU
```

This installs:

* PyTorch (GPU-enabled)
* Ultralytics YOLO
* OpenCV
* Streamlit
* PyYAML
* NumPy

---

## **🚀 Training the Model**

To retrain the YOLO model:

```
cd code
python train.py
```

Training parameters inside `train.py`:

* Epochs: 10
* Batch Size: 16
* Image Size: 640
* Optimizer: AdamW
* Pretrained Weights: yolov8s.pt

Training logs are saved automatically in:

```
runs/detect/trainX/
```

---

## **🧪 Running Predictions**

### **Batch Prediction**

```
python predict.py
```

Results will be saved to:

```
predictions/images/
predictions/labels/
```

---

## **🌐 Streamlit App (Bonus Component)**

To launch the app:

```
streamlit run app.py
```

### App Features:

* Upload an image
* Run YOLO inference (real-time)
* Download annotated output
* Clear UI for judges
* Included Falcon updating explanation

---

## **📊 Model Performance**

### **Final Validation Metrics:**

| Metric    | Score     |
| --------- | --------- |
| Precision | **0.866** |
| Recall    | **0.684** |
| mAP@50    | **0.773** |
| mAP@50–95 | **0.645** |

### **Class-wise mAP@50**

* OxygenTank — 0.871
* NitrogenTank — 0.815
* FirstAidBox — 0.832
* FireAlarm — 0.839
* SafetySwitchPanel — 0.685
* EmergencyPhone — 0.653
* FireExtinguisher — 0.718

---

## **🔄 Falcon Model Updating Plan**

Falcon can generate updated synthetic datasets when:

* New objects are added
* Lighting conditions change
* Camera angles vary
* Equipment models are modified

**Updating Workflow:**

1. Generate new synthetic dataset from Falcon
2. Update paths in `yolo_params.yaml`
3. Retrain using `python train.py`
4. Replace `best.pt` in `app.py` directory
5. The Streamlit app instantly uses the updated model

This ensures **continuous improvement** without needing real ISS imagery.

---

## **📦 Submission Includes**

* Trained YOLOv8 model
* All scripts (train, predict, app)
* Dataset configuration
* Full training logs
* Streamlit interface
* Prediction results
* Final report
* README
* Falcon updating plan

---

## **🏁 Conclusion**

The project demonstrates how **synthetic digital-twin data** from Falcon can be combined with **YOLOv8** to build a reliable, scalable safety-monitoring system for space-station environments. The integration of a real-time detection app further highlights the practical value of the solution.

