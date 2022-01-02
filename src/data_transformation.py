from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer


def transformation_function(data_set, position):
    """
    Transform tokenized and stemmed data into train and test
    :param data_set: processed data
    :param position: Separates the raw data into training and online, with position*2 entries in training
    :return: Series objects for train and test
    """
    print('')
    print('******************************************')
    print('************Data Transformation***********')
    print('******************************************')
    print('')
    X = data_set.text.astype(str)
    y = data_set.target

    # Separating the 95% data for training data and 5% for testing data
    print('Creating Test Train Split of Data')
    random_state = int(0.005 * position)
    print(f'Random State: {random_state}')
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.05, random_state=random_state)

    print('Converting into TF-IDF vectorization')
    vectoriser = TfidfVectorizer(ngram_range=(1, 2), max_features=500000)
    vectoriser.fit(X_train)
    print('No. of feature_words: ', len(vectoriser.get_feature_names_out()))
    X_train = vectoriser.transform(X_train)
    X_test = vectoriser.transform(X_test)
    print('')
    print('******************************************')
    print('**************Model Evaluation************')
    print('******************************************')
    print('')
    return X_train, X_test, y_train, y_test


class ConversionClass:
    def __init__(self, X_train, X_test, y_train, y_test):
        self.X_train = X_train
        self.X_test = X_test
        self.y_train = y_train
        self.y_test = y_test


class TransformationClass(ConversionClass):
    def __init__(self, dataset, position):
        self.dataset = dataset
        self.position = position

    def data_transform(self):
        X_train, X_test, y_train, y_test = transformation_function(self.dataset, self.position)
        data = ConversionClass(X_train, X_test, y_train, y_test)
        return data
