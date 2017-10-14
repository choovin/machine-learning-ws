# pandas数据结构简介

2013年10月26日|标签：python pandas sql教程数据科学

>*NOTE* :更新：如果您有兴趣从SQL角度学习pandas，并希望观看视频，您可以在这里找到我的2014年PyData NYC讲座的视频[link](http://reda.io/sql2pandas)。

一会儿，我声称我要写几篇关于将pandas翻译成SQL的帖子。我从来没有跟进。不过，另外一周，几位同事表示有兴趣了解更多信息 - 这似乎是重新审视这个话题的好理由。

以下是对图书馆的相当全面的介绍。我选择把它分成三部分，因为我觉得它太长而令人生畏。

* 第1部分：pandas数据结构简介，涵盖了库的两个主要数据结构的基础 - 系列和数据框架。

* 第2部分：使用DataFrames，深入了解DataFrames的功能。它显示如何检查，选择，过滤，合并，组合和分组数据。

* 第3部分：使用pandas与MovieLens数据集，应用前两部分的学习，以回答有关MovieLens评级数据的一些基本分析问题。

如果您想跟随，您可以在[这里](http://files.grouplens.org/datasets/movielens/ml-100k.zip)找到必要的CSV文件和MovieLens数据集。

本教程的目标是通过比较和对比其语法与SQL来教授pandas的基础知识。由于我所有的同事都熟悉SQL，所以我觉得这是提供一个可以容易地被目标受众理解的环境的最佳方法。

如果您有兴趣了解更多关于图书馆的信息，pandas作家威斯·麦金尼（Wes McKinney）编写了数据分析Python，其内容更为详细。

## 它是什么？
pandas是用于数据分析的开源Python库。 Python一直非常适合准备和打印数据，但是从来不是很好的分析 - 通常最终会使用R或将其加载到数据库中，并使用SQL（或更糟的是Excel）。pandas让Python非常适合分析。

## 数据结构
pandas向Python - Series和DataFrame引入了两个新的数据结构，它们都建立在NumPy之上（这意味着它很快）。

```
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
pd.set_option('max_columns', 50)
%matplotlib inline
```
## 系列
A系列是与表中的数组，列表或列类似的一维对象。它将为系列中的每个项目分配一个标记的索引。默认情况下，每个项目将从0到N接收索引标签，其中N是系列的长度减1。

```
# create a Series with an arbitrary list
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'])
s
0                7
1       Heisenberg
2             3.14
3      -1789710578
4    Happy Eating!
dtype: object
```
或者，您可以指定创建系列时要使用的索引。

```
s = pd.Series([7, 'Heisenberg', 3.14, -1789710578, 'Happy Eating!'],
              index=['A', 'Z', 'C', 'Y', 'E'])
s
A                7
Z       Heisenberg
C             3.14
Y      -1789710578
E    Happy Eating!
dtype: object
```
系列构造函数也可以使用词典的键作为索引来转换词汇。

```
d = {'Chicago': 1000, 'New York': 1300, 'Portland': 900, 'San Francisco': 1100,
     'Austin': 450, 'Boston': None}
cities = pd.Series(d)
cities
Austin            450
Boston            NaN
Chicago          1000
New York         1300
Portland          900
San Francisco    1100
dtype: float64
```
您可以使用索引从系列中选择特定的项目...

```
cities['Chicago']
1000.0
cities[['Chicago', 'Portland', 'San Francisco']]
Chicago          1000
Portland          900
San Francisco    1100
dtype: float64
```
或者您可以使用布尔索引进行选择。

```
cities[cities < 1000]
Austin      450
Portland    900
dtype: float64
```
最后一个可能有点奇怪，所以让我们来更clear - cities < 1000返回一系列真/假值，然后我们传递给我们的系列城市，返回相应的True项。

```
less_than_1000 = cities < 1000
print(less_than_1000)
print('\n')
print(cities[less_than_1000])
Austin            True
Boston           False
Chicago          False
New York         False
Portland          True
San Francisco    False
dtype: bool


Austin      450
Portland    900
dtype: float64
```


您还可以即时更改系列中的值。

```
# changing based on the index
print('Old value:', cities['Chicago'])
cities['Chicago'] = 1400
print('New value:', cities['Chicago'])
('Old value:', 1000.0)
('New value:', 1400.0)
# changing values using boolean logic
print(cities[cities < 1000])
print('\n')
cities[cities < 1000] = 750

print cities[cities < 1000]
Austin      450
Portland    900
dtype: float64


Austin      750
Portland    750
dtype: float64
```
如果您不确定一个项目是否在系列中怎么办？你可以使用惯用的Python来检查。

