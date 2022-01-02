import sys
import os.path
import pandas as pd
import seaborn as sns
from pathlib import Path
import matplotlib.pyplot as plt
from wordcloud import WordCloud


def data_visuals(df, data, print_to_file=False, display_plots=False):
    """
    Generate initial EDA charts for data
    :param df: full dataset
    :param data: relevant dataset
    :param print_to_file: print new images if set True
    :param display_plots: display plot in IDE if set True
    :return: None
    """
    # Plotting the distribution for dataset.
    path = 'static/eda/'
    if not Path(sys.path[0] + '/' + path).exists():
        Path(sys.path[0] + '/' + path).mkdir(parents=True, exist_ok=True)
    print('')
    print('******************************************')
    print('*********Exploratory Data Analysis********')
    print('******************************************')
    print('')
    if not os.path.isfile(path + 'data_visuals.png') or print_to_file:
        print('Generating Data Distribution Graphs')
        fig, (ax1, ax2) = plt.subplots(ncols=2)
        ax = df.groupby('target').count().plot(kind='bar', title='Distribution of data', legend=True, ax=ax1)
        ax.set_xticklabels(['Negative', 'Positive'], rotation=0)

        # Plotting the distribution for target variable
        sns.countplot(x='target', data=data, ax=ax2).set(title='Target Distribution')
        fig.set_size_inches(10, 5)
        fig.savefig(path + 'data_visuals.png', dpi=100)
        if display_plots:
            plt.show()
    else:
        print('EDA statistics already saved in static, pass command print_to_file=True')


def plot_word_cloud(data, position, print_to_file=False, display_plots=False):
    """
    Plot word cloud for negative and positive tweets, only for the chose sample for training
    Create sub-folders if doesn't exists and avoid printing if the file is already present
    :param position: separates the raw data into training and online, with position*2 entries in training
    :param data: relevant dataset
    :param print_to_file: print new images if set True
    :param display_plots: display plot in IDE if set True
    :return: None
    """
    file_extension = '_' + str(position) + '.png'
    path = 'static/wc/' + str(position) + '/'
    if not Path(sys.path[0] + '/' + path).exists():
        Path(sys.path[0] + '/' + path).mkdir(parents=True, exist_ok=True)
    print('')
    print('******************************************')
    print('***********Generating Word Cloud**********')
    print('******************************************')
    print('')
    if not os.path.isfile(path + 'negative_wc' + file_extension) \
            or not os.path.isfile(path + 'positive_wc' + file_extension) or print_to_file:
        pd.options.display.max_colwidth = 100
        data_pos_all = data[data['target'] == 1]
        data_neg_all = data[data['target'] == 0]
        # For Negative Tweets
        print(f'Plotting negative tweets word cloud from {position} entries')
        data_neg = data_neg_all['text'].iloc[:int(position)]
        plt.figure(figsize=(20, 20))
        wc1 = WordCloud(max_words=1000, width=1600, height=800,
                        collocations=False).generate(" ".join(data_neg))
        image1 = wc1.to_image()
        wc1.to_file(path + 'negative_wc' + file_extension)
        if display_plots:
            image1.show()

        # For Positive Tweets
        print(f'Plotting positive tweets word cloud from {position} entries')
        data_pos = data_pos_all['text'].iloc[:int(position)]
        wc2 = WordCloud(max_words=1000, width=1600, height=800,
                        collocations=False).generate(" ".join(data_pos))
        plt.figure(figsize=(20, 20))
        image2 = wc2.to_image()
        wc2.to_file(path + 'positive_wc' + file_extension)
        if display_plots:
            image2.show()
        plt.clf()
    else:
        print('Word Cloud already saved in static, pass command print_to_file=True')
