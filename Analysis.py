import numpy as np
import pandas as pd 
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import BaggingClassifier

###### Change directory
os.chdir("/Users/shen/Desktop/Homework/parsed_results/")

dataset = pd.read_csv("BoardGameGeekClean.csv")

np.any(np.isnan(dataset))
#print(dataset.shape)
######################### RandomForest Analysis ####################
target = dataset.iloc[:,7].values

data = dataset[['AvgRating','GeekRating', 'ListPrice', 'NumVoters']]

data_training, data_test, target_training, target_test = train_test_split(data,target, test_size = 0.2, random_state = 1)



random_forest_machine = RandomForestClassifier(n_estimators=11)

random_forest_machine.fit(data_training,target_training)


print(accuracy_score(target_test,predictions))

#print(data.head())
	









