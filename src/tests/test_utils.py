from settings import TEST_DATA
from src.transaction.utils import load_json


def test_load_json(transactions_fixture):
    assert load_json(TEST_DATA) == transactions_fixture
