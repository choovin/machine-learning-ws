# Pandas 向量化方法
来复习一下 lambda 函数。lambda 函数是在 Python 中即时定义的小型内联函数。 lambda x: x>= 1 将获取输入 x 并返回 x>=1，或者返回一个等于 True 或 False 的布尔值。
在此例中，map() 和 applymap() 通过向每个元素应用 lambda 函数来新建一个序列或数据框。请注意，只能在序列上使用 map() 来返回新序列，并且只能在数据框上使用 applymap() 来返回新数据框。

有关更多参考，请参考官方的 lambda 文档：
[Lambda Function](https://docs.python.org/2/tutorial/controlflow.html#lambda-expressions)
