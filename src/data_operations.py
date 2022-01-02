import re
import sys
import string
import os.path
import pandas as pd
from pathlib import Path
from nltk.corpus import stopwords

"""
# To display max width of data in column
pd.options.display.max_colwidth = 500
pd.options.display.max_rows = 100
"""


def set_position(position=20000):
    """

    :param position: separates the raw data into training and online, with position*2 entries in training
    :return: validated position
    """
    if position <= 10 or position >= 800001:
        print('position is out of range, assigning default value 20000')
        position = 20000
    return position


def get_preprocessed_data(data, position, dataset_type='training'):
    """
    Divide the dataset into training and online based on position
    :param data: relevant dataset
    :param position: separates the raw data into training and online, with position*2 entries in training
    :param dataset_type: takes input training/online to return the respective dataset
    :return: processed dataset based on dataset_type input
    """
    DATASET_ENCODING = 'ISO-8859-1'
    path = 'data/' + str(position) + '/'
    file_extension = '_' + str(position) + '.csv'
    print('')
    print('******************************************')
    print('************Data Pre-Processing***********')
    print('******************************************')
    print('')
    print('Processing data into training and online')
    print(f'Training data has {position * 2} entries')
    if not os.path.isfile(path + 'twitter_training' + file_extension) \
            or not os.path.isfile(path + 'twitter_online' + file_extension):

        # Separating positive and negative tweets
        data_pos_all = data[data['target'] == 1]
        data_neg_all = data[data['target'] == 0]
        print('Separating positive and negative sentiments')
        print('Shape of positive before')
        print(data_pos_all.shape)
        print('Shape of negative before')
        print(data_neg_all.shape)

        # Taking only a small fraction to train initial model (say 1/80th of each, total 5%)
        data_pos = data_pos_all.iloc[:int(position)]
        data_neg = data_neg_all.iloc[:int(position)]
        print('')
        print('Shape of positive after')
        print(data_pos.shape)
        print('Shape of negative after')
        print(data_neg.shape)

        # Remaining data kept for online learning (95%)
        data_pos_rem = data_pos_all.iloc[int(position):]
        data_neg_rem = data_neg_all.iloc[int(position):]
        print('')
        print('Shape of remaining positive for online dataset')
        print(data_pos_rem.shape)
        print('Shape of remaining negative for online dataset')
        print(data_neg_rem.shape)

        # Combining positive and negative tweet datasets
        dataset = pd.concat([data_pos, data_neg])
        dataset_rem = pd.concat([data_pos_rem, data_neg_rem])

        # Making text in lower case
        dataset['text'] = dataset['text'].str.lower()
        dataset_rem['text'] = dataset_rem['text'].str.lower()

        # Saving dataframe as csv
        if not Path(sys.path[0] + '/' + path).exists():
            Path(sys.path[0] + '/' + path).mkdir(parents=True, exist_ok=True)

        print('Saving generated data files')
        dataset.to_csv(path + 'twitter_training' + file_extension, encoding=DATASET_ENCODING, index=False)
        dataset_rem.to_csv(path + 'twitter_online' + file_extension, encoding=DATASET_ENCODING, index=False)

    else:
        print('Files with the given split already present, reading existing data')
        dataset = pd.read_csv(path + 'twitter_training' + file_extension, encoding=DATASET_ENCODING)
        dataset_rem = pd.read_csv(path + 'twitter_online' + file_extension, encoding=DATASET_ENCODING)

    print('')
    print('Training Dataset shape')
    print(dataset.shape)
    print('Remaining Online Dataset shape')
    print(dataset_rem.shape)

    t = dataset_type.lower()
    if t == 'training':
        return dataset
    else:
        return dataset_rem


def get_stopwords():
    stopwordlist = ['shes', 'shouldve', 'youve', 'iam', 'youre', 'thatll', 'youd', 'hi', 'ya',
                    'im', 'youll', 'u', 'i\'m', 'aw', 'he\'s', 'i\'ll', 'i\'ve', 'it\'ll', 'us', 'she\'s', 'r',
                    'twitter', 'yall', 'thats', 'havent', 'st', 'one', 'two', 'three', 'first', 'second', 'third']
    return stopwordlist


