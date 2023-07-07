from datetime import datetime


class Transaction:
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

    def __str__(self):
        return self.id_
