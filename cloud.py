import numpy as np
import pandas as pd

from sklearn.cross_validation import train_test_split
from sklearn.tree import DecisionTreeClassifier
from sklearn.metrics import accuracy_score
from sklearn import tree

def dct(processed_text1,processed_text2,processed_text3,processed_text4,processed_text5):
	balance_data = pd.read_csv('./xyz.csv',sep= ',', header= None)

	#print ("Dataset Length:: ", len(balance_data))
	#print ("Dataset Shape:: ", balance_data.shape)

	X = balance_data.values[:, 0:5]
	Y = balance_data.values[:,5]

	#print(balance_data.head(5))
	#print(X)
	#print(Y)
	X_train, X_test, y_train, y_test = train_test_split( X, Y, test_size = 0.3, random_state = 100)

	clf_entropy = DecisionTreeClassifier(criterion = "entropy", random_state = 100,
	max_depth=10, min_samples_leaf=15)

	clf_entropy.fit(X_train, y_train)

	x = clf_entropy.predict([[int(processed_text1),int(processed_text2),int(processed_text3),int(processed_text4),int(processed_text5)]])
	print(x);
	y_pred_en = clf_entropy.predict(X_test)
	y_pred_en

	return str(x[0]);

if __name__=='__main__':
	dct();
