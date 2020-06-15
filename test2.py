import pandas as pd 
import random

data = pd.read_csv("data/csv/True.csv") 
r=data.to_dict()
# dict_keys(['title', 'text', 'subject', 'date'])

leng=len(r["title"])

i=random.randint(0,leng-1)
print(r["title"][i])
print(r["text"][i])
print(r["subject"][i])
print(r["data"][i])