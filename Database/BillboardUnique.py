import csv
import ast

#decades = ['60','70','80','90','00','10']

#decades = ['00']

#['60','70','80','90']

for decade in decades:

	filename = 'billboard' + decade

	songlist = set()
	songCount = 0
	count=10

	with open(filename + '.csv') as fp1, open(filename+'Unique' + '.csv', 'w', newline="") as fp2:

		reader = csv.reader(fp1) # First file has raw fetched Billboard Charts
		writer = csv.writer(fp2) # This is going to have unique songs

		for row in reader: 

			row = row[1:] #Removing the date

			for song in row:

				songCount += 1
				track = list(ast.literal_eval(song)) #since its a list turned into a string
				track = tuple(track) #need to store in a set
				songlist.add(track)

		for song in songlist:
		
			song = list(song)

			writer.writerow(song)		



	print("songCount:", songCount, "setCount:", len(songlist))






