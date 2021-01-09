import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import csv
import json


genreDict = {}

df = pd.read_csv("test2.csv")

with open('movieExtraInfo.json') as jsonfile:
    data = json.load(jsonfile)
    i = 0
    for key, value in data.items():
        print(i)
        if value["Response"] == "True":
            generos = value["Genre"]
            anno = value["Year"]
            L = generos.split(", ")
            while int(df.at[i,"id_movie"]) == int(key):
                try:
                    df.at[i,"movieYear"] = anno
                except:
                    pass
                for j in L:
                    df.at[i,j] = 1
                i+=1
                if i == 3768690:
                    break
        
        else:
            while int(df.at[i,"id_movie"]) == int(key):
                df.at[i,"movieYear"] = 0
                # for j in L:
                #     df.at[i,j] = 1
                i+=1

        if i == 3768690:
            break



# df["movieYear"] = 0
# df["Crime"] = 0
# df["Drama"] = 0
# df["Mistery"] = 0
# df["Documentary"] = 0
# df["Action"] = 0
# df["Sci-Fi"] = 0
# df["Comedy"] = 0
# df["Romance"] = 0
# df["Thriller"] = 0
# df["Music"] = 0
# df["Biography"] = 0
# df["Family"] = 0
# df["Musical"] = 0
# df["Horror"] = 0
# df["Animation"] = 0
# df["Adventure"] = 0
# df["Fantasy"] = 0
# df["War"] = 0
# df["History"] = 0
# df["Western"] = 0
# df["Film-Noir"] = 0
# df["Sport"] = 0
# df["Short"] = 0
# df["Mystery"] = 0


df["movieYear"].astype('int')
df["Crime"].astype('int')
df["Drama"].astype('int')
df["Mistery"].astype('int')
df["Documentary"].astype('int')
df["Action"].astype('int')
df["Sci-Fi"].astype('int')
df["Comedy"].astype('int')
df["Romance"].astype('int')
df["Thriller"].astype('int')
df["Music"].astype('int')
df["Biography"].astype('int')
df["Family"].astype('int')
df["Musical"].astype('int')
df["Horror"].astype('int')
df["Animation"].astype('int')
df["Adventure"].astype('int')
df["Fantasy"].astype('int')
df["War"].astype('int')
df["History"].astype('int')
df["Western"].astype('int')
df["Film-Noir"].astype('int')
df["Sport"].astype('int')
df["Short"].astype('int')
df["Mystery"].astype('int')


print(genreDict)
df.to_csv("test2.csv", index=False)





