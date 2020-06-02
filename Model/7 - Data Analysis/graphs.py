import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns


data = pd.read_csv(os.path.join('dataset', 'dataset-of-10s.csv'))
print(data)