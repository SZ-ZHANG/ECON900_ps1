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

dataset = pd.read_csv("BoardGameGeekClean_Miss.csv")

#np.any(np.isnan(dataset))
#print(dataset.shape)
######################### RandomForest Analysis ####################
target = dataset.iloc[:,7].values

data = dataset[['AvgRating','GeekRating', 'ListPrice', 'NumVoters']]

data_training, data_test, target_training, target_test = train_test_split(data,target, test_size = 0.2, random_state = 1)
	


random_forest_machine = RandomForestClassifier(n_estimators=11)

random_forest_machine.fit(data_training,target_training)

predictions = random_forest_machine.predict(data_test)

print(accuracy_score(target_test,predictions))


confusion_matrix = pd.DataFrame(
	confusion_matrix(target_test,predictions),
	columns = ['predict 1', 'Predict 2', 'Predict 3','Predict 4'],
	index = ['True 1','True 2','True 3','True 4' ]
	)
		

print(confusion_matrix)

print(dict(zip(data.columns, 
	random_forest_machine.feature_importances_)))


######## Data set without the Missing Values #######
#### We do the exactly same thing but without the information of Missing value
### We use the data set 'BoardGameGeekClean_Miss.csv' which do not contain missing value.
## We also get the accuracy_score and confusion matrix
## Code is same but switch the dataset 






