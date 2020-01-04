# Using this to keep track of both billboard tracks and 
# failed tracks that I've fetched so far
import csv
decades = ['60','70','80','90','00','10']


for decade in decades:

	billboard = 'billboard' + decade + 'FeaturesDatabase.csv'
	failed = 'failedEqual' + decade + 'Unique.csv'

	with open(billboard, encoding='latin-1') as fp1, open(failed, encoding='latin-1') as fp2:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)

		billCount = 0
		failedCount = 0


		for row in reader1:
			billCount += 1

		for row in reader2:

			failedCount += 1

		print(decade, billCount, failedCount)		
