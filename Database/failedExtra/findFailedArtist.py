import csv

decades = ['60','70','80','90','00','10']


for decade in decades:

	output = open('failed' + decade + 'Artist.txt', 'w', encoding = 'latin-1')

	failed = 'failed' + decade + 'FeaturesDatabase.csv'

	artists = set()

	with open(failed, encoding = 'latin-1') as fp:

		reader = csv.reader(fp)

		for row in reader:

			artists.add(row[1])

	for artist in artists:
	
		print(artist, file = output)	

	print(decade + 's is done!')		

