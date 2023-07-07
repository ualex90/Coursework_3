from settings import TEST_DATA
from src.transaction.Transaction import Transaction
from src.transaction.utils import get_recent_transactions


def test_Transaction_init():
    data = get_recent_transactions(TEST_DATA)[0]
    tr = Transaction(**data)
    assert tr.id_ == 11111111
    assert tr.state == 'EXECUTED'
    assert str(tr.date) == '2023-07-07 10:00:00.111111'
    assert tr.currency_name == 'руб.'
    assert tr.amount == '10000.99'
    assert tr.currency_name == 'руб.'
    assert tr.currency_code == 'RUB'
    assert tr.description == 'Перевод организации'
    assert tr.from_ == 'Maestro 1234123412341234'
    assert tr.to_ == 'Счет 12345123451234512345'
