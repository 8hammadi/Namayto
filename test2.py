import pandas as pd 
import random

data = pd.read_csv("csv/en_fr.csv") 
r=data.to_dict()
leng=len(r["English words/sentences"])

#mode random
i=random.randint(0,leng-1)
print(r["English words/sentences"][i])
print(r["French words/sentences"][i])

