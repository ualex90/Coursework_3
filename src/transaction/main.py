from settings import OPERATIONS
from src.transaction.Transaction import Transaction
from utils import get_recent_transactions


def main():
    recent_transactions = get_recent_transactions(OPERATIONS)
    transactions_list = [Transaction(**i) for i in recent_transactions]
    [print(i, "\n") for i in transactions_list]


if __name__ == '__main__':
    main()
