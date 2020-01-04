import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os

def getSongURI(trackName,artistName):

	client_credentials_manager = SpotifyClientCredentials(client_id='79730d009d364b1b9ee81745626e69aa',client_secret='5cfde76bb72f43eaa500e2e019ed52fa')
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
			
			

def getSongFeatures(trackID):
	

	client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	data = []
	#FETCHING TRACK NAME AND ARTIST NAME
	try:

		#FETCHING ARTIST DETAILS
		respTrack = sp.track(trackID)

		artistID = respTrack['artists'][0]['id']

		artistFetched = respTrack['artists'][0]['name']
		trackFetched =  respTrack['name']

		respArtist = sp.artist(artistID)
		#data.append(respArtist['popularity'])


		#FETCHING AUDIO FEATURES

		respFeature = sp.audio_features(trackID)
		featureFields = list(respFeature[0].keys())

		for key in featureFields:
			if key in {'type','track_href','uri','id','analysis_url'}:
				pass
			else:	
				data.append(respFeature[0][key])
	


		#FETCHING AUDIO ANALYSIS

		respAnalysis = sp.audio_analysis(trackID)
		chorusHit = respAnalysis['sections'][2]['start']
		sections = len(respAnalysis['sections'])
		data.append(chorusHit)
		data.append(sections)
		
	except:
		print("Error in fetching "+ trackID)
		
		
	return data

decades = ['90']#,'70','80','90','00','10']


for decade in decades:

	filename1 = 'billboard' + decade + 'Unique.csv'
	filename2 = 'billboard' + decade + 'FeaturesDatabase.csv'

	with open(filename1) as fp1, open(filename2,'a',newline="") as fp2:

		reader = csv.reader(fp1)
		writer = csv.writer(fp2)

		header = ['Track','Artist','URI','danceability','energy','key',\
		'loudness','mode','speechiness','acousticness','instrumentalness',\
		'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']

		#print(writer.writerow(header))

		for _ in range(392):

			next(reader)


		for row in reader:

			track = row[0]
			artist = row[1]

			fetchedDetails = [track, artist]

			print("Fetching",row,"....",end="")


			songURI = getSongURI(track, artist)

			if songURI:


				songFeatures = getSongFeatures(songURI)

				fetchedDetails.append(songURI)
				fetchedDetails = fetchedDetails + songFeatures

				print("Fetched!")
				print(fetchedDetails)
	

				print(writer.writerow(fetchedDetails))

			else:
			
				print(row, "Not Found!")	
			

print("70s are DONE!")			










