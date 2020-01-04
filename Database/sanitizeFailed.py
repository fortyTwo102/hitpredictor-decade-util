# This script will remove a song from the failed list
# if it has charted on billboard.

import csv

decades = ['60','70','80','90','00','10']

for decade in decades:

	billboard = 'billboard' + decade + 'FeaturesDatabase.csv'
	failed = 'failed' + decade + 'Unique.csv'

	billboardSet = set()
	failedSet = set()

	count = 0
	count2 = 0

	with open(billboard, encoding='latin-1') as fp1, open(failed, encoding='latin-1') as fp2:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		for row in reader1:

			song = (row[0], row[1], row[2])
			billboardSet.add(song)

		for row in reader2:
			
			song = (row[0], row[1], row[2])

			if song in billboardSet:

				# print (song, 'has not flopped.')	

				count += 1

			else:
			
				failedSet.add(song)	

				count2 += 1

	failedUnique = 'failedFinal' + decade + 'Unique.csv'

	with open(failedUnique,'w+', encoding='utf-8', newline='') as fp:

		writer = csv.writer(fp)

		for song in failedSet:

			song = list(song)
			writer.writerow(song)

	print(decade, len(billboardSet), len(failedSet), count)				
			
