import csv

decades = ['60','70','80','90','00','10']

unfound = open('unFetchedFeaturesDataset.csv', 'a', encoding = 'latin-1')

for decade in decades:


	file = 'failed' + decade + 'FeaturesDatabase.csv'

	with open(file, encoding = 'latin-1') as fp: #, open(flop, encoding = 'latin-1') as fp2:

		reader = csv.reader(fp)


		for row in reader:

			if len(row) == 3:

				print(row)
				print(",".join(row), file = unfound)

	print(decade + 's done!')	
	# print(decade + 's done!', file = unfound)		
