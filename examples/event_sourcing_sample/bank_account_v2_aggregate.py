from domain.aggregate_root import AggregateRoot
from domain.snapshot import Snapshot
from event_sourcing_sample.account_created_event import AccountCreated
from event_sourcing_sample.money_deposited_event import MoneyDeposited
from event_sourcing_sample.money_withdrawn_event import MoneyWithdrawn


class BankAccountV2(AggregateRoot):
    """
    Represents a bank account.

    Attributes:
        id (str): The unique identifier of the bank account.
        owner (str): The owner of the bank account.
        balance (float): The current balance of the bank account.
    """

    def __init__(self, id):
        super().__init__(id)
        self.owner = None
        self.balance = 0

    def create_account(self, owner):
        """
        Creates a new bank account.

        Args:
            owner (str): The owner of the bank account.
        """
        self.apply(AccountCreated(account_id=self.get_id(), owner=owner))

    def deposit_money(self, amount):
        """
        Deposits money into the bank account.

        Args:
            amount (float): The amount of money to deposit.
        """
        self.apply(MoneyDeposited(account_id=self.get_id(), amount=amount))

    def withdraw_money(self, amount):
        """
        Withdraws money from the bank account.

        Args:
            amount (float): The amount of money to withdraw.

        Raises:
            ValueError: If the amount to withdraw is greater than the current balance.
        """
        if amount > self.balance:
            raise ValueError("Insufficient funds")
        self.apply(MoneyWithdrawn(account_id=self.get_id(), amount=amount))

    def handle(self, event):
        """
        Handles an event by calling the corresponding event handler method.

        Args:
            event: The event to handle.

        Raises:
            ValueError: If the event handler method for the event is not found.
        """
        handler_name = f"handle_{event.__class__.__name__}"
        handler = getattr(self, handler_name, None)
        if handler:
            handler(event)
        else:
            raise ValueError(f"Handler for {event.__class__.__name__} not found")

    def handle_AccountCreated(self, event):
        """
        Event handler for the AccountCreated event.

        Args:
            event (AccountCreated): The AccountCreated event.
        """
        self.owner = event.owner

    def handle_MoneyDeposited(self, event):
        """
        Event handler for the MoneyDeposited event.

        Args:
            event (MoneyDeposited): The MoneyDeposited event.
        """
        self.balance += event.amount

    def handle_MoneyWithdrawn(self, event):
        """
        Event handler for the MoneyWithdrawn event.

        Args:
            event (MoneyWithdrawn): The MoneyWithdrawn event.
        """
        self.balance -= event.amount

    def snapshot_state(self):
        """
        Returns the current state of the bank account as a dictionary.

        Returns:
            dict: The current state of the bank account.
        """
        return {"owner": self.owner, "balance": self.balance}

    def restore_from_snapshot(self, snapshot: Snapshot):
        """
        Restores the state of the bank account from a snapshot.

        Args:
            snapshot (Snapshot): The snapshot to restore from.
        """
        self.owner = snapshot.state["owner"]
        self.balance = snapshot.state["balance"]
        self.set_version(snapshot.version)