import csv

decades = ['60','70','80','90','00','10']


for decade in decades:
	
	flopSet = set()

	# billboard = 'billboard' + decade + 'FeaturesDatabase.csv'

	flop = 'failed' + decade + 'FeaturesDatabase.csv'

	file = open(flop[:-4] + 'X.txt', 'w', encoding = 'latin-1')

	with open(flop, encoding = 'latin-1') as fp2:

		# reader1 = csv.reader(fp1)

		reader2 = csv.reader(fp2)

		for row in reader2:

			if 'sections' in row:
				pass

			elif len(row) == 18:

				row.append(0)
				row = tuple(row)
				flopSet.add(row)

		for song in flopSet:
		
			song = list(song)
			song = [str(x) for x in song]

			print('\t'.join(song[3:]), file=file)	

	print(decade + 's is done!')		

