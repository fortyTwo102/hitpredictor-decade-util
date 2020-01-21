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

# To remove duplicate tracks all over playlists

now = datetime.now() 
filename = 'logs//' + __file__ + now.strftime("_%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w')

def getSongsByGenreAndDecade(genre, decade, off):

	client_credentials_manager = SpotifyClientCredentials(client_id='87b136708f154032b21b7f3e618867a2',client_secret='e114dac3aeb94e83b68e601209af778b')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)


	if decade in ('60','70','80','90'):
		year = '19' + decade + '-' + '19' + str(int(decade) + 9)	
	elif decade == '10' :
		year = '20' + decade + '-' + '20' + str(int(decade) + 9)
	else:
		year = '2000-2009'	

	tracks = sp.search(q="genre:" + genre + " year:" + year, type = 'track', limit = 50, offset = 50*off, market = 'US')

	return tracks
	

def populateSet(song_uris, database, genre, decade):

	for genre in genres[decade]:

		for offsets in database[decade][genre]:

			for song in offsets['tracks']['items']:

				uri = song['uri']

				song_uris.add(uri)

	return song_uris	

decades = ['60','70','80','90','00','10']

genres = {
	
	'60':[	
			"avant-garde", 
			'experimental',
			'experimental rock',
			'post-punk',
			'art pop',
			'experimental rock',
			'post-punk',
			'art pop',
			'no wave',
			'metalcore',
			'instrumental rock',
			'new americana',
			'chicano punk',
			'classical',
			'australian metal', 
			'sleep',
			'space rock',
			'glam metal',
			'metal',
		],

	'70':[	
			'avant-garde',
			'metalcore',
			'uk post-punk',
			'spiritual jazz',
			'noise pop',
			'industrial',
			'free improvisation',
			'industrial rock',
			'slow core',
			'avant-garde jazz',
			'emo',
			'glam punk',
			'post-screamo',
			'deep free jazz',
			'melodic hardcore',
			'garage psych',
			'noise rock',
			'doom metal',
			'cyberpunk',
			'folktronica',

		],

	'80':[
			'avant-garde',
			'indie psychedelic rock',
			'industrial',
			'groove metal'
			'noise rock',
			'post-disco soul',
			'minimal wave',
			'power metal',
			'slow core',
			'death metal',
			'crossover thrash',
			'cancion melodica',
			'progressive metal',
			'post-hardcore',
			'grunge',
			'dark post-punk',
			'shoegaze',
			'electro-industrial',
			'hardcore punk',
			'ethereal wave',
			'garage psych',
			'industrial metal',
			'nu gaze',
			'outsider',
			'math rock',
			'doom metal',

		],
	'90':[
			'avant-garde',
			'math rock',
			'noise rock',
			'no wave',
			'experimental',
			'punk blues',
			'death metal',
			'progressive metal',
			'noise punk',
			'art punk',
			'electro-industrial',
			'classic psychedelic rock',
			'post-metal',
			'post-hardcore',
			'shoegaze',
			'melodic metal',
			'screamo',
			'hardcore',
			'instrumental post-rock',
			'dreamgaze',
			'british post-rock',
			'doom metal',
		],
	'00' :[
			'avant-garde',
			'poetry',
			'british experimental',
			'melodic death metal',
			'melodic metalcore',
			'metalcore',
			'death metal',
			'neofolk',
			'post-rock',
			'swedish metal',
			'doom metal',
			'martial industrial',
			'gothic metal',
			'finnish metal',
			'viking metal',
			'post-hardcore',
			'pagan black metal',
			'brutal death metal',
			'deathgrind',
			'instrumental post-rock',
			'symphonic black metal',
			'sludge metal',
			'deathcore',
			'black metal',
			'folk metal',
			'freak folk', 
			'finnish death metal',
			'melodic metal',
			'american post-rock',
			'drone metal',
			'atmospheric post-rock',
			'dreamo',
			'psychedelic doom',
			'uk doom metal',
			'boston metal',
			'british post-rock',
			'lo-fi beats',
		],

	'10' :[

			'avant-garde',
			'poetry',
			'metalcore',
			'melodic metalcore',
			'post-rock',
			'instrumental post-rock',
			'melodic death metal',
			'post-screamo',
			'post-metal',
			'screamo',
			'doom metal',
			'lo-fi beats',
			'post-doom metal',
			'death metal',
			'stoner metal',
			'sludge metal',
			'pagan black metal',
			'indie r&b', 
			'american post-rock',
			'stoner rock',
			'drone metal',
			'psychedelic doom',
			'brutal death metal',
			'progressive metal',
			'swedish metal',
			'speed metal',
			'voidgaze',
			'gymcore',
			'deathcore',
			'chillhop',
			'compositional ambient',
			'power metal',
			'gothic metal',
			'spanish post-rock',
			'german post-rock',
			'thrash metal',
			'slow core',
			'russian post-rock',
			'hardcore',

		],

}

pickle.dump(genres, open("genres-dict.p", "wb"))

database = {

	"60": {},
	"70": {},
	"80": {},
	"90": {},
	"00": {},
	"10": {},

}

try:

	for keys in database:

		for genre in genres[keys]:

			database[keys][genre] = []
	

	for decade in decades:

		limit = 7000
		song_uris = set()

		for i in range(1000):

			for genre in genres[decade]:


				if len(song_uris) > limit:
					break

				print("offset: ",i, "genre: ", genre, "songs_yet: ", len(song_uris))

				database[decade][genre].append(getSongsByGenreAndDecade(genre, decade, i))
				pickle.dump(database, open("genre+year+database.p", "wb"))

				song_uris = populateSet(song_uris, database, genre, decade)


			if len(song_uris) > limit:
				break

		print(decade, "s are done!----------------------------------------------------------------------------------------------")


except:

	print("Uh oh, something happened.")
	pickle.dump(database, open("genre+year+database.p", "wb"))		
	raise

	

					
log.close()









