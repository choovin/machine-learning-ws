#!/usr/bin/env python
# -*- coding: utf-8 -*-

# 测验: 奥林匹克奖牌分数
# 这里是 Pandas 文档的链接。(http://pandas.pydata.org/pandas-docs/stable/)
# 这里还有一系列优秀的 IPython Notebook 教程 (https://bitbucket.org/hrojas/learn-pandas)
# （感谢 Dominique Luna 分享！）
# 只使用 pandas 的替代方案：
# df['points'] = df[['gold','silver','bronze']].dot([4, 2, 1])
# olympic_points_df = df[['country_name','points']]
# 这里是 Pandas 文档的链接。
# 这里还有一系列优秀的 IPython Notebook 教程
# （感谢 Dominique Luna 分享！）
#
# 有问题？ 请访问 优达学城论坛(https://discussions.youdaxue.com/c/nd009-model-evaluation-validation) 参与大家的讨论吧

import numpy
from pandas import DataFrame, Series


def numpy_dot():
    '''
    Imagine a point system in which each country is awarded 4 points for each
    gold medal,  2 points for each silver medal, and one point for each
    bronze medal.

    Using the numpy.dot function, create a new dataframe called
    'olympic_points_df' that includes:
        a) a column called 'country_name' with the country name
        b) a column called 'points' with the total number of points the country
           earned at the Sochi olympics.

    You do not need to call the function in your code when running it in the
    browser - the grader will do that automatically when you submit or test it.
    '''

    countries = ['Russian Fed.', 'Norway', 'Canada', 'United States',
                 'Netherlands', 'Germany', 'Switzerland', 'Belarus',
                 'Austria', 'France', 'Poland', 'China', 'Korea',
                 'Sweden', 'Czech Republic', 'Slovenia', 'Japan',
                 'Finland', 'Great Britain', 'Ukraine', 'Slovakia',
                 'Italy', 'Latvia', 'Australia', 'Croatia', 'Kazakhstan']

    gold = [13, 11, 10, 9, 8, 8, 6, 5, 4, 4, 4, 3, 3, 2, 2, 2, 1, 1, 1, 1, 1, 0, 0, 0, 0, 0]
    silver = [11, 5, 10, 7, 7, 6, 3, 0, 8, 4, 1, 4, 3, 7, 4, 2, 4, 3, 1, 0, 0, 2, 2, 2, 1, 0]
    bronze = [9, 10, 5, 12, 9, 5, 2, 1, 5, 7, 1, 2, 2, 6, 2, 4, 3, 1, 2, 1, 0, 6, 2, 1, 0, 1]

    print 'olympic_medal_counts'
    olympic_medal_counts = {'country_name': Series(countries), 'gold': Series(gold), 'silver': Series(silver), 'bronze': Series(bronze)}

    # print olympic_medal_counts
    # YOUR CODE HERE
    print 'olympic_medal_counts_df'
    olympic_medal_counts_df = DataFrame(olympic_medal_counts)
    print olympic_medal_counts_df

    print 'medal_counts'
    medal_counts = olympic_medal_counts_df[['gold', 'silver', 'bronze']]
    print medal_counts
    points = numpy.dot(medal_counts, [4, 2, 1])
    print points

    olympic_points =  {'country_name': Series(countries), 'points': Series(points)}
    #olympic_points_df = numpy.dot(countries, olypmic_countries_points)
    olympic_points_df = DataFrame(olympic_points)
    return olympic_points_df

if __name__ == '__main__':
    #app.run()
    print 'finish'
    print numpy_dot()
