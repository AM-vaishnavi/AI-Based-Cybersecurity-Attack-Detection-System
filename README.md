# 🛡️ AI-Based Cybersecurity Attack Detection System
## Network Intrusion Detection System (NIDS)

An AI-powered Network Intrusion Detection System (NIDS) developed using Machine Learning and Streamlit. The system detects different types of cyber attacks by analyzing network traffic from the CIC-IDS2017 dataset.

---

# 📌 Features

- AI-Based Intrusion Detection
- Random Forest Machine Learning Model
- CIC-IDS2017 Dataset
- Automatic Parquet to CSV Conversion
- Model Training
- Save Trained Model (.pkl)
- Upload Test CSV for Prediction
- Prediction Summary
- Prediction Distribution Chart
- Classification Report
- Confusion Matrix
- Download Prediction Results
- Interactive Streamlit Dashboard

---

# 📂 Project Structure

```
AI-Based-NIDS/
│
├── app.py
├── train_model.py
├── predict.py
├── convert_dataset.py
├── utils.py
├── style.css
├── requirements.txt
├── README.md
│
├── datasets/
│     ├── Benign-Monday-no-metadata.parquet
│     ├── Bot-Friday-no-metadata.parquet
│     ├── DDoS-Friday-no-metadata.parquet
│     ├── DoS-Wednesday-no-metadata.parquet
│     ├── PortScan-Friday-no-metadata.parquet
│     ├── WebAttacks-Thursday-no-metadata.parquet
│     └── ...
│
├── csv_datasets/
│     ├── Benign-Monday.csv
│     ├── Bot-Friday.csv
│     ├── DDoS-Friday.csv
│     └── ...
│
├── merged_dataset/
│     └── merged_dataset.csv
│
└── model/
      ├── model.pkl
      ├── features.pkl
      └── accuracy.pkl
```

---

# 📊 Dataset

Dataset Used:

**CIC-IDS2017**

The dataset contains both normal and malicious network traffic collected from real-world enterprise network environments.

Attack Classes include:

- Benign
- Bot
- DDoS
- DoS Hulk
- DoS GoldenEye
- DoS Slowloris
- DoS SlowHTTPTest
- FTP-Patator
- SSH-Patator
- PortScan
- Infiltration
- Heartbleed
- Web Attack – Brute Force
- Web Attack – SQL Injection
- Web Attack – XSS

---

# ⚙️ Installation

Clone the repository

```bash
git clone <repository-url>
```

Go to project folder

```bash
cd AI-Based-NIDS
```

Create Virtual Environment

```bash
python -m venv venv
```

Activate Virtual Environment

### Windows

```bash
venv\Scripts\activate
```

### Linux / Mac

```bash
source venv/bin/activate
```

Install required libraries

```bash
pip install -r requirements.txt
```

---

# 🚀 Convert Dataset

Convert all Parquet files into CSV files.

```bash
python convert_dataset.py
```

Converted CSV files will be stored inside

```
csv_datasets/
```

---

# 🧠 Train Machine Learning Model

Train the Random Forest model.

```bash
python train_model.py
```

After training, the following files will be created.

```
model/
│
├── model.pkl
├── features.pkl
└── accuracy.pkl
```

---

# ▶️ Run Streamlit Application

```bash
streamlit run app.py
```

The application opens automatically in your browser.

```
http://localhost:8501
```

---

# 📈 Prediction

1. Open Streamlit App

2. Click **Predict Attack**

3. Upload Test CSV

4. Click **Predict**

The application will display

- Predicted Attack Type
- Prediction Summary
- Attack Distribution Chart
- Accuracy (if Label column exists)
- Classification Report
- Confusion Matrix

You can also download the prediction results as CSV.

---

# 🤖 Machine Learning Algorithm

Random Forest Classifier

Reasons for selecting Random Forest

- High Accuracy
- Fast Prediction
- Handles Large Datasets
- Less Overfitting
- Feature Importance

---

# 🛠️ Technologies Used

- Python
- Streamlit
- Pandas
- NumPy
- Scikit-Learn
- Joblib
- Matplotlib
- Seaborn

---

# 📌 Project Workflow

```
CIC-IDS2017 Dataset
        │
        ▼
Parquet Files
        │
        ▼
Convert to CSV
        │
        ▼
Merge CSV Files
        │
        ▼
Data Cleaning
        │
        ▼
Feature Selection
        │
        ▼
Train Random Forest
        │
        ▼
Save Model (.pkl)
        │
        ▼
Run Streamlit App
        │
        ▼
Upload Test Dataset
        │
        ▼
Predict Attack
        │
        ▼
Display Results
```

---

# 👥 End Users

- Network Administrators
- Cybersecurity Analysts
- Organizations
- Researchers
- Students

---

# 📄 License

This project is developed for educational and academic purposes.

---

# 👩‍💻 Author

**Vaishnavi A M**

**B.Tech – Computer Science and Engineering**

AI-Based Cybersecurity Attack Detection System (Network Intrusion Detection System - NIDS)