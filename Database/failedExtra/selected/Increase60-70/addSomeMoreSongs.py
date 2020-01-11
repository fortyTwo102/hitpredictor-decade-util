import csv

failedFull = set()
failedSelected = set()


decades = {

	'60' : 560,
	'70' : 500,

}

for decade in decades.keys():


	songsExtra = set()

	with open('track-artist-uri-' + decade + '.csv', encoding = 'latin-1') as fp1, \
	open('track-artist-uri-' + decade + '-cleaned.csv',  encoding = 'latin-1') as fp2:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		for row in reader1:

			failedFull.add(tuple(row))

		for row in reader2:

			failedSelected.add(tuple(row))

		unselected = failedFull - failedFull.intersection(failedSelected)


		count = decades[decade]

		for song in unselected:

			songsExtra.add(song)

			count -= 1

			if count == 0:
				break

	with open('track-artist-uri-' + decade + '-extra.csv', 'w', encoding = 'latin-1', newline = '') as fp:


		writer = csv.writer(fp)

		for song in songsExtra:

			song = list(song)

			writer.writerow(song)




