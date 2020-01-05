import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from datetime import datetime
from pprint import pprint

# uniqueBucket = set() # To remove duplicate tracks all over playlists

now = datetime.now() 
filename = __file__ + now.strftime("_%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w+')

findUnfetchedOP = open('findUnfetchedOP.csv', 'w', encoding = 'utf-8')


def getDecadeAlbums(artist, decade):

	client_credentials_manager = SpotifyClientCredentials(client_id='87b136708f154032b21b7f3e618867a2',client_secret='e114dac3aeb94e83b68e601209af778b')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	

	
	artistObj = sp.search(q='artist:' + artist,type='artist',limit=10)

	items = artistObj['artists']['items']


	if items:
		
		artistURI = items[0]['uri']

	else:
		artistURI = 'spotify:artist:3qkxZa9xd3ZFcKVC7DRhMH'	

	albums = sp.artist_albums(artistURI)
	
	return albums		

'''	result = track['tracks']['items']

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
				return uri'''
			
def getTracksfromAlbum(album, _decade):



	client_credentials_manager = SpotifyClientCredentials(client_id='87b136708f154032b21b7f3e618867a2',client_secret='e114dac3aeb94e83b68e601209af778b')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)
	

	uri = album['uri']
	releaseDate = album['release_date']
	releaseDatePrec = album['release_date_precision']

	if releaseDatePrec == 'day':
		releaseDateObj = datetime.strptime(releaseDate, '%Y-%m-%d')

	elif releaseDatePrec == 'month':
		releaseDateObj = datetime.strptime(releaseDate, '%Y-%m')

	elif releaseDatePrec == 'year':
		releaseDateObj = datetime.strptime(releaseDate,'%Y')



	if releaseDateObj >= datetime(1950,1,1) and releaseDateObj <= datetime(1969,12,31):
		decade = '60'

	elif releaseDateObj >= datetime(1970,1,1) and releaseDateObj <= datetime(1979,12,31):
		decade = '70'	

	elif releaseDateObj >= datetime(1980,1,1) and releaseDateObj <= datetime(1989,12,31):	
		decade = '80'
	
	elif releaseDateObj >= datetime(1990,1,1) and releaseDateObj <= datetime(1999,12,31):
		decade = '90'	

	elif releaseDateObj >= datetime(2000,1,1) and releaseDateObj <= datetime(2009,12,31):
		decade = '00'	

	elif releaseDateObj >= datetime(2010,1,1) and releaseDateObj <= datetime(2019,12,31):
		decade = '10'	

	else:
		print("PROBLEM", uri)
		return



	if _decade == decade:
		
		return sp.album_tracks(uri)




decades = ['60','70','80','90','00','10']


for decade in decades:

	count = 0

	filename1 = 'failed' + decade + 'Artist.txt'
	filename2 = 'track-artist-uri-' + decade + '.csv'

	with open(filename1, encoding='latin-1') as fp1, open(filename2,'a',newline="", encoding='latin-1') as fp2:

		reader = fp1.readlines()
		writer = csv.writer(fp2)

		header = ['Track','Artist','URI','danceability','energy','key',\
		'loudness','mode','speechiness','acousticness','instrumentalness',\
		'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']

		#print(writer.writerow(header), file=log)

		for row in reader:

			print(decade, row)
			
			artist = row

			albums = getDecadeAlbums(artist, decade)



			for album in albums['items']:

				tracks = getTracksfromAlbum(album, decade)

				#pprint(tracks)

				if tracks:

					for track in tracks['items']:

						trackName = track['name']
						artistName = track['artists'][0]['name']
						songURI = track['uri']

						writer.writerow([trackName, artistName, songURI])

					
					
log.close()
findUnfetchedOP.close()
print("Unfounds are DONE!")			










