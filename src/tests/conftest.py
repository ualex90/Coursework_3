import pytest

from settings import TEST_DATA
from src.transaction.Transaction import Transaction
from src.transaction.utils import get_recent_transactions


@pytest.fixture
def transactions_fixture():  # исходные тестовые данные
    return [{'id': 11111111,
             'state': 'EXECUTED',
             'date': '2023-07-07T10:00:00.111111',
             'operationAmount': {'amount': '10000.99', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации',
             'from': 'Maestro 1234123412341234',
             'to': 'Счет 12345123451234512345'
             },
            {'id': 22222222,
             'state': 'EXECUTED',
             'date': '2023-07-07T10:00:00.222222',
             'operationAmount': {'amount': '20000.33', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации',
             'from': 'Счет 54321543215432154321',
             'to': 'Счет 54321543215432154321'
             },
            {'id': 33333333,
             'state': 'EXECUTED',
             'date': '2023-07-07T10:00:00.222223',
             'operationAmount': {'amount': '20000.33', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Пополнение',
             'to': 'Счет 54321543215432154321'
             },
            {'id': 44444444,
             'state': 'CANCELED',
             'date': '2023-07-08T10:00:00.000000',
             'operationAmount': {'amount': '20000.33', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации',
             'from': 'Счет 54321543215432154321',
             'to': 'Счет 54321543215432154321'
             },
            ]


@pytest.fixture()
def mod_tr_fixture():
    return [{'id_': 11111111,
             'state': 'EXECUTED',
             'date': 1688688000.111111,
             'operationAmount': {'amount': '10000.99', 'currency': {'name': 'руб.', 'code': 'RUB'}},
             'description': 'Перевод организации',
             'from_': 'Maestro 1234123412341234',
             'to_': 'Счет 12345123451234512345'
             },
            {'id_': 22222222,
             'state': 'EXECUTED', 'date': 1688688000.222222,
             'operationAmount': {'amount': '20000.33', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Перевод организации',
             'from_': 'Счет 54321543215432154321',
             'to_': 'Счет 54321543215432154321'
             },
            {'id_': 33333333,
             'state': 'EXECUTED',
             'date': 1688688000.222223,
             'operationAmount': {'amount': '20000.33', 'currency': {'name': 'USD', 'code': 'USD'}},
             'description': 'Пополнение',
             'from_': 'Наличные',
             'to_': 'Счет 54321543215432154321'
             },
            ]


@pytest.fixture()
def result_fixture():
    return ['''07.07.2023 Перевод организации
                 \rMaestro 1234 23** **** 1234 -> Счет **2345
                 \r10000.99 руб.''',
            '''07.07.2023 Перевод организации
                 \rСчет **4321 -> Счет **4321
                 \r20000.33 USD''',
            '''07.07.2023 Пополнение
                 \rНаличные -> Счет **4321
                 \r20000.33 USD''']
