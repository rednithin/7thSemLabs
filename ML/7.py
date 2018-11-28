import numpy as np
import pandas as pd
import csv
from pgmpy.estimators import MaximumLikelihoodEstimator
from pgmpy.models import BayesianModel
from pgmpy.inference import VariableElimination

heartDisease = pd.read_csv('7-dataset.csv', names=['age', 'sex', 'cp', 'trestbps', 'chol',
                                                   'fbs', 'restecg', 'thalach', 'exang', 'oldspeak', 'slope', 'ca', 'thal', 'heartdisease'])
heartDisease = heartDisease.replace("?", np.nan)

print(heartDisease.head())

model = BayesianModel([('age', 'trestbps'), ('age', 'fbs'), ('sex', 'trestbps'), ('exang', 'trestbps'), ('trestbps', 'heartdisease'),
                       ('fbs', 'heartdisease'), ('heartdisease',
                                                 'restecg'), ('heartdisease', 'thalach'),
                       ('heartdisease', 'chol')])

model.fit(heartDisease, estimator=MaximumLikelihoodEstimator)
HeartDisease_infer = VariableElimination(model)

print("1. Probability Of Heart Disease Given Age = 28")
q = HeartDisease_infer.query(variables=['heartdisease'], evidence={'age': 28})
print(q["heartdisease"])

print("2. Probability Of Heart Disease Given Chol (cholestrol) = 100")
q = HeartDisease_infer.query(
    variables=['heartdisease'], evidence={'chol': 25})
print(q['heartdisease'])
