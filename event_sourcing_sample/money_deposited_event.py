from domain.event import Event


class MoneyDeposited(Event):
    def __init__(self, account_id, amount):
        self.account_id = account_id
        self.amount = amount
