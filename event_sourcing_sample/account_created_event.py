from domain.event import Event


class AccountCreated(Event):
    def __init__(self, account_id, owner):
        self.aggregate_id = account_id
        self.account_id = account_id
        self.owner = owner
