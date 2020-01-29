from pandas import read_csv
import pandas as pd
import os
from sklearn import tree
from sklearn.model_selection import train_test_split


filename = 'wuhan.csv'
dataFrame = pd.read_csv(filename)
print("number of row = {}  number of column = {}".format(dataFrame.shape[0],dataFrame.shape[1]))


array = dataFrame.values
X = array[:,0:2]
Y = array[:,2]


X_train, X_test, Y_train, Y_test = train_test_split(X, Y,test_size=0.30, random_state=0)
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)

score = clf.score(X_test, Y_test)
print("score = {}".format(score))

while(True):
    ans = True
    while(ans):
        city = str(input("Did you come from Wuhan(y/n) ? = "))
        if city == "y":
            city = 1
            ans = False
            
        elif city == "n":
            city = 0
            ans = False
        else : ans = True
    temp = int(input("Temp = "))
    prediction = clf.predict([[city,temp]])    
    print(prediction)
