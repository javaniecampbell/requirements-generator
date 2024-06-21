from domain.event import Event


class MoneyDeposited(Event):
    """
    Represents an event that is triggered when money is deposited into an account.

    Attributes:
        account_id (str): The ID of the account where the money is deposited.
        amount (float): The amount of money deposited.
    """

    def __init__(self, account_id, amount):
        """
        Initializes a MoneyDepositedEvent object.

        Args:
            account_id (str): The ID of the account where the money is being deposited.
            amount (float): The amount of money being deposited.

        Attributes:
            version (int): The version of the event.
            account_id (str): The ID of the account where the money is being deposited.
            amount (float): The amount of money being deposited.
        """
        super().__init__(
            type="MoneyDeposited",
            data={"account_id": account_id, "amount": amount},
            aggregate_id=account_id,
        )
        self.version = 0
        self.account_id = account_id
        self.amount = amount
