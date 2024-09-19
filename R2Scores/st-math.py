import numpy as np
import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.utils import shuffle
from sklearn.metrics import mean_absolute_error

data = pd.read_csv("https://raw.githubusercontent.com/amankharwal/Website-data/master/student-mat.csv")

data = data[["G1", "G2", "G3", "studytime", "failures", "absences"]]

predict = "G3"
x = np.array(data.drop([predict], 1))
y = np.array(data[predict])

print(x.shape)
print(y.shape)

from sklearn.model_selection import train_test_split
xtrain, xtest, ytrain, ytest = train_test_split(x, y, test_size=0.2)

# mean absolute error - with numpy
def mae_np(y_true, predictions):
    y_true, predictions = np.array(y_true), np.array(predictions)
    return np.mean(np.abs(y_true - predictions))

# mean_absolute_error - using sklearn library
def mae_sklearn(y_true, predictions):
    y_true, predictions = np.array(y_true), np.array(predictions)
    return mean_absolute_error(y_true, predictions)



linear_regression = LinearRegression()
linear_regression.fit(xtrain, ytrain)
predictions = linear_regression.predict(xtest)

# Calculation of R2 Score
from sklearn.model_selection import cross_val_score
print(cross_val_score(linear_regression, x, y, cv=10, scoring="r2").mean())

print(mae_sklearn(ytest, predictions))

