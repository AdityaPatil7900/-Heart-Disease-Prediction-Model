# ❤️ Heart Disease Prediction using Machine Learning

![Python](https://img.shields.io/badge/Python-3.9%2B-blue?logo=python)   

> 🩺 A machine learning-based web application that predicts the likelihood of heart disease based on patient health parameters. Built with Streamlit for a clean and interactive UI, ideal for healthcare demo projects and portfolios.

---

## ✨ Features
- 📊 Predicts heart disease risk using medical attributes (age, cholesterol, blood pressure, etc.)
- ⚡ Real-time prediction with user-friendly web interface
- 🔢 Preprocessing with **StandardScaler** for accurate results
- 🧠 Trained with multiple ML algorithms; optimized model used for deployment
- 📈 Visualizes insights from training dataset

---

## 🧠 How It Works
1. User inputs **medical data** (age, sex, cholesterol, etc.) through UI.  
2. Data is **scaled using pre-trained scaler** for consistency.  
3. **Trained ML model (Logistic Regression / RandomForest)** predicts probability of heart disease.  
4. Displays **risk prediction** in a clear, user-friendly result card.

---

## 🛠️ Tech Stack
| Technology | Role |
|------------|------|
| Python | Programming Language |
| Streamlit | Web App Framework |
| Scikit-Learn | Machine Learning Model |
| Pandas/Numpy | Data Preprocessing |
| Matplotlib/Seaborn | Data Visualization |

---

## 📸 Screenshots
| Input Form | Prediction Result |
|------------|-------------------|
| ![form](Images/Screenshot%202025-08-03%20102616.png) | ![result](Images/Screenshot%202025-08-03%20102652.png) |

---
## 📁 Project Structure
```
│
├── app.py               # Streamlit application
├── heart_model.pkl      # Trained ML model
├── scaler.pkl           # Scaler for preprocessing
├── dataset.csv          # Dataset used for training
├── requirements.txt     # Dependencies
├── README.md            # Project documentation
└── Images/
    └── screenshot.png   # App screenshot
```
--- 

## 🚀 Getting Started

### 🔧 Installation
```bash
# Clone the repository
git clone https://github.com/AdityaPatil7900/Heart-Disease-Prediction.git
cd Heart-Disease-Prediction

# Install dependencies
pip install -r requirements.txt

# Run the Streamlit application
streamlit run app.py
```
---
## 👤 Author
**[Aditya Patil]**  
🔗 [LinkedIn](https://www.linkedin.com/in/aditya-patil-aj7900/)<br> 

---
