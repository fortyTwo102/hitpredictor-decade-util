import csv
import pickle

decades  = ['60','70','80','90','00','10']

for decade in decades:

	file1 = 'billboard' + decade + 'FeaturesDatabase.csv'
	file2 = 'hits'  + decade + '.p'

	with open(file1, 'r', encoding = 'latin-1') as fp:

		reader = csv.reader(fp)

		hits = set()

		for row in reader:

			if len(row) == 18 and 'sections' not in row:

				to_add = (row[0], row[1], row[2])
				hits.add(to_add)
				
	pickle.dump(hits, open(file2, 'wb'))		





