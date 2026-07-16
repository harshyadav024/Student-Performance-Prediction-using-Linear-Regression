# Student-Performance-Prediction-using-Linear-Regression
A machine learning project that predicts student performance using Linear Regression with Python, Pandas, Scikit-learn, and Matplotlib.

# 🎓 Student Performance Prediction using Machine Learning

Predict student **Total Scores** using **Linear Regression** based on academic performance metrics such as study hours, attendance, quizzes, projects, and participation.

---

## 📌 Project Overview

This project demonstrates the complete workflow of a **Supervised Machine Learning Regression** model using **Python** and **Scikit-learn**.

The model learns the relationship between a student's academic performance and their final score, then predicts the total score for new students based on their input.

---

## 🚀 Features

- 📂 Load student dataset using Pandas
- 📊 Perform data preprocessing
- 🤖 Train a Linear Regression model
- 📈 Predict student total scores
- 📉 Evaluate model performance using regression metrics
- 📊 Visualize score distribution
- 📈 Compare Actual vs Predicted Scores
- 💻 Predict scores using custom user input

---

## 📂 Dataset Features

### Input Features

- Study Hours per Week
- Attendance
- Midterm Score
- Project Score
- Participation Score
- Quiz Average

### Target Variable

- Total Score

---

## 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib

---

## 📊 Machine Learning Workflow

1. Import required libraries
2. Load the dataset
3. Select input and target variables
4. Train a Linear Regression model
5. Predict student scores
6. Evaluate the model
7. Visualize the results
8. Predict scores for new student data

---

## 📈 Model Evaluation Metrics

The model is evaluated using:

- Mean Absolute Error (MAE)
- Mean Squared Error (MSE)
- Root Mean Squared Error (RMSE)
- R² Score

---

# 📊 Output Visualizations

## Distribution of Total Scores

Shows how student scores are distributed across the dataset.

![Distribution of Total Scores](https://github.com/harshyadav024/Student-Performance-Prediction-using-Linear-Regression/blob/main/ml_project/distribution_of_total_scores.png)

---

## Actual vs Predicted Scores

Compares the model's predicted scores with the actual student scores.

![Actual vs Predicted Scores](https://github.com/harshyadav024/Student-Performance-Prediction-using-Linear-Regression/blob/main/ml_project/actual_vs_predicted_scores.png)

---

## 📁 Project Structure

```
ML_PROJECT/
│
├── project.py
├── Student_Performance_Dataset_5000_v2.csv
├── distribution_of_total_scores.png
├── actual_vs_predicted_scores.png
├── about.txt
└── README.md
```

---

## ▶️ Installation

Clone the repository

```bash
git clone https://github.com/your-username/student-performance-prediction.git
```

Move into the project folder

```bash
cd student-performance-prediction
```

Install dependencies

```bash
pip install pandas numpy matplotlib scikit-learn
```

Run the project

```bash
python project.py
```

---

## 💻 Example Prediction

The program accepts user input such as:

```
Study Hours per Week: 25
Attendance: 92
Midterm Score: 80
Project Score: 85
Participation Score: 88
Quiz Average: 79
```

Example Output

```
Predicted Total Score: 83.47
```

---

## 📚 Skills Demonstrated

- Data Analysis
- Data Preprocessing
- Feature Selection
- Linear Regression
- Model Evaluation
- Data Visualization
- Machine Learning using Scikit-learn
- Python Programming

---

## 🔮 Future Improvements

- Train/Test Split for unbiased evaluation
- Feature Scaling
- Cross Validation
- Hyperparameter Tuning
- Decision Tree Regression
- Random Forest Regression
- Gradient Boosting Regression
- Streamlit Web App Deployment
- Model Serialization using Pickle

---

## 👨‍💻 Author

**Harsh Yadav**

- Delhi Technological University (DTU)
- IIT Guwahati BS in Data Science & Artificial Intelligence

---
