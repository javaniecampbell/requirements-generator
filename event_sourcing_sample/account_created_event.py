from domain.event import Event


class AccountCreated(Event):
    def __init__(self, account_id, owner):
        super().__init__(
            type="AccountCreated",
            data={"account_id": account_id, "owner": owner},
            aggregate_id=account_id,
        )
        self.version = 0
        self.account_id = account_id
        self.owner = owner
