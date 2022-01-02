from nltk import word_tokenize
from nltk import PorterStemmer
from nltk.stem import WordNetLemmatizer


# Tokenization of tweet text
def text_tokenier(data_set):
    """
    performs word tokenization on data
    :param data_set: cleaned dataset
    :return: tokenized dataset
    """
    data_set['text'] = data_set['text'].apply(lambda x: word_tokenize(str(x)))
    return data_set


# Applying Stemming
def text_stemmer(data_set):
    """
    performs word stemming on data
    :param data_set: tokenized dataset
    :return: stemmed dataset
    """
    st = PorterStemmer()

    def stemming_on_text(data):
        text = [st.stem(word) for word in data]
        return data

    data_set['text'] = data_set['text'].apply(lambda x: stemming_on_text(x))
    return data_set


# Applying Lemmatizer
def text_lemmatizer(data_set):
    """
    performs word lemmatization on data
    :param data_set: stemmed dataset
    :return: lemmatized dataset
    """
    lm = WordNetLemmatizer()

    def lemmatizer_on_text(data):
        text = [lm.lemmatize(word) for word in data]
        return data

    data_set['text'] = data_set['text'].apply(lambda x: lemmatizer_on_text(x))
    return data_set


# All Data prep operations
def data_prep(data_set):
    """
    prepares tokenized and stemmed data for model
    :param data_set: cleaned dataset
    :return: processed data
    """
    print('')
    print('******************************************')
    print('********Data Preparation for Model********')
    print('******************************************')
    print('')
    print('Applying Tokenization')
    data_set = text_tokenier(data_set)
    print(data_set.head())
    print('')
    print('Applying Stemming')
    data_set = text_stemmer(data_set)
    print(data_set.head())
    print('')
    print('Applying Lemmatization')
    data_set = text_lemmatizer(data_set)
    print(data_set.head())
    return data_set
