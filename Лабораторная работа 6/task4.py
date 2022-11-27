import json

INPUT_FILE = "input_1.csv"
delimiter = ","

def csv_to_list_dict(filename):
    list_ = []
    with open(filename) as f:
        for line in f:
            list_.append((line.rstrip().split(delimiter)))

    list_ = [{j: i[list_[0].index(j)] for j in list_[0]} for i in list_[1:]]

    return list_

print(json.dumps(csv_to_list_dict(INPUT_FILE), indent=4))