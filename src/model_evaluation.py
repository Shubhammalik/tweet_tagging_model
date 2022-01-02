import os
import sys
import json
import numpy as np
import seaborn as sns
from pathlib import Path
from datetime import datetime
import matplotlib.pyplot as plt
# sklearn
from sklearn.svm import LinearSVC
from sklearn.metrics import roc_curve, auc
from sklearn.naive_bayes import BernoulliNB, MultinomialNB
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix, classification_report
from xgboost import XGBClassifier
from src.model_comparison import model_comparator


def model_evaluate(model, name, position, X_test, y_test, print_to_file, display_plots):
    """
    Runs the model on test data, and generate classification reports and confusion matrix
    :param model: Classification model
    :param name: name of model
    :param position: Separates the raw data into training and online, with position*2 entries in training
    :param X_test: actual text values of the sample
    :param y_test: actual target values of the sample
    :param print_to_file: print new images if set True
    :param display_plots: display plot in IDE if set True
    :return: None
    """
    path = 'static/model_eval/' + str(position) + '/'
    file_name = name + '_cf_' + str(position) + '.png'
    if not Path(sys.path[0] + '/' + path).exists():
        Path(sys.path[0] + '/' + path).mkdir(parents=True, exist_ok=True)

    print(f'EVALUATING MODEL: {name}')
    # Predict values for Test dataset
    y_pred = model.predict(X_test)
    # Print the evaluation metrics for the dataset.
    report = classification_report(y_test, y_pred, output_dict=True)
    accuracy = report['accuracy']
    print(classification_report(y_test, y_pred))
    print(f'Generating Confusion Matrix for Model: {name}')
    if not os.path.isfile(path + file_name) or print_to_file:
        # Compute and plot the Confusion matrix
        # Start a new plot else seaborn plots multiple figures on top of one another
        plt.figure()
        cf_matrix = confusion_matrix(y_test, y_pred)
        categories = ['Negative', 'Positive']
        group_names = ['True Neg', 'False Pos', 'False Neg', 'True Pos']
        group_percentages = ['{0:.2%}'.format(value) for value in cf_matrix.flatten() / np.sum(cf_matrix)]
        labels = [f'{v1}n{v2}' for v1, v2 in zip(group_names, group_percentages)]
        labels = np.asarray(labels).reshape(2, 2)
        sns.heatmap(cf_matrix, annot=labels, cmap='Blues', fmt='',
                    xticklabels=categories, yticklabels=categories)
        plt.xlabel("Predicted values", fontdict={'size': 14}, labelpad=10)
        plt.ylabel("Actual values", fontdict={'size': 14}, labelpad=10)
        plt.title("Confusion Matrix", fontdict={'size': 18}, pad=20)
        plt.savefig(path + file_name, bbox_inches='tight')
        if display_plots:
            plt.show()
    else:
        print('Confusion matrix already saved in static, pass command print_to_file=True')

    return y_pred, accuracy


def plot_roc(name, position, y_test, y_pred, print_to_file, display_plots):
    """
    Plots and save roc curve for the given model
    :param name: name of model
    :param position: Separates the raw data into training and online, with position*2 entries in training
    :param y_test: actual target values of the sample
    :param y_pred: predicted target values of the sample
    :param print_to_file: print new images if set True
    :param display_plots: display plot in IDE if set True
    :return: None
    """
    path = 'static/model_eval/' + str(position) + '/'
    file_name = name + '_roc_' + str(position) + '.png'
    print(f'Generating ROC curve for Model: {name}')
    if not os.path.isfile(path + file_name) or print_to_file:
        fpr, tpr, thresholds = roc_curve(y_test, y_pred)
        roc_auc = auc(fpr, tpr)
        plt.figure()
        plt.plot(fpr, tpr, color='darkorange', lw=1, label='ROC curve (area = %0.2f)' % roc_auc)
        plt.xlim([0.0, 1.0])
        plt.ylim([0.0, 1.05])
        plt.xlabel('False Positive Rate')
        plt.ylabel('True Positive Rate')
        plt.title('ROC CURVE')
        plt.legend(loc="lower right")
        plt.savefig(path + file_name, bbox_inches='tight')
        if display_plots:
            plt.show()
    else:
        print('ROC curve already saved in static, pass command print_to_file=True')
    print('')


def get_model(name):
    if name == 'bernoulli_nb':
        print(f'Selecting model: Bernaulli Naive Bayes')
        model = BernoulliNB()
        return model
    elif name == 'multinomial_nb':
        print(f'Selecting model: Multinomial Naive Bayes')
        model = MultinomialNB()
        return model
    elif name == 'linear_svc':
        print(f'Selecting model: Linear SVC')
        model = LogisticRegression(C=2, max_iter=1000, n_jobs=-1)
        return model
    elif name == 'lr':
        print(f'Selecting model: Logistic Regression')
        model = LogisticRegression(C=2, max_iter=1000, n_jobs=-1)
        return model
    elif name == 'xgboost':
        print(f'Selecting model: XG Boost')
        model = XGBClassifier(max_depth=6, n_estimators=1000, use_label_encoder=False, eval_metric='logloss')
        return model
    else:
        print(f'Unmatched model type, Logistic model selected as default')
        model = LogisticRegression(C=2, max_iter=1000, n_jobs=-1)
        return model


def model_train(name, position, X_train, X_test, y_train, y_test, print_to_file=False, display_plots=False):
    """
     Fits the selected model on training data and plots its reports and checks accuracy
    """
    model = get_model(name)
    model.fit(X_train, y_train)
    y_pred, accuracy = model_evaluate(model, name, position, X_test, y_test, print_to_file, display_plots)
    time_ = datetime.now()
    model_comparator(name, position, accuracy, time_)
    plot_roc(name, position, y_test, y_pred, print_to_file, display_plots)
