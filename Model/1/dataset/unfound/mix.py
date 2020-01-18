import csv

decades = ['60','70','80','90','00','10']


for decade in decades:

	billSet = set()
	flopSet = set()

	billboard = 'billboard' + decade + 'FeaturesDatabase.csv'
	flop = 'failed' + decade + 'FeaturesDatabase.csv'

	billdataset = open('billdataset', 'w', encoding = 'latin-1')
	flopdataset = open('flopdataset', 'w', encoding = 'latin-1')

	with open(billboard, encoding = 'latin-1') as fp1, open(flop, encoding = 'latin-1') as fp2:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		for 