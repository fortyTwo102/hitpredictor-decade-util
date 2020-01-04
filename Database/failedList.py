# Now we need to make the final failed songs list
# Their number should be equal to the number of 
# billboard/hit songs of that decade


import csv

decades = ['60','70','80','90','00','10']

for decade in decades:

	billboard = 'billboard' + decade + 'FeaturesDatabase.csv'
	failed = 'failedFinal' + decade + 'Unique.csv'

	billboardSet = set()
	failedSet = set()

	count = 0
	# count2 = 0

	with open(billboard, encoding='latin-1') as fp1, open(failed, encoding='latin-1') as fp2:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		for row in reader1:

			song = (row[0], row[1], row[2])
			billboardSet.add(song)

		for row in reader2:
			
			song = (row[0], row[1], row[2])
			failedSet.add(song)	

	billCount = len(billboardSet)	

	failedEqual = 'failedEqual' + decade + 'Unique.csv'

	with open(failedEqual,'w+', encoding='utf-8', newline='') as fp:

		writer = csv.writer(fp)

		for song in failedSet:

			song = list(song)
			writer.writerow(song)

			count += 1

			if count == billCount:
				break

	# print(decade, len(billboardSet), len(failedSet), count)				
			
print("done!")