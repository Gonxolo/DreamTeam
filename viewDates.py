import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
import matplotlib.pyplot as plt
import numpy as np
import csv


viewDateList = []

with open('combined_data_vCorta.csv') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',')
    next(spamreader, None)
    for row in spamreader:
        viewDateList.append(row[3])

for i in range(len(viewDateList)):
    viewDateList[i] = viewDateList[i].split("-")
    viewDateList[i] = [viewDateList[i][0]]

with open('viewDates.csv', 'w', newline='\n') as newfile:
    writer = csv.writer(newfile)
    writer.writerows(viewDateList)



# plt.hist(x, density=True, bins=30)  # `density=False` would make counts
# plt.ylabel('Probability')
# plt.xlabel('Data');
