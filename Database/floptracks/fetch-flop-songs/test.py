import pickle
from pprint import pprint
import time

data = pickle.load(open('cleaned_flops_70.p', 'rb'))

print(len(data))