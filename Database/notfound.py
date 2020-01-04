# So I feel like some songs are not being fetched
# because of issues with artist's name, like when
# the songs "features" two artists and neither one get found
# I made the changes from 80s list onward to accomodate for that
# but I still have to fix this 60s and 70s one
# but first, I need a list of missed out songs and thats what this
# script does.

import sys
import csv

decade = '10'

file1 = 'billboard' + decade + 'Unique.csv'
file2 = 'billboard' + decade + 'FeaturesDatabase.csv'

uniqueTracks = set()
fetchedTracks = set()

with open(file1) as fp1, open(file2) as fp2:

	reader1 = csv.reader(fp1)
	reader2 = csv.reader(fp2)

	for row in reader1:

		song = (row[0],row[1])	
		uniqueTracks.add(song)

	for row in reader2:
	
		song = (row[0],row[1])
		fetchedTracks.add(song)

notFound = uniqueTracks - fetchedTracks


with open("notFound" + decade + '.csv', 'w', newline='') as fp:

	writer = csv.writer(fp)

	for song in notFound:

		song = list(song)
		writer.writerow(song)