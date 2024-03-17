from domain.event import Event


class MoneyWithdrawn(Event):
    """
    Represents an event indicating that money has been withdrawn from an account.

    Attributes:
        account_id (str): The ID of the account from which the money was withdrawn.
        amount (float): The amount of money that was withdrawn.
    """

    def __init__(self, account_id, amount):
        """
        Initializes a new instance of the MoneyWithdrawnEvent class.

        Args:
            account_id (str): The ID of the account from which money is being withdrawn.
            amount (float): The amount of money being withdrawn.

        Attributes:
            version (int): The version of the event.
            account_id (str): The ID of the account from which money is being withdrawn.
            amount (float): The amount of money being withdrawn.
        """
        super().__init__(
            type="MoneyWithdrawn",
            data={"account_id": account_id, "amount": amount},
            aggregate_id=account_id,
        )
        self.version = 0
        self.account_id = account_id
        self.amount = amount
