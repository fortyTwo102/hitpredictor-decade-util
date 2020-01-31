import csv
import numpy as np
from sklearn.linear_model import LogisticRegression
from scipy import stats
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials
import os
from datetime import datetime
from pprint import pprint
import pickle
import time

'''now = datetime.now() 
filename = __file__ + now.strftime("_%d_%m_%Y_%H_%M_%S") + '.txt'
print("date and time =", filename)	
log = open(filename,'w+')

'''

print(__file__) 
error_log = open(__file__+  '.txt', 'a')			

def getSongFeatures(trackID):
	
	client_credentials_manager = SpotifyClientCredentials(client_id='87b136708f154032b21b7f3e618867a2',client_secret='e114dac3aeb94e83b68e601209af778b')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	attempt = 0

	respFeature = []

	while True:

		try:

			attempt += 1
			print("features attempt: ", attempt, end = ' ')
			respFeature = sp.audio_features(trackID)
			break

		except ConnectionError:

			print("ConnectionError was thrown, retrying.")
			time.sleep(100)

		except:
			print("Error. Retrying.")
			if attempt == 5:
				print("Error in features", trackID, file=error_log)
				break		

	print("Features done!")
		
	return respFeature

def getSongAnalysis(trackID):
	

	client_credentials_manager = SpotifyClientCredentials(client_id='ad3b6e58606c4b1d91832ecd0c160557',client_secret='e3f68c9f1c2b42e5a48a1d61e10fa0ab')
	sp = spotipy.Spotify(client_credentials_manager=client_credentials_manager)

	attempt = 0
	chorusHit = 0
	sections = 0
	respAnalysis = []

	try:
		attempt += 1
		print("analysis attempt: ", attempt, end = " ")
		respAnalysis = sp.audio_analysis(trackID)

		sections = len(respAnalysis['sections'])

		if sections > 3:
			chorusHit = respAnalysis['sections'][2]['start']
		elif sections > 2:
			chorusHit = respAnalysis['sections'][1]['start']	
		elif sections >= 1:
			chorusHit = respAnalysis['sections'][0]['start']
		else:
			chorusHit = 0	
	except:
		
		time.sleep(100)

		if attempt == 5:

			print("Error in", trackID, file=error_log) 		
		
	print("Analysis done!")

	return chorusHit, sections


# PROGRAM STARTS HERE--------------------------------------------------------

decades = ['70']


for decade in decades:

	count = 0

	filename1 = 'cleaned_flops_' + decade + '.p'
	filename2 = 'flop_features_' + decade + '_db4.p' 
#	filename3 = 'flop_analysis_' + decade + '_db.p' 
	filename4 = 'songs_fetched_' + decade + '4.p'

	header = ['Track','Artist','URI','danceability','energy','key',\
	'loudness','mode','speechiness','acousticness','instrumentalness',\
	'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']

	cleaned_flops = pickle.load(open(filename1, 'rb'))

	total = len(cleaned_flops)

	features = []

	analysis = []

	songs_fetched = []
	
	for song in cleaned_flops:

		track = song[0]
		artist = song[1]
		songURI = '4VdYJOe9CNF4vhJdr4TWQg'
		count += 1 
		print(track, 'by', artist)
		print(count, '/', total)

		songFeatures = getSongFeatures(songURI)
		(chorusHit, sections) = getSongAnalysis(songURI)

#		print(chorusHit, sections)

		if songFeatures:
#			print("here")
			songFeatures[0]['track'] = track
			songFeatures[0]['artist'] = artist
			songFeatures[0]['chorusHit'] = chorusHit
			songFeatures[0]['sections'] = sections
		

		features.append(songFeatures)
		songs_fetched.append(songURI)


		pickle.dump(features, open(filename2, 'wb'))	
		pickle.dump(songs_fetched, open(filename4, 'wb'))	

		break

	print(decade, 's done!--------------------------------------------------------------------------')




error_log.close()		








