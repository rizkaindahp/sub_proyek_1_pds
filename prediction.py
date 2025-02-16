import pandas as pd
import pickle

# Load model yang sudah dilatih
model_path = "attrition_rf_model.pkl"
model = pickle.load(open(model_path, "rb"))

# Masukkan data yang ingin diprediksi
X_new = pd.DataFrame({
    'Age': [35], 
    'BusinessTravel': [0], 
    'DailyRate': [1100], 
    'Department': [1], 
    'DistanceFromHome': [5], 
    'Education': [3], 
    'EducationField': [0], 
    'EnvironmentSatisfaction': [3],
    'Gender': [1], 
    'HourlyRate': [70], 
    'JobInvolvement': [3], 
    'JobLevel': [2], 
    'JobRole': [1], 
    'JobSatisfaction': [4], 
    'MaritalStatus': [1], 
    'MonthlyIncome': [5000], 
    'MonthlyRate': [20000], 
    'NumCompaniesWorked': [1], 
    'OverTime': [1], 
    'PercentSalaryHike': [12], 
    'PerformanceRating': [3], 
    'RelationshipSatisfaction': [4], 
    'StockOptionLevel': [1], 
    'TotalWorkingYears': [10], 
    'TrainingTimesLastYear': [3], 
    'WorkLifeBalance': [3], 
    'YearsAtCompany': [5], 
    'YearsInCurrentRole': [2], 
    'YearsSinceLastPromotion': [1], 
    'YearsWithCurrManager': [3], 
})

# Model akan memprediksi
y_pred = model.predict(X_new)

print("Hasil Prediksi:", y_pred)
