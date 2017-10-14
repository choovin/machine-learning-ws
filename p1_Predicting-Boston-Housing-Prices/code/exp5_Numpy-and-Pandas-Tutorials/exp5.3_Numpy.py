# coding=utf-8

import numpy as np

numbers = [1,2,3,4,5]

# 平均数
mean = np.mean(numbers)
print("{0}".format(mean))

# 中位数
median = np.median(numbers)
print ("{0}".format(median))

# 标准差
std = np.std(numbers)
print (std)

print "exp3====="
'''
The following code is to help you play with Numpy, which is a library
that provides functions that are especially useful when you have to
work with large arrays and matrices of numeric data, like doing
matrix matrix multiplications. Also, Numpy is battle tested and
optimized so that it runs fast, much faster than if you were working
with Python lists directly.

以下代码是帮助您玩Numpy，它是一个图书馆
这提供了当你必须特别有用的功能
使用大数组和数字数据矩阵，就像做
矩阵矩阵乘法。 此外，Numpy也是经过测试的
优化，使其运行速度快，比您工作时快得多
直接使用Python列表。
'''

'''
The array object class is the foundation of Numpy, and Numpy arrays are like
lists in Python, except that every thing inside an array must be of the
same type, like int or float.
数组对象类是Numpy的基础，Numpy数组就像
列表中的Python，除了数组中的每一件事情都必须是
相同类型，如int或float。
'''
# Change False to True to see Numpy arrays in action
if False:
    array = np.array([1, 4, 5, 8], float)
    print array
    print ""
    array = np.array([[1, 2, 3], [4, 5, 6]], float)  # a 2D array/Matrix
    print array

'''
You can index, slice, and manipulate a Numpy array much like you would with a
a Python list.
'''
# Change False to True to see array indexing and slicing in action
if False:
    array = np.array([1, 4, 5, 8], float)
    print array
    print ""
    print array[1]
    print ""
    print array[:2]
    print ""
    array[1] = 5.0
    print array[1]

# [ 1.  4.  5.  8.]
#
# 4.0
#
# [ 1.  4.]
#
# 5.0

# Change False to True to see Matrix indexing and slicing in action
if True:
    two_D_array = np.array([[1, 2, 3], [4, 5, 6]], float)
    print two_D_array
    print ""
    print two_D_array[1][1]
    print ""
    print two_D_array[1, :]
    print ""
    print two_D_array[:, 2]

# [行][列] 下标0开始
# [[ 1.  2.  3.]
#  [ 4.  5.  6.]]
#
# 5.0
#
# [ 4.  5.  6.]
#
# [ 3.  6.]

'''
Here are some arithmetic operations that you can do with Numpy arrays
'''
print("这里有一些使用Numpy数组的算术运算")
# Change False to True to see Array arithmetics in action
if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([5, 2, 6], float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2
# [ 6.  4.  9.]
#
# [-4.  0. -3.]
#
# [  5.   4.  18.]

# Change False to True to see Matrix arithmetics in action
if True:
    array_1 = np.array([[1, 2], [3, 4]], float)
    array_2 = np.array([[5, 6], [7, 8]], float)
    print array_1 + array_2
    print ""
    print array_1 - array_2
    print ""
    print array_1 * array_2

# [[  6.   8.]
#  [ 10.  12.]]
#
# [[-4. -4.]
#  [-4. -4.]]
#
# [[  5.  12.]
#  [ 21.  32.]]
'''
In addition to the standard arthimetic operations, Numpy also has a range of
other mathematical operations that you can apply to Numpy arrays, such as
mean and dot product.

Both of these functions will be useful in later programming quizzes.
除了标准的游戏操作，Numpy也有一系列的
可以应用于Numpy数组的其他数学运算，如
平均值和点积。

这两个功能在后来的编程测验中将会很有用。
'''
if True:
    array_1 = np.array([1, 2, 3], float)
    array_2 = np.array([[6], [7], [8]], float)
    print np.mean(array_1)
    print np.mean(array_2)
    print ""
print np.dot(array_1, array_2)
# 2.0
# 7.0
#
# numpy乘法运算中dot是按照矩阵乘法的规则来运算的 1*6 + 2*7 + 3*8 = 44
# [ 44.]

