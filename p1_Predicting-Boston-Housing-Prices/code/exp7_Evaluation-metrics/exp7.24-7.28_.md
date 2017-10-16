# 24. F1 分数
既然我们已讨论了精确率和召回率，接下来可能要考虑的另一个指标是 F1 分数。F1 分数会同时考虑精确率和召回率，以便计算新的分数。
可将 F1 分数理解为精确率和召回率的加权平均值，其中 F1 分数的最佳值为 1、最差值为 0：
```
F1 = 2 (精确率 召回率) / (精确率 + 召回率)
```
有关 F1 分数和如何在 sklearn 中使用它的更多信息，请查看此链接 [此处](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.f1_score.html#sklearn.metrics.f1_score)。

# 25. 回归指标
正如前面对问题的回归类型所做的介绍，我们处理的是根据连续数据进行预测的模型。在这里，我们更关注预测的接近程度。

例如，对于身高和体重预测，我们不是很关心模型能否将某人的体重 100% 准确地预测到小于零点几磅，但可能很关心模型如何能始终进行接近的预测（可能与个人的真实体重相差 3-4 磅）。

# 26. 平均绝对误差
您可能已回想起，在统计学中可以使用绝对误差来测量误差，以找出预测值与真实值之间的差距。平均绝对误差的计算方法是，将各个样本的绝对误差汇总， 然后根据数据点数量求出平均误差。通过将模型的所有绝对值加起来，可以避免因预测值比真实值过高或过低而抵销误差，并能获得用于评估模型的整体误差指标。

有关平均绝对误差和如何在 sklearn 中使用它的更多信息，请查看此链接 [此处](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.mean_absolute_error.html#sklearn.metrics.mean_absolute_error)。

# 27. 均方误差
均方误差是另一个经常用于测量模型性能的指标。与绝对误差相比，残差（预测值与真实值的差值）被求平方。

对残差求平方的一些好处是，自动将所有误差转换为正数、注重较大的误差而不是较小的误差以及在微积分中是可微的（可让我们找到最小值和最大值）。
有关均方误差和如何在 sklearn 中使用它的更多信息，请查看此链接 此处。

# 28. Regression Scoring Functions
In addition to error metrics, Scikit-learn contains two scoring metrics which scale generally from 0 to 1, with values of 0 being bad and 1 being perfect performance.

Though we will not be using these metrics for the project at the end of this course, they are important to be aware of. They also have the advantage of looking similar to classification metrics, with numbers closer to 1.0 being good scores.

One of these is the [R2 score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.r2_score.html#sklearn.metrics.r2_score), which computes the coefficient of determination of predictions for true values. This is the default scoring method for regression learners in scikit-learn.

The other is [the explained variance score](http://scikit-learn.org/stable/modules/generated/sklearn.metrics.explained_variance_score.html#sklearn.metrics.explained_variance_score).

While we will not treat these metrics in detail just now, one important point to remember is that the default metrics for regression are "higher is better"; that is, higher scores indicate better performance. When we use the error metrics described previously, we will need to overwrite this preference.

除了错误指标之外，Scikit-learn还包含两个评分指标，通常从0到1，其值为0，而1是完美的表现。

虽然我们不会在本课程结束时为项目使用这些指标，但重要的是要注意。 他们还具有看起来类似于分类度量的优势，数字接近1.0是好的成绩。

其中之一是R2得分，其计算真实值的预测的确定系数。 这是scikit学习中回归学习者的默认评分方法。

另一个是解释的方差分数。

虽然我们现在不会详细对待这些指标，但需要记住的一个重要的一点是，回归的默认指标是“更高更好”; 也就是说，更高的分数表示更好的表现。 当我们使用之前描述的错误度量时，我们将需要覆盖此偏好。
