import pandas as pd
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.metrics import mean_squared_error
from sklearn.metrics import mean_absolute_error
from sklearn.metrics import r2_score
from sklearn.metrics import accuracy_score
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier
from sklearn.linear_model import LogisticRegression

def process(path,s):
	dataset=pd.read_csv(path).values
	x1 = dataset[:,0:5]
	y1 = dataset[:,5] # define the target variable (dependent variable) as y
	print(x1)
	print(y1)
	#X_train, X_test, y_train, y_test = train_test_split(x1, y1)

	#x2=[29,84,80,1002,7]
	print(s)
	x2=s
	x=np.asarray(x2).reshape(1,-1)
	model2=RandomForestClassifier(n_estimators=10,criterion='entropy',random_state=42)
	model2.fit(x1, y1)
	rf_pred = model2.predict(x)
	print(rf_pred)

	model2=LogisticRegression()
	model2.fit(x1,y1)
	lr_pred = model2.predict(x)
	print(lr_pred)
	return rf_pred,lr_pred
	
#process("results/data2.csv")




