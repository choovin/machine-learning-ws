# 误差原因
既然我们已讨论了一些用于测量模型性能的基本指标，现在来关注一下模型起初为何会出现误差。
在模型预测中，模型可能出现的误差来自两个主要来源，即：因模型无法表示基本数据的复杂度而造成的偏差，或者因模型对训练它所用的有限数据过度敏感而造成的方差。我们会对两者进行更详细一些的探讨。

# 偏差造成的误差 - 精度和欠拟合
如前所述，如果模型具有足够的数据，但因不够复杂而无法捕捉基本关系，则会出现偏差。这样一来，模型一直会系统地错误表示数据，从而导致预测精度低。这种现象叫做欠拟合。
简单来说，如果模型不适当，则会出现偏差。举例而言：对象是按颜色和形状分类的，但模型只能按颜色来区分对象和将对象分类（这是过度简化的模型），因而一直会错误地表示未来的对象。
或者，我们可能有本质上是多项式的连续数据，但模型只能表示线性关系。在此情况下，我们向模型提供多少数据并不重要，因为模型根本无法表示需要更复杂的模型来表示的基本关系。

# 方差造成的误差 - 精度和过拟合
在训练模型时，通常使用来自较大母体（训练集）的有限数量样本。如果利用随机选择的数据子集反复训练模型，可以预料它的预测结果会因提供给它的具体样本而异。在这里，方差用来测量预测结果对于任何给定的测试样本会出现多大的变化。
出现方差是正常的，但方差过高表明模型无法将其预测结果泛化到从中抽取训练样本的较大母体。对训练集高度敏感也称为过拟合，而且通常出现在模型过于复杂和/或我们没有足够的数据支持它时。
通常，可以利用更多数据进行训练，以降低模型预测结果的变化性和提高精度。

# 改进模型的有效性
我们可以看到，在给定一组固定数据时，模型不能过于简单或复杂。如果过于简单，模型无法了解数据并会错误地表示数据。但是，如果建立非常复杂的模型，则需要更多数据才能了解基本关系，否则十分常见的是，模型会推断出在数据中实际上可能不存在的关系。
关键在于，通过找出正确的模型复杂度来找到最大限度降低偏差和方差的最有效点。当然，数据越多，模型随着时间推移会变得越好。
要详细了解偏差和方差，建议阅读 Scott Fortmann-Roe 撰写的 [此文章](http://scott.fortmann-roe.com/docs/BiasVariance.html)。
除了选定用来训练模型的数据子集外，您使用的哪些来自给定数据集的特征也会显著影响模型的偏差和方差？
