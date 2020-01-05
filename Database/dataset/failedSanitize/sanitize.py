# To find tracks from artist that have songs in the bilboard list

import csv

decades = ['60','70','80','90','00','10']

for decade in decades:

	billboard = 'billboard' + decade + 'FeaturesDatabase.csv'
	failed = 'failed' + decade + 'FeaturesDatabase.csv'

	with open(billboard, encoding = 'latin-1') as fp1, open(failed, encoding = 'latin-1') as fp2:


		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		failedArtists = set()
		hitArtists = set()

		for row in reader2:

			if 'sections' not in row:

				artist = row[1]

				failedArtists.add(artist)

		for row in reader1:
		
			if 'sections' not in row:

				artist = row[1]

				hitArtists.add(artist)

		common = failedArtists.intersection(hitArtists)

	with open(failed, encoding = 'latin-1')  as fp2, open('sanitized/'+failed, 'a', encoding = 'latin-1', newline = "") as fp3:
	
		reader2 = csv.reader(fp2)
		writer = csv.writer(fp3)

		count = 0

		for row in reader2:

			artist = row[1]

			if artist in hitArtists:
				count += 1

			else:
				writer.writerow(row)


		print(count)		

	print(decade + 's is done.')					 