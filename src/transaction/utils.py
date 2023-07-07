import json
from datetime import datetime


def load_json(file):
    """
    Функция чтения файла json
    :param file: путь к файлу
    :return: содержимое файла преобразованное в коллекцию python
    """
    with open(file, 'r', encoding='UTF-8') as file_in:
        return json.load(file_in)


def mod_transactions(tr):
    """
    Функция преобразует поле date в unix и
    сортирует список транзакций от ранних до поздних
    :param tr: исходный список транзакций
    :return: модифицированный список транзакций
    """
    mod_tr = list()
    for i in range(len(tr)):
        if tr[i].get("date") is not None:
            dt = tr[i]["date"]
            tr[i]["date"] = datetime.fromisoformat(dt).timestamp()
            mod_tr.append(tr[i])
    mod_tr.sort(key=lambda dict_: dict_["date"])
    return mod_tr


def get_recent_transactions(file: list, quantity=5):
    """
    Функция вызывает чтение JSON файла,
    вызывает функцию модифификации списка и
    возвращает список из последних "quantity" транзакций
    :param file: JSON файл
    :param quantity: количество последних транзакций в списке для возврата
    :return:
    """
    tr = load_json(file)
    mod_tr = mod_transactions(tr)
    return mod_tr[(quantity * -1):]
