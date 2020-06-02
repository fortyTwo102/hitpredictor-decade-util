import sklearn
from sklearn.cluster import AffinityPropagation
import matplotlib.pyplot as plt
from itertools import cycle
import numpy as np
import os
from sklearn import metrics, preprocessing 

decades = ['60', '70', '80', '90', '00', '10']

for decade in decades[:1]:

	details = {}
	
	filename = 'dataset/' + decade + 's.txt'
	path = os.path.join(filename)

	if decade == '60':
		data = np.loadtxt(path, delimiter='\t')

	else:	
		data = np.append(data, np.loadtxt(path, delimiter='\t'), axis = 0)

	print(data.shape)	

	X, y = data[:, :-1], data[:, -1]

	X = preprocessing.scale(X)

	af = AffinityPropagation(verbose = True).fit(X)
	cluster_centers_indices = af.cluster_centers_indices_
	labels = af.labels_

	no_clusters = len(cluster_centers_indices)

	print(no_clusters)

	plt.close('all')
	plt.figure(1)
	plt.clf()

	colors = cycle('bgrcmykbgrcmykbgrcmykbgrcmyk')
	for k, col in zip(range(no_clusters), colors):
	    class_members = labels == k
	    cluster_center = X[cluster_centers_indices[k]]
	    plt.plot(X[class_members, 0], X[class_members, 1], col + '.')
	    plt.plot(cluster_center[0], cluster_center[1], 'o', markerfacecolor=col, markeredgecolor='k', markersize=14)
	    for x in X[class_members]:
	        plt.plot([cluster_center[0], x[0]], [cluster_center[1], x[1]], col)

	plt.show()