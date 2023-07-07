from settings import OPERATIONS
from src.transaction.Transaction import Transaction
from utils import get_recent_transactions


def main():
    # Получение списка последних 5-ти (корректно заполненных) транзакций из JSON
    recent_transactions = get_recent_transactions(OPERATIONS, quantity=5)

    # Создание списка из заданного числа объектов Transaction
    transactions_list = [Transaction(**i) for i in recent_transactions]

    # Вывод на экран информации о переводах хранящийся в объектах (__str__)
    [print(i, "\n") for i in transactions_list]


if __name__ == '__main__':
    main()
