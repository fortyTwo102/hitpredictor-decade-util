import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from datetime import datetime
import json
from pprint import pprint
import pickle

uniqueBucket = set() # To remove duplicate tracks all over playlists

now = datetime.now() 
filename = 'logs//' + __file__ + now.strftime("_%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w')

def getArtist(artistName):

	client_credentials_manager = SpotifyClientCredentials(client_id='87b136708f154032b21b7f3e618867a2',client_secret='e114dac3aeb94e83b68e601209af778b')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	
	artists = sp.search(q='artist:' + artistName,type='artist',limit=10)

	for artist in artists['artists']['items']:

		if artistName.lower() in artist['name'].lower():

			return artist

decades = ['60','70']


for decade in decades:

	count = 0

	data  = []

	filename = 'list-flop-and-hit-artists//flop-hit-artists-' + decade + '.csv'
	artist_obj_db = 'flop-artist-objects-' + decade +  '.p'

	with open(filename, encoding='latin-1') as fp1:

		reader = csv.reader(fp1)

		#print(writer.writerow(header), file=log)


		for row in reader:
			
			artist = row[0]

			artist_obj = getArtist(artist)

			data.append(artist_obj)

			pickle.dump(data, open(artist_obj_db,'wb'))

			count += 1

			print(count)

					
log.close()









