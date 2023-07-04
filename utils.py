import json


def get_operations(file):
    with open(file, 'r', encoding='UTF-8') as file_in:
        return json.load(file_in)
