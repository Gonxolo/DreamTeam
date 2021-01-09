import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import matplotlib.pyplot as plt
import numpy as np
import csv
import json


genreDict = {}

df = pd.read_csv("test.csv")
with open('movieExtraInfo.json') as jsonfile:
    data = json.load(jsonfile)
    i=0
    for key, value in data.items():
        if value["Response"] == "True":
            generos = value["Genre"]
            L = generos.split(", ")
            for j in L:
                df.at[i,j] = 1
            # break
            # if "Crime" in L:
            #     i[3] = 1
            # if "Drama" in L:
            #     i[4] = 1
            # if "Mistery" in L:
            #     i[5] = 1
            # if "Documentary" in L:
            #     i[6] = 1
            # if "Action" in L:
            #     i[7] = 1
            # if "Sci-Fi" in L:
            #     i[8] = 1
            # if "Comedy" in L:
            #     i[9] = 1
            # if "Romance" in L:
            #     i[10] = 1
            # if "Thriller" in L:
            #     i[11] = 1
            # if "Music" in L:
            #     i[12] = 1
            # if "Biography" in L:
            #     i[13] = 1
            # if "Family" in L:
            #     i[14] = 1
            # if "Musical" in L:
            #     i[15] = 1
            # if "Horror" in L:
            #     i[16] = 1
            # if "Animation" in L:
            #     i[17] = 1
            # if "Adventure" in L:
            #     i[18] = 1
            # if "Fantasy" in L:
            #     i[19] = 1
            # if "War" in L:
            #     i[20] = 1
            # if "History" in L:
            #     i[21] = 1
            # if "Western" in L:
            #     i[22] = 1
            # if "Film-Noir" in L:
            #     i[23] = 1
            # if "Sport" in L:
            #     i[24] = 1
            # if "Short" in L:
            #     i[25] = 1
        # for i in L:
        #     try: genreDict[i] += 1
        #     except: genreDict[i] = 1
        else: pass
        i+=1

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
df.to_csv("test.csv", index=False)

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

# df.to_csv("test.csv", index=False)


# for i in range(len(viewDateList)):
#     viewDateList[i] = viewDateList[i].split("-")
#     viewDateList[i] = [viewDateList[i][0]]

# with open('genreCount.csv', 'w', newline='\n') as newfile:
#     writer = csv.writer(newfile)
#     writer.writerows(genre)
