from sklearn import tree
clf=tree.DecisionTreeClassifier()
X=[['45','56',7],['123','54','8'],['76','54','5'],['335','65','4']]
Y=['female','male','male','female']
clf=clf.fit(X,Y)
prediction=clf.predict(X,Y)
print(prediction)
