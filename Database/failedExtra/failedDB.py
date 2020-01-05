import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from datetime import datetime

uniqueBucket = set() # To remove duplicate tracks all over playlists

now = datetime.now() 
filename = __file__ + now.strftime("_%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w+')

findUnfetchedOP = open('findUnfetchedOP.csv', 'w', encoding = 'utf-8')


def getSongURI(trackName,artistName):

	client_credentials_manager = SpotifyClientCredentials(client_id='87b136708f154032b21b7f3e618867a2',client_secret='e114dac3aeb94e83b68e601209af778b')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	

	
	track = sp.search(q='artist:' + artistName+' track:'+trackName,type='track',limit=10)

	result = track['tracks']['items']

	for each in result:
		for artist in each['artists']:			
			if artist['name'].lower() == artistName.lower():
				uri = each['uri']
				artistName = artist['name']
				return uri

			


	track = sp.search(trackName,type='track',limit=50)

	result = track['tracks']['items']

	for each in result:
		for artist in each['artists']:			
			if artist['name'].lower() == artistName.lower():
				uri = each['uri']
				artistName = artist['name']
				return uri

	for each in result:
		for artist in each['artists']:			
			if artist['name'].lower() in artistName.lower():
				uri = each['uri']
				artistName = artist['name']
				return uri
			


decades = ['60','70','80','90','00','10']


for decade in decades:

	count = 0

	filename1 = 'failed' + decade + 'Artists.csv'
	filename2 = 'track-artist-uri-' + decade + '.csv'

	with open(filename1, encoding='latin-1') as fp1, open(filename2,'a',newline="", encoding='latin-1') as fp2:

		reader = csv.reader(fp1)
		writer = csv.writer(fp2)

		header = ['Track','Artist','URI','danceability','energy','key',\
		'loudness','mode','speechiness','acousticness','instrumentalness',\
		'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']

		#print(writer.writerow(header), file=log)

		for row in reader:
			
			artist = row[0]

			albums = getDecadeAlbums(artist, decade)

			for album in albums:

				tracks = getTracksfromAlbum(album)

				for track in tracks:

					trackName = 
					artistName = 
					songURI = 

					writer.writerow([trackName, artistName, songURI])

					
log.close()
findUnfetchedOP.close()
print("Unfounds are DONE!")			










