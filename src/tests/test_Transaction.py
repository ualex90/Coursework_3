import pytest

from src.transaction.Transaction import Transaction


def test_Transaction_init(mod_tr_fixture):
    tr = Transaction(**mod_tr_fixture[0])
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


@pytest.mark.parametrize('index', [0, 1, 2])
def test_Transaction_str(mod_tr_fixture, result_fixture, index):
    data = mod_tr_fixture[index]
    assert Transaction(**data).__str__() == result_fixture[index]
