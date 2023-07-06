import pytest


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
             'from': 'MasterCard 4321432143214321',
             'to': 'Счет 54321543215432154321'
             }
            ]
