from sklearn import svm, model_selection, datasets

iris = datasets.load_iris()
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = model_selection.GridSearchCV(svr, parameters)
print clf.fit(iris.data, iris.target)