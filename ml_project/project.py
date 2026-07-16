import pandas as pd
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.metrics import mean_squared_error, mean_absolute_error, r2_score
import matplotlib.pyplot as plt

# load dataset
data = pd.read_csv("/Users/harshyadav/Desktop/ml_project/Student_Performance_Dataset_5000_v2.csv")

# Input and output
X = data[["study_hours_per_week", "Attendance", "Midterm", "Project", "participation_score", "quizzes_avg"]]
y= data["total_score"]

# train model 
model = LinearRegression()
model.fit(X,y)
predicted_scores = model.predict(X)

# Valid regression matrices
mae = mean_absolute_error(y, predicted_scores)
mse = mean_squared_error(y, predicted_scores)
rsme = np.sqrt(mse)
r2 = r2_score(y, predicted_scores)

# show result
print("Mean Absolute Error (MAE):", round(mae,2))
print("Mean Squared Error (MSE):", round(mse,2))
print("Root Mean Squared Error (RMSE):", round(rsme,2))
print("R-squared (R2)[accuracy]:", round(r2,5)) # close to 1 means better accuracy

# predict new data
new_hours = float(input("Study hours per week: "))
attendance = float(input("Attendance: "))
midterm = float(input("Midterm score: "))
project = float(input("Project score: "))
participation = float(input("Participation score: "))
quiz = float(input("Quiz average: "))

new_student = pd.DataFrame({
    "study_hours_per_week": [new_hours],
    "Attendance": [attendance],
    "Midterm": [midterm],
    "Project": [project],
    "participation_score": [participation],
    "quizzes_avg": [quiz]
})

marks = model.predict(new_student)

print("Predicted total score:", round(marks[0], 2))

# Histogram 
plt.figure(figsize =(10,6))
plt.hist(data["total_score"], bins = 30, color = 'blue',edgecolor = 'black')
plt.title("Distribution of Total Scores")
plt.xlabel("Total Score")
plt.ylabel("No of students")
plt.show()

# scatter + regression line
plt.figure(figsize=(8,6))

plt.scatter(y, predicted_scores, alpha=0.6)

plt.plot(
    [y.min(), y.max()],
    [y.min(), y.max()],
    color='red',
    linewidth=2
)

plt.xlabel("Actual Scores")
plt.ylabel("Predicted Scores")
plt.title("Actual vs Predicted Scores")
plt.grid(True)
plt.show()

