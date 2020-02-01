import pickle
from pprint import pprint
import time

data = pickle.load(open('genres-dict.p', 'rb'))


f = open("genres-dict.txt", "w")

pprint(data)