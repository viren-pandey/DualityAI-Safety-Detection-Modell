

# **DualityAI Space Station Safety Object Detection – Hackathon Submission**

This repository contains my official submission for the
**DualityAI Space Station Safety Challenge** (BuildWithIndia 2.0).

The full submission (model, code, logs, report, app, predictions) is inside:

👉 **`Final_Submission/` folder**

---

# ## 📁 Folder Structure

```
Final_Submission/
│
├── models/                 → best.pt (trained YOLO model)
├── runs/                   → training logs & graphs
├── predictions/            → output images + YOLO labels
├── code/                   → train.py, predict.py, app.py
├── docs/                   → Report.pdf + detailed README
└── requirements.txt
```

---

# ## 🚀 Installation & Running Instructions

You can run the project using **pip** or the included **Conda environment**.

---

# ### **1. Clone the Repository**

```
git clone https://github.com/viren-pandey/DualityAI-Safety-Detection-Model.git
cd DualityAI-Safety-Detection-Model/Final_Submission
```

---

# ### **2. Install Dependencies (pip)**

Run:

```
pip install -r requirements.txt
```

This installs:

* YOLO (Ultralytics)
* PyTorch
* OpenCV
* Streamlit
* NumPy
* PyYAML

---

# ### **3. Optional: Create Conda Environment**

Navigate to:

```
Final_Submission/code/ENV_SETUP
```

Run:

```
setup_env.bat
conda activate EDU
```

This reproduces the exact environment used for training and testing.

---

# ### **4. Train the Model (Optional)**

If you want to retrain YOLO:

```
cd code
python train.py
```

This will create a new `runs/detect/trainX` folder with updated logs.

---

# ### **5. Run Batch Predictions**

```
python predict.py
```

The results will be saved to:

```
predictions/images/
predictions/labels/
```

---

# ### **6. Launch the Streamlit App (Bonus Component)**

The web app allows uploading images and seeing detection results instantly.

```
streamlit run app.py
```

This opens a browser window at:

```
http://localhost:8501
```

Features:

* Upload any image
* YOLO runs inference in real-time
* Download processed images
* Clear UI for judges
* Falcon model updating explanation included

---

# ## 🎯 Features

* Custom-trained YOLOv8 model on Falcon synthetic dataset
* High accuracy across 7 safety-critical classes
* Real-time detection via Streamlit
* Falcon-based model updating pipeline
* Complete documentation + predictions + logs

---

# ## 👨‍🚀 Classes Detected

* OxygenTank
* NitrogenTank
* FirstAidBox
* FireAlarm
* SafetySwitchPanel
* EmergencyPhone
* FireExtinguisher

---

# ## 🏁 Final Note

A complete detailed report is inside:
👉 **`Final_Submission/docs/Report.pdf`**


