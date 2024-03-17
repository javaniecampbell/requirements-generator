from domain.event import Event


class MoneyWithdrawn(Event):
    def __init__(self, account_id, amount):
        self.account_id = account_id
        self.amount = amount
