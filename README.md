# 🏡 Airbnb Dynamic Pricing Prediction System

## 📌 Project Overview
This project builds a machine learning model to predict Airbnb listing prices based on property features such as location, availability, and demand. The goal is to simulate a dynamic pricing system that helps hosts set optimal prices.

---

## 🎯 Objectives
- Analyze Airbnb listing data
- Perform feature engineering to capture demand patterns
- Train and compare multiple regression models
- Optimize model using hyperparameter tuning
- Deploy the model using Streamlit for real-time predictions

---

## 📊 Dataset
- Source: Inside Airbnb
- Contains listing details like price, location, availability, and reviews

---

## ⚙️ Tech Stack
- Python
- Pandas, NumPy
- Scikit-learn
- Matplotlib, Seaborn
- Streamlit
- Joblib

---

## 🔍 Exploratory Data Analysis (EDA)
- Price distribution analysis
- Room type vs price comparison
- Correlation heatmap for numerical features
- Availability vs price comparison
- Review vs price comparison

---

## 🧹 Data Cleaning
- Removed irrelevant columns
- Handled missing values
- Removed outliers in price

---

## ⚡ Feature Engineering
- One-hot encoding for categorical variables
- Created new features:
  - `availability_ratio`
  - `demand_score`
- Reduced high-cardinality features (top neighbourhoods)

---

## 🤖 Models Used
- Linear Regression
- Decision Tree Regressor
- Random Forest Regressor
- Gradient Boosting Regressor

---

## 📈 Model Evaluation
- Metric used: RMSE (Root Mean Squared Error)
- Compared all models using a bar plot
- Selected best model based on lowest RMSE

---

## 🏆 Final Model
Linear Regression (Best Performing Model)
---

## 📊 Feature Importance
- Identified most influential features affecting price

---

## 💾 Model Saving
```python
joblib.dump(model, "model.pkl")
joblib.dump(columns, "columns.pkl")

🚀 Deployment using Streamlit

The trained model is deployed using Streamlit to create an interactive web application.

🔹 Features:

User inputs property details

Model predicts price instantly

Simple and interactive UI

🔹 Run the app:
streamlit run app.py
🎯 Outcome

The deployed application allows users to predict Airbnb prices in real-time. This project demonstrates an end-to-end machine learning workflow including data preprocessing, model building, evaluation, tuning, and deployment.

##📁 Project Structure    

project/
│
├── notebook.ipynb        # ML pipeline (EDA → Model)
├── app.py                # Streamlit app
├── model.pkl             # Saved model
├── columns.pkl           # Feature columns
├── listings.csv          # Dataset
└── README.md             # Project documentation

## 🚀 Future Improvements
- Add more features like seasonality and location clustering
- Improve UI with dropdowns for categorical variables
- Deploy on cloud platforms (Streamlit Cloud / AWS)
- Use advanced models like XGBoost
- Add real-time data integration

## 🚀 Future Improvements
- Add more features like seasonality and location clustering
- Improve UI with dropdowns for categorical variables
- Deploy on cloud platforms (Streamlit Cloud / AWS)
- Use advanced models like XGBoost
- Add real-time data integration

👩‍💻 Author

Shaheen Akram

