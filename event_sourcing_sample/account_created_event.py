from domain.event import Event


class AccountCreated(Event):
    def __init__(self, account_id, owner):
        self.account_id = account_id
        self.owner = owner
