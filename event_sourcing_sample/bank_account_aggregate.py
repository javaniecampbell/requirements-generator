from domain.event import Event
from event_sourcing_sample.account_created_event import AccountCreated
from event_sourcing_sample.money_deposited_event import MoneyDeposited
from event_sourcing_sample.money_withdrawn_event import MoneyWithdrawn


class BankAccount:
    """
    Represents a bank account.

    Attributes:
        id (int): The unique identifier of the bank account.
        owner (str): The owner of the bank account.
        balance (float): The current balance of the bank account.
        changes (list): A list of events that have been applied to the bank account.
    """

    def __init__(self, id, owner=None):
        self.id = id
        self.owner = owner
        self.balance = 0
        self.changes = []

    def apply(self, event: Event):
        """
        Applies the given event to the bank account.

        Args:
            event (Event): The event to be applied.

        Raises:
            ValueError: If the event is not of a valid type.
        """
        if isinstance(event, AccountCreated):
            self.owner = event.owner
        elif isinstance(event, MoneyDeposited):
            self.balance += event.amount
        elif isinstance(event, MoneyWithdrawn):
            self.balance -= event.amount

    def create_account(self, owner):
        """
        Creates a new bank account with the given owner.

        Args:
            owner (str): The owner of the bank account.
        """
        event = AccountCreated(account_id=self.id, owner=owner)
        self.apply(event)
        self.changes.append(event)

    def deposit_money(self, amount):
        """
        Deposits the specified amount of money into the bank account.

        Args:
            amount (float): The amount of money to be deposited.
        """
        event = MoneyDeposited(account_id=self.id, amount=amount)
        self.apply(event)
        self.changes.append(event)

    def withdraw_money(self, amount):
        """
        Withdraws the specified amount of money from the bank account.

        Args:
            amount (float): The amount of money to be withdrawn.

        Raises:
            ValueError: If the amount exceeds the available balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        event = MoneyWithdrawn(account_id=self.id, amount=amount)
        self.apply(event)
        self.changes.append(event)


