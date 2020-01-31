import pickle

data_60_1 = pickle.load(open('flop_features_60_db1.p', 'rb'))

data_60_2 = pickle.load(open("flop_features_60_db2.p", "rb"))

data_70_1 = pickle.load(open("flop_features_70_db1.p", "rb"))

data_70_2 = pickle.load(open("flop_features_70_db2.p", "rb"))

data_70_3 = pickle.load(open("flop_features_70_db3.p", "rb"))

data_70_4 = pickle.load(open("flop_features_70_db4.p", "rb"))


data_70_2[0][0]['track'] = 'Alazao Claroes'
data_70_2[0][0]['artist'] = 'Ednardo'

data_60_1[0][0] = data_60_2[0][0]
data_70_1[0][0] = data_70_3[0][0]
data_70_2[0][0] = data_70_4[0][0]

print(len(data_70_1))
print(len(data_70_2))

data_70_1.extend(data_70_2)


print(len(data_70_1))


pickle.dump(data_60_1, open("flop_features_60_db.p", "wb")) #Merged
pickle.dump(data_70_1, open("flop_features_70_db.p", "wb")) #Merged
pickle.dump(data_70_1, open("flop_features_70_db.p", "wb"))

