import pandas as pd 
import random

data = pd.read_csv("en_fr.csv") 
r=data.to_dict()
leng=len(r["English words/sentences"])

#mode random
i=random.randint(0,leng-1)
print(r["English words/sentences"][i])
print(r["French words/sentences"][i])

# 
z="E500"
i=int(z[1:])%(leng)
print(r["English words/sentences"][i])

#
z="F500"
i=int(z[1:])%(leng)
print(r["French words/sentences"][i])


# F545
# E5455
# F* -> sentences +id
# E* -> sentences +id