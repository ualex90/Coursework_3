from settings import TEST_DATA
from src.transaction.utils import load_json, mod_transactions, get_recent_transactions


def test_load_json(transactions_fixture):
    assert load_json(TEST_DATA) == transactions_fixture


def test_mod_transactions(mod_tr_fixture):
    assert mod_transactions(load_json(TEST_DATA)) == mod_tr_fixture


def test_get_recent_transactions(mod_tr_fixture):
    assert get_recent_transactions(TEST_DATA, 1) == [mod_tr_fixture[-1]]
    assert get_recent_transactions(TEST_DATA, 2) == mod_tr_fixture[1:]
