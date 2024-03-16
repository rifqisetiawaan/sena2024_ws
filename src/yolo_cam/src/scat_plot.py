#!/usr/bin/env python3
import matplotlib.pyplot as plt
from scipy import stats
from sklearn.linear_model import LinearRegression

x = [88, 126, 149, 165] # jarak pixel
y = [40, 80, 120, 160] # jarak real (cm)

model = LinearRegression()
model.fit(x, y)
X_predict = 200
y_predict = model.predict([[X_predict]])