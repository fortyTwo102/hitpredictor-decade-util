import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
import pprint
from datetime import datetime

uniqueBucket = set() # To remove duplicate tracks all over playlists

now = datetime.now() 
filename = 'log' + now.strftime("%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w+')


def makeUniqueBucket(): # To remove duplicate tracks all over playlists
	global uniqueBucket

	decades = ['60','70','80','90','00','10']

	for decade in decades:

		file = 'failedSongs' + decade + '.csv'

		with open(file, encoding='utf-8') as fp:

			reader = csv.reader(fp)

			for row in reader:

				song = (row[0], row[1], row[2])

				uniqueBucket.add(song)





def writeToFile(track, artist, uri, releaseDate, releaseDatePrec):

	global uniqueBucket

	song = (track, artist, uri)

	if song in uniqueBucket:
		print("Song already fetched in", releaseDate, file=log)
		return

	else:
		uniqueBucket.add(song)	

	if releaseDatePrec == 'day':
		releaseDateObj = datetime.strptime(releaseDate, '%Y-%m-%d')

	elif releaseDatePrec == 'month':
		releaseDateObj = datetime.strptime(releaseDate, '%Y-%m')

	elif releaseDatePrec == 'year':
		releaseDateObj = datetime.strptime(releaseDate,'%Y')



	if releaseDateObj >= datetime(1960,1,1) and releaseDateObj <= datetime(1969,12,31):
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
		problemTracks(track, artist, uri)
		return

	if decade not in ('00','10'):
		return

	file = 'failedSongs' + decade + '.csv'

	with open(file,'a', encoding='utf-8', newline='') as fp:

		writer = csv.writer(fp)
		writer.writerow([track, artist, uri])

		print(track, 'by', artist, 'is written to', decade, file=log)
	


def fetchPlaylist(ID, off):

	client_credentials_manager = SpotifyClientCredentials(client_id='79730d009d364b1b9ee81745626e69aa',client_secret='5cfde76bb72f43eaa500e2e019ed52fa')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	return sp.user_playlist_tracks(user='paperboats97', playlist_id=ID, offset=off*100)

def problemTracks(track, artist, uri):

	print("PROBLEM", track, artist, uri, releaseDate, releaseDatePrec)

	with open('failedSongsProblem.csv', 'a', encoding='utf-8', newline='') as fp:

		writer = csv.writer(fp)
		writer.writerow([track, artist, uri])

'''playlists = [

'spotify:playlist:5T38LTxcDS5eGIyDXWvCKL',
'spotify:playlist:2wB2BSgekCDIWXFpvGuHkp',
'spotify:playlist:2XaeKTfGkXbl7azxOGFT8B',
'spotify:playlist:4hTSi1yGbvUzPanMIUvXAi',
'spotify:playlist:52dVCmKe3SVkbsNs46P3Zt',
'spotify:playlist:1n0uEdue65pITMkeaprgFv',
'spotify:playlist:07UmiBiNfu538BlX12IGVY',
'spotify:playlist:58F0dtGg2ShDVEnS7OaCkV',
'spotify:playlist:6E3Dra7wUEMmumKs8FddmP',
'spotify:playlist:5pQ8B5MD9lWDBU2J98EscC',
'spotify:playlist:4EwXmKdmadS95GeCsSK32D',
'spotify:playlist:4HBjN53ACJmMSPKaLbQUv2', 
'spotify:playlist:7oKsKC5P5x2z2i0MCtRJ2B',
'spotify:playlist:6NmEPWZCTs469cU8eVhe4v',
'spotify:playlist:4VORkMBsPxCX6V9eIbNVYk',
'spotify:playlist:6ee6LBovYNOIQfVsKmNZTS',
'spotify:playlist:7bE2sQM5iaumauvqlAeP48',
'spotify:playlist:5pQ8B5MD9lWDBU2J98EscC',
'spotify:playlist:2XaeKTfGkXbl7azxOGFT8B',
'spotify:playlist:4hTSi1yGbvUzPanMIUvXAi',
'spotify:playlist:1DmzPOzqsNjQQJEPSc9nHN',


]'''

playlists = [

'spotify:playlist:4j53v3ELuxx4wMx5AgrP9Q',

]

makeUniqueBucket()

for ID in playlists:

	for offset in range(80):
		playlist = fetchPlaylist(ID, offset)

		items = playlist['items']

		for song in items:

			artist = song['track']['artists'][0]['name']
			track = song['track']['name']
			uri = song['track']['uri']
			releaseDate = song['track']['album']['release_date']
			releaseDatePrec = song['track']['album']['release_date_precision']

			# print(releaseDate, releaseDatePrec)

			try:
				writeToFile(track, artist, uri, releaseDate, releaseDatePrec)

			except:		
				problemTracks(track, artist, uri)



log.close()