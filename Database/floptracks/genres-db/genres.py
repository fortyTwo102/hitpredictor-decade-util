import csv
import os
from datetime import datetime
from pprint import pprint
import pickle
import operator


now = datetime.now() 
filename = 'logs//' + __file__ + now.strftime("_%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w')


decades = ['60','70','80','90','00','10']


for decade in decades:

	count = 0

	filename1 = 'flop-artist-objects-' + decade + '.p'
	filename2 = 'hit-artist-objects-' + decade + '.p'

	flop_artists = pickle.load(open(filename1,'rb'))
	hit_artists = pickle.load(open(filename2,'rb'))

	flop_genres = {}

	hit_genres = {}

	for artist in hit_artists:

		try:
			genres = artist['genres']
		except:
			pass	

		for genre in genres:

			if genre not in hit_genres:

				hit_genres[genre] = 1

			else:

				hit_genres[genre] += 1	

	for artist in flop_artists:

		try:
			genres = artist['genres']
		except:
			pass	

		for genre in genres:

			if genre not in flop_genres:

				flop_genres[genre] = 1

			else:

				flop_genres[genre] += 1	

	flop_genres_sorted = sorted(flop_genres.items(), key = lambda x: x[1], reverse = True)	
	hit_genres_sorted = sorted(hit_genres.items(), key = lambda x: x[1], reverse = True)	

	
	pickle.dump(flop_genres_sorted, open("flop-" + decade + "-genres.p", 'wb'))
	pickle.dump(hit_genres_sorted, open("hit-" + decade + "-genres.p", 'wb'))


	all_hits = set(hit_genres.keys())
	all_flops = set(flop_genres.keys())


	common = all_hits.intersection(all_flops)


	print(decade)

	common_dict = {}

	for each in common:

		common_dict[each] = (flop_genres[each], hit_genres[each])


	common_dict = sorted(common_dict.items(), key = lambda x: x[1])
	pprint(common_dict)
		
	print("\n\n\n\n")	




log.close()









