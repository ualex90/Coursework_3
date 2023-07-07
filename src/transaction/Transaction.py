from datetime import datetime


class Transaction:
    """
    Класс транзакция.
    Принимает следущие данные:
    :param id_: ID перевода
    :param state: Статус перевода
    :param date: Дату совершения перевода
    :param operationAmount: Сведения о сумме и валюте
    :param description: Описание перевода
    :param from_: откуда
    :param to_: куда
    """
    def __init__(self, id_, state, date, operationAmount, description, from_, to_, ):
        self.id_ = id_
        self.state = state
        self.date = datetime.fromtimestamp(date)
        self.amount = operationAmount.get("amount")
        self.currency_name = operationAmount.get("currency").get("name")
        self.currency_code = operationAmount.get("currency").get("code")
        self.description = description
        self.from_ = from_
        self.to_ = to_

    @staticmethod
    def mask(check: str):
        """
        Метод маскирует номер счета в формате **XXXX
        и номер карты в формате XXXX XX** **** XXXX
        либо возвращает "Наличные" без маскирования
        :param check: данные в формате строки
        :return: замаскированная строка
        """
        if "Наличные" in check:
            return check
        if "Счет" in check:
            return f'Счет **{check[-4:]}'
        return f'{check[:-17]} {check[-16:-12]} {check[-11:-9]}** **** {check[-4:]}'

    def __str__(self):
        return f'''{self.date.strftime("%d.%m.%Y")} {self.description}
                 \r{self.mask(self.from_)} -> {self.mask(self.to_)}
                 \r{self.amount} {self.currency_name}'''
