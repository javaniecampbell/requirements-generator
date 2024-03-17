from domain.event import Event


class MoneyDeposited(Event):
    def __init__(self, account_id, amount):
        super().__init__(
            type="MoneyDeposited",
            data={"account_id": account_id, "amount": amount},
            aggregate_id=account_id,
        )
        self.account_id = account_id
        self.amount = amount
