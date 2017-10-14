# encoding: utf-8
'''

@author: choovin

@license: (C) Copyright 2013-2017, Node Supply Chain Manager Corporation Limited.

@contact: choovin@gmail.com

@software: garner

@file: ${NAME}.py

@time: ${DATE} ${TIME}

@desc:

'''



import numpy as np
import pandas as pd

# RMS Titanic data visualization code
from titanic_visualizations import survival_stats
from IPython.display import display

%matplotlib inline

# Load the dataset
in_file = 'titanic_data.csv'
full_data = pd.read_csv(in_file)

# Print the first few entries of the RMS Titanic data
display(full_data.head())


# Store the 'Survived' feature in a new variable and remove it from the dataset
outcomes = full_data['Survived']
data = full_data.drop('Survived', axis = 1)

# Show the new dataset with 'Survived' removed
display(data.head())


def accuracy_score(truth, pred):
    """ Returns accuracy score for input truth and predictions. 返回输入真值和预测的准确性分数。 """

    # Ensure that the number of predictions matches number of outcomes
    # 确保预测数与结果数的长度相匹配

    if len(truth) == len(pred):

        # Calculate and return the accuracy as a percent
        return "Predictions have an accuracy of {:.2f}%.".format((truth == pred).mean()*100)

    else:
        return "Number of predictions does not match number of outcomes!"

# Test the 'accuracy_score' function
predictions = pd.Series(np.ones(5, dtype = int))
print accuracy_score(outcomes[:5], predictions)


