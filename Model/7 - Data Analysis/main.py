import os
import numpy as np
import matplotlib.pyplot as plot
from sklearn.model_selection import train_test_split
from xgboost import XGBClassifier
from xgboost import plot_importance
from sklearn import metrics, preprocessing 
from sklearn.neural_network import MLPClassifier
from sklearn.linear_model import LogisticRegression
from sklearn.ensemble import RandomForestClassifier
# import skflow
from datetime import datetime
import matplotlib.pyplot as plt


decades = ['60', '70', '80', '90', '00', '10']



for decade in decades:

	details = {}
	
	filename = 'dataset/' + decade + 's.txt'
	path = os.path.join(filename)

	if decade == '60':
		data = np.loadtxt(path, delimiter='\t')

	else:	
		np.append(data, np.loadtxt(path, delimiter='\t'), axis = 0)


X, y = data[:, :-1], data[:, -1]

X = preprocessing.scale(X)


X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=5)

model = XGBClassifier() #MLPClassifier(hidden_layer_sizes = (10,5), max_iter = 1000) # MLPClassifier(solver='lbfgs',alpha=1e-1,hidden_layer_sizes=(10,2), random_state=1)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

accuracy = round(100*float(metrics.accuracy_score(y_test, y_pred)),2)
print("Accuracy: ", accuracy)
