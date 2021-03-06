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
# import tensorflow.compat.v1 as tf
# tf.disable_v2_behavior()


'''def logger(details):

	for key in details:
		print(key," = ",details[key], file=log)
		print("\n", file=log)


	print("_"*100 + '\n\n\n', file=log)	'''

def visualize(data):

	header = ['danceability','energy','key',\
		'loudness','mode','speechiness','acousticness','instrumentalness',\
		'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']

	y_pos = np.arange(len(header))

	plt.bar(y_pos, data, align = 'center', alpha = 0.5)
	plt.xticks(y_pos, header)
	plt.ylabel("Feature Importance")
	plt.show()

decades = ['60', '70', '80', '90', '00', '10']

for decade in decades:

	details = {}
	
	filename = 'dataset/' + decade + 's.txt'
	path = os.path.join(filename)
	data = np.loadtxt(path, delimiter='\t')
	X, y = data[:, :-1], data[:, -1]

	# print("Shape of X", X.shape)
	# print("Shape of y", y.shape)

	X = preprocessing.scale(X)

	# X = featureNorm(X)


	X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=1/3, random_state=5)


	# model = skflow.TensorFlowDNNClassifier(hidden_units = [10,20,10], n_classes=3)
	model = XGBClassifier() #MLPClassifier(hidden_layer_sizes = (10,5), max_iter = 1000) # MLPClassifier(solver='lbfgs',alpha=1e-1,hidden_layer_sizes=(10,2), random_state=1)
	details["Decade"] = decade + "s"
	details["Model"] = model.fit(X_train, y_train)
	# details["Feature Importance"] = list(model.feature_importances_)
	
	try:	
		details["Co-Efficient"] = model.coef_

	except:
		pass	


	y_pred = model.predict(X_test)
	# predictions = [round(value) for value in y_pred]

	accuracy = round(100*float(metrics.accuracy_score(y_test, y_pred)),2)
	print(decade + "s Accuracy: ", accuracy)

	details["Accuracy"] = accuracy

	# logger(details)

	#visualize(list(details["Feature Importance"]))

	header = ['danceability','energy','key',\
		'loudness','mode','speechiness','acousticness','instrumentalness',\
		'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']
	#plot_importance(model, ylabel = header)
	#plt.show()

