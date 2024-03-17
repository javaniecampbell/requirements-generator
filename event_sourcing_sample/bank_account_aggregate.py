from domain.event import Event
from event_sourcing_sample.account_created_event import AccountCreated
from event_sourcing_sample.money_deposited_event import MoneyDeposited
from event_sourcing_sample.money_withdrawn_event import MoneyWithdrawn


class BankAccount:
    def __init__(self, id, owner=None):
        self.id = id
        self.owner = owner
        self.balance = 0
        self.changes = []

    def apply(self, event: Event):
        if isinstance(event, AccountCreated):
            self.owner = event.owner
        elif isinstance(event, MoneyDeposited):
            self.balance += event.amount
        elif isinstance(event, MoneyWithdrawn):
            self.balance -= event.amount

    def create_account(self, owner):
        event = AccountCreated(account_id=self.id, owner=owner)
        self.apply(event)
        self.changes.append(event)

    def deposit_money(self, amount):
        event = MoneyDeposited(account_id=self.id, amount=amount)
        self.apply(event)
        self.changes.append(event)

    def withdraw_money(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        event = MoneyWithdrawn(account_id=self.id, amount=amount)
        self.apply(event)
        self.changes.append(event)
