from domain.event import Event


class AccountCreated(Event):
    """
    Represents an event that is triggered when a new account is created.

    Attributes:
        account_id (str): The unique identifier of the account.
        owner (str): The owner of the account.
    """

    def __init__(self, account_id, owner):
        """
        Initializes a new instance of the AccountCreatedEvent class.

        Args:
            account_id (str): The ID of the account being created.
            owner (str): The owner of the account.

        Attributes:
            version (int): The version of the event.
            account_id (str): The ID of the account being created.
            owner (str): The owner of the account.
        """
        super().__init__(
            type="AccountCreated",
            data={"account_id": account_id, "owner": owner},
            aggregate_id=account_id,
        )
        self.version = 0
        self.account_id = account_id
        self.owner = owner
