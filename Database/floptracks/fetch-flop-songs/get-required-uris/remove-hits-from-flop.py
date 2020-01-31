import csv
import pickle

decades  = ['60','70','80','90','00','10']

hit_artist = set() # To remove flop songs by artists that have appeared in the hit list 

for decade in decades:

	file1 = 'hits'  + decade + '.p'
	file2 = 'song_uris_' + decade + '.p'
	file3 = 'cleaned_flops_' + decade + '.p'

	cleaned_flops = set()

	hits_set = pickle.load(open(file1, 'rb'))	
	flops = pickle.load(open(file2, 'rb'))

	for hit_song in hits_set:

		hit_artist.add(hit_song[1])

	count = 0

	limit = len(hits_set)

	for flop_track in flops:

		if (flop_track not in hits_set) and (flop_track[1] not in hit_artist):

			cleaned_flops.add(flop_track)

			count += 1

			if count == limit:

				break

			
	cleaned_flops = list(cleaned_flops)
	
	pickle.dump(cleaned_flops, open(file3, 'wb'))	
	
	print(len(hits_set), len(flops), len(cleaned_flops))	


	for each in cleaned_flops:

		print












