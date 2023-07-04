import json
from datetime import datetime


def load_json(file):
    with open(file, 'r', encoding='UTF-8') as file_in:
        return json.load(file_in)


def mod_transactions(tr):
    mod_tr = list()
    for i in range(len(tr)):
        if tr[i].get("date") is not None:
            dt = tr[i]["date"].replace('T', ' ')
            mod_tr.append(dt)
    return mod_tr


def get_recent_transactions(file: list, quantity=5):
    tr = load_json(file)
    mod_tr = mod_transactions(tr)
    print(mod_tr)
