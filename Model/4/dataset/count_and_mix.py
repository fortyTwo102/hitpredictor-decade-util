import numpy as np

decades = ['60', '70', '80', '90', '00', '10']

for decade in decades:

	filename =  'dataset-of-' + decade + 's.txt'
	
	data = np.loadtxt(filename, delimiter='\t')
	X, y = data[:, :-1], data[:, -1]

	flop = 0
	hit = 0

	for target in y:

		if target == 0:

			flop += 1

		else:

			hit += 1

	print(decade, hit - flop)			
