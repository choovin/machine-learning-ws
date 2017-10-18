# 2.1.视频: sklearn 中的 K 折 CV
可通过简单的方式随机化 sklearn k 折 CV 中的事件，就是将 shuffle 标志设置为 true。
之后，代码将从如下所示：
```
cv = KFold( len(authors), 2 )
变为如下所示：
cv = KFold( len(authors), 2, shuffle=True )
```

# 5. sklearn 中的 GridSearchCV

GridCV 用于系统地彻底检查参数调整的多种组合，并在确定哪次调整带来最佳性能时进行交叉验证。它的好处是，只需增加几行代码，就能彻底检查许多种组合。
下面是来自 sklearn 文档的一个示例（详见此处）：
```
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
svr = svm.SVC()
clf = grid_search.GridSearchCV(svr, parameters)
clf.fit(iris.data, iris.target)
```
让我们逐行进行说明。
```
parameters = {'kernel':('linear', 'rbf'), 'C':[1, 10]}
```

参数字典以及您想尝试的可能的值。在这种情况下，他们在尝试找到内核（可能的选择为'linear'和'rbf'）和C语言（可能的选择为1和10）的最佳方案。
这时，自动生产以下（内核、C语言）组合: [('rbf', 1), ('rbf', 10), ('linear', 1), ('linear', 10)]。各组合均用于训练SVM，并使用交叉验证对性能进行评估。
```
svr = svm.SVC()
```
这与创建分类器有点类似，就如我们从第一节课一直在做的一样。但是请注意，“clf”到下一行才会生成——这儿仅仅是在说采用哪种算法。另一种思考方法 是，“分类器”在这种情况下不仅仅是一个算法，而是算法加参数值。请注意，这里不需对内核或C语言做各种尝试；下一行将处理这个问题。
 ```
clf = grid_search.GridSearchCV(svr, parameters)
````
这是第一个不可思议之处，分类器创建好了。 我们传达算法 (svr) 和参数字典来尝试 (参数) 而分类器则生成一个网格的参数组合进行尝试。
```
clf.fit(iris.data, iris.target)
```
第二个不可思议之处。 拟合函数现在尝试了所有的参数组合，并返回一个合适的分类器，自动调整至最佳参数组合。现在您便可通过clf.bestestimator.获得参数值。
5/6

# 6. 测验: sklearn 中的 GridSearchCV
请参考[此处](http://scikit-learn.org/stable/auto_examples/applications/face_recognition.html)的特征脸方法代码。使用 GridSearchCV 调整了 SVM 的哪些参数？


Give it another shot. You can find the code [here](http://scikit-learn.org/stable/auto_examples/applications/face_recognition.html)
