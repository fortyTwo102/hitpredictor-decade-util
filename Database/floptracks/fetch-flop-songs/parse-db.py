import pickle

from pprint import pprint

database = pickle.load(open("genre+year+database.p", "rb"))

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

for decade in decades:

	song_uris = set()

	for genre in genres[decade]:

		for offsets in database[decade][genre]:

			for song in offsets['tracks']['items']:

				uri = song['uri']

				song_uris.add(uri)


	print(len(song_uris))	

	if decade == '10':

		
		pprint(database[decade])		