from settings import OPERATIONS
from utils import get_recent_transactions


def main():
    recent_transactions = get_recent_transactions(OPERATIONS)
    print(recent_transactions)


if __name__ == '__main__':
    main()
