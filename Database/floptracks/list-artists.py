import csv
import pandas as pd

decades = ['60', '70', '80', '90', '00', '10']

always_flop = set()
always_hit = set()


for decade in decades:

	file1 = 'old//failed' + decade + 'FeaturesDatabase.csv'
	file2 = 'old//billboard' + decade + 'FeaturesDatabase.csv'
	file3 = 'flop-hit-artists-' + decade + '.csv'

	with open(file1, encoding = 'latin-1') as fp1, open(file2, encoding = 'latin-1') as fp2, \
	open(file3, 'w', encoding = 'latin-1', newline = "") as fp3:

		reader1 = csv.reader(fp1)
		reader2 = csv.reader(fp2)
		writer = csv.writer(fp3)

		flops = set()
		hits = set()

		output = []

		for row in reader2:

			always_hit.add(row[1])
			hits.add(row[1])


		for row in reader1:

			try:
				if row[1] not in always_hit:
					flops.add(row[1])

			except:
				 pass		



		print(len(flops), len(hits))
		
		hits = pd.DataFrame(list(hits))
		flops = pd.DataFrame(list(flops))

		data = pd.concat([flops, hits], axis = 1)

		data.to_csv(file3, index = False, header = False)



