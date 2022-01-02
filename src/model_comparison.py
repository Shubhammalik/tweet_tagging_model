import json
from pathlib import Path


def model_comparator(name, position, accuracy, time_):
    model_stats = {}
    path = './model/stats/'
    file = 'model_stats'
    ext = '.json'
    best = 'best'
    path_to_file = path + file + ext
    position = str(position)
    if not Path(path).exists():
        Path(path).mkdir(parents=True, exist_ok=True)

    updated_flag = False
    if Path(path_to_file).is_file():
        model_stats = json.load(open(path_to_file), )
        updated_flag = True

    if not updated_flag:
        print('Creating new model stats file')
        model_stats[position] = {}
        model_stats[position][name] = {}
        model_stats[position][best] = {}
        model_stats[position][name]['accuracy'] = accuracy
        model_stats[position][name]['time'] = str(time_)
        model_stats[position][best]['accuracy'] = accuracy
        model_stats[position][best]['model'] = name
    else:
        print('Updating existing model stats file')
        if position not in model_stats:
            model_stats[position] = {}
        try:
            prev_model_acc = model_stats[position][name]['accuracy']
        except KeyError:
            prev_model_acc = 0
            model_stats[position][name] = {}
        if accuracy > prev_model_acc:
            model_stats[position][name]['accuracy'] = accuracy
            model_stats[position][name]['time'] = str(time_)
            print('Model better performing than previous')
        else:
            print('Model less performing than previous')
        try:
            prev_best_acc = model_stats[position][best]['accuracy']
        except KeyError:
            prev_best_acc = 0
            model_stats[position][best] = {}
        if accuracy > prev_best_acc:
            model_stats[position][best]['accuracy'] = accuracy
            model_stats[position][best]['model'] = name
            print(f'Best model for position {position} changed to {name}')

    outfile = open(path_to_file, 'w')
    json.dump(model_stats, outfile, indent=4, sort_keys=True)
    print('file written')
    outfile.close()
