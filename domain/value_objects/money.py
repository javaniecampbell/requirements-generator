from domain.value_objects.value_object import ValueObject


class Money(ValueObject):
    """
    Represents a money value with a currency.

    Attributes:
        id (str): The unique identifier of the budget.
        amount (float): The amount of the budget.
        currency (str): The currency of the budget.
    """

    def __init__(self, amount: float, currency: str):
        """
        Initializes a new instance of the InitiativeBudget class.

        Args:
            id (str): The unique identifier of the budget.
            amount (float): The amount of the budget.
            currency (str): The currency of the budget.
        """
        self.amount = amount
        self.currency = currency

    def __eq__(self, other):
        if isinstance(other, Money):
            return self.amount == other.amount and self.currency == other.currency
        return False
