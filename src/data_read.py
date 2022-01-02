import sys
import os.path
import pandas as pd
from pathlib import Path


def get_data():
    """
    The src fetches data file from the system and trim it for relevant data
    :return: Returns full dataset as df and trimmed dataset data with only relevant data features
    """
    # Importing the dataset
    # https://www.kaggle.com/paoloripamonti/twitter-sentiment-analysis/data
    file_name = 'twitter'
    path = 'data/raw/'
    DATASET_COLUMNS = ['target', 'ids', 'date', 'flag', 'user', 'text']
    DATASET_ENCODING = "ISO-8859-1"
    # Specifying column ids as index
    file_name = file_name + '.csv'

    try:
        df = pd.read_csv(path + file_name, encoding=DATASET_ENCODING, names=DATASET_COLUMNS)
    except FileNotFoundError as e:
        print(f'Data File Not Found Error: {e}')
        sys.exit(1)

    # Print sample
    print('')
    print('******************************************')
    print('**************Raw Data Sample*************')
    print('******************************************')
    print('')
    print(df.sample(5))

    if not Path(sys.path[0] + '/' + path).exists():
        Path(sys.path[0] + '/' + path).mkdir(parents=True, exist_ok=True)

    if not os.path.isfile(path + 'data.csv'):
        # Selecting text and target only
        data = df.loc[:, ['text', 'target']]
        # OR
        # data=df[['text','target']] # Gives the warning for using .loc

        # Replacing target value 4 with 1 for positive
        data['target'] = data['target'].replace(4, 1)
        data.to_csv(path + 'data.csv', encoding=DATASET_ENCODING, index=False)
        # Checking update
        print('')
        print('Extracting only required data')
        print('Replacing target 4 with 1 and checking')
        print(data['target'].unique())
    else:
        data = pd.read_csv(path + 'data.csv', encoding=DATASET_ENCODING)

    return df, data
