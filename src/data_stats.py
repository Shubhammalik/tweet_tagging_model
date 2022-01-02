import numpy as np


def get_data_stats(df):
    """
    Generate statistics about data
    :param df: Taken full dataset as input
    :return: None
    """
    print('')
    print('******************************************')
    print('*********Printing Data Statistics*********')
    print('******************************************')
    print('')
    print('Data Shape')
    print(df.shape)
    print('All Columns')
    print(df.columns)
    print('Data Types')
    print(df.dtypes)
    print('Check unique Target Values')
    print(df['target'].nunique())
    print(df['target'].unique())
    print('Checking for Null values')
    print(np.sum(df.isnull().any(axis=1)))

