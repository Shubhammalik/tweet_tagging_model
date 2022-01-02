import json
import pickle
from pathlib import Path
from os import listdir
from src.model_evaluation import get_model


def save_best_model(name, position, X_train, y_train):
    model = get_model(name)
    model.fit(X_train, y_train)
    # save the model to disk
    print(f'Saving the best model as ({name}) for position {position}')
    path = './model/saved_model/' + position + '/'
    filename = path + name + '.sav'
    if not Path(path).exists():
        Path(path).mkdir(parents=True, exist_ok=True)
    pickle.dump(model, open(filename, 'wb'))


def load_best_model(position):
    path = './model/saved_model/' + str(position) + '/'
    name = listdir(path)
    filename = path + name[0]
    if Path(filename).is_file():
        print(f'Loading the best model for position {position}')
        print(f'MODEL: {name[0]}')
        loaded_model = pickle.load(open(filename, 'rb'))
        return loaded_model
    else:
        print('Incorrect Location or file name')


def model_selector(position, X_train, y_train):
    path = './model/stats/'
    file = 'model_stats'
    ext = '.json'
    best = 'best'
    position = str(position)
    path_to_file = path + file + ext
    model_stats = {}
    if Path(path_to_file).is_file():
        model_stats = json.load(open(path_to_file), )
    best_model = model_stats[position][best]['model']
    save_best_model(best_model, position, X_train, y_train)


def model_run_history():
    path = './model/stats/'
    file = 'model_stats'
    ext = '.json'
    path_to_file = path + file + ext
    model_stats = {}
    if Path(path_to_file).is_file():
        model_stats = json.load(open(path_to_file), )
    print(json.dumps(model_stats, indent=4, sort_keys=True))
