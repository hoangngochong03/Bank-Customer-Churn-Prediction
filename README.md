# 📌  Bank Customer Churn Prediction

## 🚀 Introduction
This project aims to build a model to predict customer churn in a bank. The model is trained on the dataset located in the `data` directory and integrated into a **Streamlit** application for easy interaction.

---
📊 Dataset

 The dataset used for this project can be found on Kaggle: [Bank Customer Churn Modeling](https://www.kaggle.com/datasets/barelydedicated/bank-customer-churn-modeling)

## 🔧 Installation and Running the Application

### 1️⃣ System Requirements
- **Python 3.12**
- Libraries listed in `requirements.txt`

### 2️⃣ Install Dependencies
Run the following command to install the required libraries:
```sh
pip install -r requirements.txt
```

### 3️⃣ Train the Model
Open **`model.ipynb`** and run all the notebook cells to:
- Preprocess the data
- Train the model
- Save the model for the Streamlit application

### 4️⃣ Run the Streamlit Application
After training the model, launch the application with:
```sh
streamlit run App/app.py
```
The application will open a web interface to predict **customer churn** based on input data.

---

## 📂 Project Structure
```
DS102-Bank-Customer-Churn-Prediction/
│── App/
│   ├── app.py  # Streamlit application source code
│── data/       # Training data
│── model.ipynb # Model training notebook
│── requirements.txt # Required dependencies
│── README.md   # Project documentation
```

---


