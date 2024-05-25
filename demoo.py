from sklearn import tree

X = [[181,90,44], [177,70,43], [160,60,38], [166,65,40], [190,100,47],[187,97,45],[158,50,36]]
Y = ['male', 'female' , 'female' , 'male', 'male','male','female']
clf = tree.DecisionTreeClassifier()
clf = clf.fit(X,Y)
height=float(input("enter height in cm="))
weight=float(input("enter weight in kg="))
shoe_size=float(input("enter shoe size ="))
prediction = clf.predict([[190,70,43]])
print (prediction)
