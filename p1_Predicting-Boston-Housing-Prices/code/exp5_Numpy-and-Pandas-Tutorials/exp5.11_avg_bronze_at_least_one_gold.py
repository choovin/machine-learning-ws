# coding=utf-8

from pandas import DataFrame, Series
import numpy


def avg_medal_count():
    '''
    您可能发现使用“boolean indexing(http://pandas.pydata.org/pandas-docs/stable/indexing.html#boolean-indexing)”对解决此问题有帮助。
    这里是 Pandas 文档的链接](http://pandas.pydata.org/pandas-docs/stable/)。
    这里还有一系列优秀的 IPython Notebook 教程](https://bitbucket.org/hrojas/learn-pandas)
    感谢 Dominique Luna (http://forums.udacity.com/users/100008880/dominique-luna#ud359)分享！）


    Compute the average number of bronze medals earned by countries who
    earned at least one gold medal.
    计算获得至少一枚金牌的国家所得的铜牌的平均数

    Save this to a variable named avg_bronze_at_least_one_gold. You do not
    need to call the function in your code when running it in the browser -
    the grader will do that automatically when you submit or test it.

    HINT-1:
    You can retrieve all of the values of a Pandas column from a
    data frame, "df", as follows:
    df['column_name']

    HINT-2:
    The numpy.mean function can accept as an argument a single
    Pandas column.

    For example, numpy.mean(df["col_name"]) would return the
    mean of the values located in "col_name" of a dataframe df.
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

    olympic_medal_counts = {'country_name':Series(countries),
                            'gold': Series(gold),
                            'silver': Series(silver),
                            'bronze': Series(bronze)}
    df = DataFrame(olympic_medal_counts)

    # 先找出有金牌的国家的dataframe 再求平均数
    at_least_one_gold_count_df = df[(df.gold) >= 1 ]
    print "at_least_one_gold_count"
    print at_least_one_gold_count_df
    avg_bronze_at_least_one_gold = numpy.mean(at_least_one_gold_count_df['bronze'])

    # YOUR CODE HERE
    # bronze_at_least_one_gold =df['bronze'][df['gold'] >= 1]
    # print bronze_at_least_one_gold
    # avg_bronze_at_least_one_gold = numpy.mean(bronze_at_least_one_gold)

    print avg_bronze_at_least_one_gold
    return avg_bronze_at_least_one_gold

avg_medal_count()