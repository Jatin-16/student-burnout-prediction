# Student Stress & Burnout Prediction Web App

This project is a machine learning web application that predicts the risk of student academic burnout using behavioural and academic indicators.

The application uses a trained machine learning model and provides a simple web interface where users can input student information to assess burnout risk.

---

## Features

• Machine learning model trained on student performance dataset  
• Interactive web interface for entering student details  
• Burnout risk prediction based on behavioural indicators  
• Flask backend serving the prediction model  

---

## Tech Stack

Python  
Flask  
Scikit-learn  
NumPy  
Pandas  
HTML  
Bootstrap  

---

## Project Structure


student-burnout-prediction
│
├── app.py
├── train.ipynb
├── student-mat.csv
│
├── burnout_model.pkl
├── scaler.pkl
├── features.pkl
│
└── templates
├── index.html
├── form.html
└── result.html


---

## How to Run the Project

### 1. Clone the repository

git clone https://github.com/your-username/student-burnout-prediction.git

### 2. Install dependencies

pip install flask numpy scikit-learn pandas

### 3. Run the application

python app.py

### 4. Open in browser

http://127.0.0.1:5000

---

## Dataset

Student Performance Dataset used for training the machine learning model.

---

## Disclaimer

This tool provides an early indicator of potential academic burnout risk a
