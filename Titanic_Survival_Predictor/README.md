# 🚀 Titanic Survival Predictor

## 🌊 Introduction
The **Titanic Survival Predictor** is a web-based application that utilizes machine learning to determine the likelihood of a passenger surviving the Titanic disaster. Built with **Python, Streamlit, and scikit-learn**, this project is fully containerized using **Docker**, making deployment and scalability seamless.

## 📦 Project Structure
```
/titanic_survival_app
│── Dockerfile
│── requirements.txt
│── main.py
│── train_model.py
│── model.pkl
```
### 🗂 File Breakdown
- **`main.py`** – Runs the Streamlit web application.
- **`train_model.py`** – Script for data preprocessing, model training, and exporting.
- **`model.pkl`** – The saved machine learning model for making predictions.
- **`requirements.txt`** – Specifies all dependencies required for execution.
- **`Dockerfile`** – Defines how the app is containerized.

## 🏗 Model Training
The survival predictor is based on a **Random Forest Classifier**, trained on historical Titanic passenger data. The training process involves:
1. **Data Cleaning** – Handling missing values and encoding categorical variables.
2. **Feature Engineering** – Selecting relevant features like age, fare, class, and family relations.
3. **Model Training** – Using a **Random Forest algorithm** for classification.
4. **Saving the Model** – Storing the trained model as `model.pkl` using `joblib`.

## 🎨 User Interface
The **Streamlit app** provides an intuitive form where users can enter passenger details to get an instant prediction on survival chances. 

### 🔹 Features:
✅ **Interactive Input Fields** – Choose passenger class, gender, age, and other details.  
✅ **Instant Prediction** – Get real-time results using the trained model.  
✅ **User-Friendly Design** – Simple layout for easy navigation.  

## 🛠 Deployment with Docker
To ensure ease of deployment across different systems, the application is containerized.

### 📜 Dockerfile
```Dockerfile
# Use Python slim image as base
FROM python:3.12-slim

# Set working directory
WORKDIR /app

# Copy required files
COPY requirements.txt .
COPY main.py .
COPY model.pkl .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose Streamlit port
EXPOSE 8501

# Run the Streamlit app
CMD ["streamlit", "run", "main.py", "--server.port=8501", "--server.address=0.0.0.0"]
```

## 🚀 How to Run
### 1️⃣ Clone the Repository
```sh
git clone https://github.com/your-username/titanic-survival-app.git
cd titanic-survival-app
```
### 2️⃣ Build the Docker Image
```sh
docker build -t titanic-app .
```
### 3️⃣ Run the Container
```sh
docker run -p 8501:8501 titanic-app
```
### 4️⃣ Access the Application
Open your browser and go to:
```
http://localhost:8501
```

## 🚢 Future Enhancements
🔹 Deploy to a cloud service like **AWS, Google Cloud, or Heroku**.  
🔹 Improve the model with **deep learning techniques**.  
🔹 Add **visualizations** for better insights.  

🌟 **Enjoy Predicting & Happy Coding!** 🐳


