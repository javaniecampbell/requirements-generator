from domain.aggregate_root import AggregateRoot
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


class BankAccountV2(AggregateRoot):
    def __init__(self, id):
        super().__init__(id)
        self.owner = None
        self.balance = 0

    def create_account(self, owner):
        self.apply(AccountCreated(account_id=self.id, owner=owner))

    def deposit_money(self, amount):
        self.apply(MoneyDeposited(account_id=self.id, amount=amount))

    def withdraw_money(self, amount):
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.apply(MoneyWithdrawn(account_id=self.id, amount=amount))

    def handle(self, event):
        handler_name = f"handle_{event.__class__.__name__}"
        handler = getattr(self, handler_name, None)
        if handler:
            handler(event)
        else:
            raise ValueError(f"Handler for {event.__class__.__name__} not found")

    def handle_AccountCreated(self, event):
        self.owner = event.owner

    def handle_MoneyDeposited(self, event):
        self.balance += event.amount

    def handle_MoneyWithdrawn(self, event):
        self.balance -= event.amount
