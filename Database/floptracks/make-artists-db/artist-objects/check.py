import json
import pandas as pd


data = pd.read_json('failed-artist-objects-60.txt', lines=True)

print(data)