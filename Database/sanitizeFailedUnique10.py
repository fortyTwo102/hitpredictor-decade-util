# 

import csv

c=0

decade = '10'
songs = set()

with open('failed' + decade + 'Unique.csv', encoding='latin-1') as fp:

	reader = csv.reader(fp)

	for row in reader:

		track = row[0]

		if 'remaster' in track.lower():
			c += 1
			pass

		else:
			songs.add((row[0], row[1], row[2]))

	failedUnique = 'failedSongsFinal' + decade + 'Unique.csv'
			
	with open(failedUnique,'w+', encoding='utf-8', newline='') as fp:
	
		writer = csv.writer(fp)
	
		for song in songs:
	
			song = list(song)
			writer.writerow(song)	


print(len(songs), c)			
		
