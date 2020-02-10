import csv

decades = ['60','70','80','90','00','10']


for decade in decades:

	billSet = set()
	flopSet = set()

	tracks = set()

	billboard = 'billboard' + decade + 'FeaturesDatabase.csv'
	flop = 'flop_features_' + decade + '_db.csv'

	# billdataset = open('billdataset', 'w', encoding = 'latin-1')
	# flopdataset = open('flopdataset', 'w', encoding = 'latin-1')

	with open(billboard, encoding = 'latin-1') as fp1, open(flop, encoding = 'utf-8') as fp2:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		for row in reader1:

			if 'sections' in row:
				pass

			elif len(row) == 18:

				row.append(1)
				row = tuple(row)
				billSet.add(row)

		for row in reader2:

			if 'sections' in row:
				pass

			elif len(row) == 18:

				row.append(0)
				row = tuple(row)
				flopSet.add(row)

		tracks = billSet.union(flopSet)

		header = ['track', 'artist', 'uri', 'danceability','energy','key',\
		'loudness','mode','speechiness','acousticness','instrumentalness',\
		'liveness','valence','tempo','duration_ms','time_signature','chorus_hit','sections','target']			

		with open('dataset-of-' + decade + 's.csv', 'w', encoding = 'utf-8', newline = '') as f:

			writer = csv.writer(f)
			writer.writerow(header)

			for song in tracks:

				song = list(song)
				song = [str(x) for x in song]

				writer.writerow(song)


	print(decade + 's is done!')		

