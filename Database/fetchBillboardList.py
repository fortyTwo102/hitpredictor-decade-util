import billboard
import csv
import pandas as pd
import time

def getChartOf(weekOf):
	chart = billboard.ChartData('hot-100', weekOf)
	print(weekOf)
	charts = []

	with open('billboard10.csv', 'a+', newline='') as csv_file:
		csv_writer = csv.writer(csv_file)
		date = str(chart.date)
		charts.append(date)
		for song in chart.entries:
			charts.append([song.title, song.artist])

		csv_writer.writerows([charts])



def allsaturdays(year=None):
    return pd.date_range(start='2010-01-02', end='2019-12-27', 
                         freq='28D').strftime('%Y-%m-%d').tolist()

saturdays = allsaturdays()


while True:
	for saturday in saturdays:
		try:
			getChartOf(saturday)
		except:
			print("Time Out.. Waiting.")
			time.sleep(100)
			getChartOf(saturday)

	print("DONE!")
	break			
			