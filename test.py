import numpy as np
import pandas as pd 
import os
import matplotlib.pyplot as plt
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
from sklearn.metrics import confusion_matrix
from sklearn.ensemble import BaggingClassifier
from sklearn.neighbors import KNeighborsClassifier

###### Change directory
os.chdir("/Users/shen/Desktop/Homework/parsed_results/")
	
######## Data set without the Missing Values #######
#### We do the exactly same thing but without the information of Missing value


dataset_Miss = pd.read_csv("BoardGameGeekClean.csv")

#np.any(np.isnan(dataset))
#print(dataset.shape)
######################### RandomForest Analysis ####################
target = dataset_Miss.iloc[:,7].values

data = dataset_Miss[['AvgRating','GeekRating', 'ListPrice', 'NumVoters']]

data_training, data_test, target_training, target_test = train_test_split(data,target, test_size = 0.2, random_state = 1)
	
knn = KNeighborsClassifier(n_neighbors=6)

knn.fit(data_training, target_training)

#random_forest_machine.fit(data_training,target_training)

predictions = knn.predict(data_test)

print(accuracy_score(target_test,predictions))


confusion_matrix2 = pd.DataFrame(
	confusion_matrix(target_test,predictions),
	columns = ['predict 1', 'Predict 2', 'Predict 3','Predict 4'],
	index = ['True 1','True 2','True 3','True 4' ]
	)
		

print(confusion_matrix2)

#print(dict(zip(data.columns, 
#	knn.feature_importances_)))







