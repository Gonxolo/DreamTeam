import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import copy
from datetime import datetime, timedelta
import pickle

import datetime as dt
import sys

from sklearn import tree
from sklearn.tree import DecisionTreeClassifier
from sklearn.model_selection import train_test_split, cross_val_score
from sklearn.ensemble import RandomForestClassifier



#CAMBIAR RUTA ACORDE A LA CARPETA DONDE TIENEN MATRIZ.csv

rutaMC = r"MATRIZ.csv"
MC = pd.read_csv(rutaMC)

caracteristicas = ['movieYear', 'Crime', 'Drama', 'Mistery', 'Documentary', 'Action', 'Sci-Fi', 'Comedy', 'Romance', 'Thriller', 'Music', 'Biography', 'Family', 'Musical', 'Horror', 'Animation', 'Adventure', 'Fantasy', 'War', 'History', 'Western', 'Film-Noir', 'Sport', 'Short', 'Mystery', 'Antiguedad']

X = MC.loc[:,caracteristicas].to_numpy()

etiqueta = ["Ranking Binario"]
y = MC.loc[:,etiqueta].to_numpy()

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25)


### ARBOL DE DECISION ###

ad = DecisionTreeClassifier() # Creando el modelo

ad.fit(X_train, y_train)

Y_pred = ad.predict(X_test)

from sklearn.metrics import confusion_matrix

tn, fp, fn, tp = confusion_matrix(y_test, Y_pred).ravel()

correctitud = (tp+tn)/float(tp+fp+fn+tn)
sensibilidad = (tp)/float(tp+fn)
especificidad = (tn)/float(fp+tn)
precision = (tp)/float(tp+fp)
tasa_real = (tp+fn)/float(tp+fp+fn+tn)
f1_score = 2*(precision*sensibilidad)/float(precision+sensibilidad)

print("correctitud: " + str(np.round(correctitud*100,2)) + "%")
print("sensibilidad: " + str(np.round(sensibilidad*100,2)) + "%")
print("especificidad: " + str(np.round(especificidad*100,2)) + "%")
print("precision: " + str(np.round(precision*100,2)) + "%")
print("tasa_real: " + str(np.round(tasa_real*100,2)) + "%")
print("f1_score: " + str(np.round(f1_score*100,2)) + "%")

aD = [correctitud, sensibilidad, especificidad, precision, tasa_real, f1_score]


### RANDOM FOREST ###

rf = RandomForestClassifier() # Creando el modelo

rf.fit(X_train, y_train)

Y_pred = rf.predict(X_test)

tn, fp, fn, tp = confusion_matrix(y_test, Y_pred).ravel()

correctitud = (tp+tn)/float(tp+fp+fn+tn)
sensibilidad = (tp)/float(tp+fn)
especificidad = (tn)/float(fp+tn)
precision = (tp)/float(tp+fp)
tasa_real = (tp+fn)/float(tp+fp+fn+tn)
f1_score = 2*(precision*sensibilidad)/float(precision+sensibilidad)

print("correctitud: " + str(np.round(correctitud*100,2)) + "%")
print("sensibilidad: " + str(np.round(sensibilidad*100,2)) + "%")
print("especificidad: " + str(np.round(especificidad*100,2)) + "%")
print("precision: " + str(np.round(precision*100,2)) + "%")
print("tasa_real: " + str(np.round(tasa_real*100,2)) + "%")
print("f1_score: " + str(np.round(f1_score*100,2)) + "%")

rF = [correctitud, sensibilidad, especificidad, precision, tasa_real, f1_score]

################### CROSS VALIDATION #######################

cv_ad_f1 = cross_val_score(DecisionTreeClassifier(), X, y, cv=10, scoring='f1')

print(cv_ad_f1)

cv_rf_f1 = cross_val_score(RandomForestClassifier(), X, y, cv=10, scoring='f1')

print(cv_rf_f1)

a = np.mean(cv_ad_f1)

b = np.mean(cv_rf_f1)

print(a)

print(b)

finalDict = {"arbolDecision":aD, "randomForest":rF, "aD Cross-Val":cv_ad_f1, "rF Cross-Val":cv_rf_f1, "aD Mean":a, "rF Mean":b}

with open("machineLearningData.pkl","wb") as f:
    pickle.dump(finalDict,f)


