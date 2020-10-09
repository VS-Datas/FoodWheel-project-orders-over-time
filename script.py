import codecademylib
from matplotlib import pyplot as plt
import pandas as pd

orders = pd.read_csv('orders.csv')

print orders.head()

orders['month'] = orders.date.apply(lambda x: x.split('-')[0])

print orders.head()

avg_order = orders.groupby('month').price.mean().reset_index()

std_order = orders.groupby('month').price.std().reset_index()

print(std_order)