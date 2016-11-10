from sklearn.pipeline import Pipeline
from sklearn.preprocessing import PolynomialFeatures
from sklearn.linear_model import LinearRegression
from sklearn import model_selection
import pandas as pd
import numpy as np
from sklearn.metrics import mean_squared_error, r2_score

df = pd.read_csv('kc_house_data.csv')
data = df.values

X = data[:, :data.shape[1] - 1]
y = data[:, -1]

kfold = model_selection.KFold(n_splits = 10, shuffle = True)

test_scores, train_scores, test_rmse, train_rmse = np.array([]), np.array([]), np.array([]), np.array([])

for train_index, test_index in kfold.split(X):

	lr = LinearRegression(normalize=True)
	polynomial_features = PolynomialFeatures(degree=2, include_bias = False)

	model = Pipeline([	("polynomial_features", polynomial_features),
                        ("linear_regression", lr)])
	X_train, X_test = X[train_index], X[test_index]
	y_train, y_test = y[train_index], y[test_index]

	model.fit(X_train, y_train)

	y_train_pred = model.predict(X_train)
	y_test_pred = model.predict(X_test)

	train_scores = np.append(train_scores, r2_score(y_train, y_train_pred))
	test_scores = np.append(test_scores, r2_score(y_test, y_test_pred))
	test_rmse = np.append(test_rmse, mean_squared_error(y_test, y_test_pred)**0.5)
	train_rmse = np.append(train_rmse, mean_squared_error(y_train, y_train_pred)**0.5)

	y_train_pred = model.predict(X_train)


print train_scores.mean(), train_rmse.mean()
print test_scores.mean(), test_rmse.mean()


