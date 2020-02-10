import csv
import pickle

decades = ['60', '70', '80', '90', '00', '10']


for decade in decades:

	data = pickle.load(open("flop_features_" + decade + "_db.p", "rb"))

	header = ['Track','Artist','URI','danceability','energy','key',\
	'loudness','mode','speechiness','acousticness','instrumentalness',\
	'liveness','valence','tempo','duration_ms','time_signature','chorusHit','sections']


	with open("flop_features_" + decade + "_db.csv", "w+", encoding = 'utf-8', newline = "") as f:


		writer = csv.writer(f)

		writer.writerow(header)

		for song in data:

			song_features = song[0]

			to_write = []

			to_write.append(song_features['track'])
			to_write.append(song_features['artist'])
			to_write.append(song_features['uri'])
			to_write.append(song_features['danceability'])
			to_write.append(song_features['energy'])
			to_write.append(song_features['key'])
			to_write.append(song_features['loudness'])
			to_write.append(song_features['mode'])
			to_write.append(song_features['speechiness'])
			to_write.append(song_features['acousticness'])
			to_write.append(song_features['instrumentalness'])
			to_write.append(song_features['liveness'])
			to_write.append(song_features['valence'])
			to_write.append(song_features['tempo'])
			to_write.append(song_features['duration_ms'])
			to_write.append(song_features['time_signature'])
			to_write.append(song_features['chorusHit'])
			to_write.append(song_features['sections'])
			writer.writerow(to_write)




