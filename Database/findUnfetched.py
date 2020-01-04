import csv

decades = ['60','70','80','90','00','10']

output = open("findUnfetched.csv", 'a', encoding = 'utf-8')

for decade in decades:

	count = 0

	file = 'billboard' + decade + 'FeaturesDatabase.csv'

	with open(file, encoding = 'latin-1') as fp:

		reader = csv.reader(fp)

		for row in reader:

			if len(row) == 3:

				print(",".join(row), file=output)

				count += 1
				print(row)

	print(decade + " is done!")			

output.close()	