from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
import pandas as pd
import numpy as np

df = pd.read_csv('kc_house_data.csv')
data = df.values

X = data[:, :data.shape[1] - 1]
y = data[:, -1]

kfold = model_selection.KFold(n_splits = 10, shuffle = True, random_state = 5)

test_scores, train_scores = np.array([]), np.array([])

for train_index, test_index in kfold.split(X):

	lr = LinearRegression(normalize=True)
	polynomial_features = PolynomialFeatures(degree=3, include_bias = False)

	model = Pipeline([	("polynomial_features", polynomial_features),
                        ("linear_regression", lr)])
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]

	model.fit(X_train, y_train)

	train_scores = np.append(train_scores, model.score(X_train, y_train))
	test_scores = np.append(test_scores, model.score(X_test, y_test))


print train_scores.mean(), train_scores.std()
print test_scores.mean(), test_scores.std()


