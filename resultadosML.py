import pickle

with open("machineLearningData.pkl","rb") as f:
    finalDict = pickle.load(f)

for key, value in finalDict.items():
    print(key, value)