# Cleaning and removing stop words
def clean_stopwords(data_set):
    """
    removes stopwords from the dataset
    :param data_set: relevant dataset
    :return: cleaned dataset
    """
    stop = stopwords.words('english')
    stop_words = get_stopwords()
    stop_words.extend(stop)
    stop_words = list(set(stop_words))

    def cleaning_stopwords(text):
        return " ".join([word for word in str(text).split() if word not in stop_words])

    data_set['text'] = data_set['text'].apply(lambda text: cleaning_stopwords(text))
    return data_set


# Removing punctuations
def remove_punctuations(data_set):
    """
    removes punctuations from the dataset
    :param data_set: relevant dataset
    :return: cleaned dataset
    """
    punctuations_list = string.punctuation

    #    punctuations_list = english_punctuations
    def cleaning_punctuations(text):
        translator = str.maketrans('', '', punctuations_list)
        return text.translate(translator)

    data_set['text'] = data_set['text'].apply(lambda x: cleaning_punctuations(x))
    return data_set


# Removing repeated words
def remove_repeating(data_set):
    """
    removes repeating characters from the dataset
    :param data_set: relevant dataset
    :return: cleaned dataset
    """

    def cleaning_repeating_char(text):
        return re.sub(r'(.)1+', r'1', text)

    data_set['text'] = data_set['text'].apply(lambda x: cleaning_repeating_char(x))
    return data_set


# Removing URLs
def removing_url(data_set):
    """
    removes urls from the dataset
    :param data_set: relevant dataset
    :return: cleaned dataset
    """

    def cleaning_urls(data):
        return re.sub('((www.[^s]+)|(https?://[^s]+))', ' ', data)

    data_set['text'] = data_set['text'].apply(lambda x: cleaning_urls(x))
    return data_set


# Removing numbers from text
def removing_numbers(data_set):
    """
    removes numbers from the dataset
    :param data_set: relevant dataset
    :return: cleaned dataset
    """

    def cleaning_numbers(data):
        return re.sub('[0-9]+', '', data)

    data_set['text'] = data_set['text'].apply(lambda x: cleaning_numbers(x))
    return data_set


# All cleaning operations
def data_cleaning(data_set):
    """
    performs all cleaning operation on data
    :param data_set: pre-processed dataset
    :return: cleaned dataset
    """
    pd.options.display.max_colwidth = 100
    print('')
    print('******************************************')
    print('*************Dataset Cleaning*************')
    print('******************************************')
    print('')
    print('Dataset before Cleaning')
    print(data_set.tail())
    print('')
    print('Removing punctuations')
    data_set = remove_punctuations(data_set)
    print(data_set.tail())
    print('')
    print('Removing Numbers')
    data_set = removing_numbers(data_set)
    print(data_set.tail())
    print('')
    print('Removing stopwords')
    data_set = clean_stopwords(data_set)
    print(data_set.tail())
    print('')
    print('Removing repeat words')
    data_set = remove_repeating(data_set)
    print(data_set.tail())
    print('')
    print('Removing URLs')
    data_set = removing_url(data_set)
    print(data_set.tail())
    return data_set


def save_dataset(dataset, name):
    DATASET_ENCODING = 'ISO-8859-1'
    path = 'data/cache/'
    if not Path(sys.path[0] + '/' + path).exists():
        Path(sys.path[0] + '/' + path).mkdir(parents=True, exist_ok=True)
    path = path + name + '.csv'
    dataset.to_csv(path, encoding=DATASET_ENCODING, index=False)


def load_saved_dataset(name):
    DATASET_ENCODING = 'ISO-8859-1'
    path = 'data/cache/' + name + '.csv'
    dataset = pd.read_csv(path, encoding=DATASET_ENCODING)
    return dataset
