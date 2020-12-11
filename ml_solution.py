__author__ = 'cripton'
# https://www.hackerrank.com/challenges/correlation-and-regression-lines-7
# http://scikit-learn.org/stable/modules/linear_model.html
from sklearn import linear_model



X= [[15], [12], [8],  [8],  [7],  [7],  [7],  [6], [5], [3] ]
y= [10, 25, 17, 11, 13, 17, 20, 13, 9, 15]

clf = linear_model.LinearRegression()
# Create linear regression object
regr = linear_model.LinearRegression()

# Train the model using the training sets
regr.fit(X, y)

# The coefficients
print('Coefficients: \n', regr.coef_)
#print round(regr.coef_,3)