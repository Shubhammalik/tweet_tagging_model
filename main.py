from src.data_read import get_data
from src.data_stats import get_data_stats
from src.data_preparation import data_prep
from src.model_evaluation import model_train
from src.data_visualization import data_visuals
from src.data_visualization import plot_word_cloud
from src.data_transformation import TransformationClass
from src.data_operations import data_cleaning, set_position, get_preprocessed_data
from src.data_operations import save_dataset, load_saved_dataset
from src.model_selection import model_selector, load_best_model, model_run_history


def main(position, dataset_type='training', print_to_file=False, display_plots=False):
    # Getting data file

    df, data = get_data()

    # Printing data statistics
    get_data_stats(data)

    # Generating data plots EDA
    data_visuals(df, data, print_to_file, display_plots)

    position = set_position(position)

    # Preprocessing Data, dividing into training and online dataset
    dataset_processed = get_preprocessed_data(data, position, dataset_type)

    # Cleaning check on data for stopwords, urls, numbers, punctuations, and repeats
    dataset_cleaned = data_cleaning(dataset_processed)

    # Plotting negative and positive tweets word cloud
    plot_word_cloud(dataset_cleaned, position, print_to_file, display_plots)

    # Data Preparation, stemming, tokenization
    dataset_prepped = data_prep(dataset_cleaned)

    # Splitting the data into test train
    data = TransformationClass(dataset_prepped, position).data_transform()

    # Evaluating Different Models
    # All models ['bernoulli_nb', 'multinomial_nb', 'linear_svc', 'lr', 'xgboost']
    models_name = ['bernoulli_nb', 'multinomial_nb', 'linear_svc', 'lr', 'xgboost']
    for model in models_name:
        model_train(model, position, data.X_train, data.X_test, data.y_train, data.y_test, print_to_file, display_plots)

    model_selector(position, data.X_train, data.y_train)


if __name__ == '__main__':
    """
    :param position: Separates the raw data into training and online, with position*2 entries in training
    :param dataset_type: Takes parameter 'training'/'online' for data input
     online mocks online machine learning situation for continuous inflow of data
    :param print_to_file: If set true then will generate new plots for the datasets
    :param display_plots: If set true then will show plots while running src
    :return: Display final classification reports of different models
    
    """
    # KEYWORDS DEFINITIONS
    position_ = 30000
    dataset_type_ = 'training'  # OR 'online'
    print_to_file_ = False
    display_plots_ = False
    main(position_, dataset_type_, print_to_file_, display_plots_)
