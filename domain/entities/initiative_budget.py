from domain.value_objects.money import Money


class InitiativeBudget:
    """
    Represents a budget associated with an initiative.

    Attributes:
        id (str): The unique identifier of the budget.
        initiative_id (str): The unique identifier of the initiative.
        budget (Money): The budget allocated for the initiative.
        cost (Money): The cost incurred so far for the initiative.
        remaining_budget (Money): The remaining budget for the initiative.

    """

    def __init__(
        self,
        id: str,
        initiative_id: str,
        budget: Money,
        cost: Money,
        remaining_budget: Money,
    ):
        """
        Initializes a new instance of the InitiativeBudget class.

        Args:
            id (str): The unique identifier of the budget.
            initiative_id (str): The unique identifier of the initiative.
            budget (Money): The budget allocated for the initiative.
            cost (Money): The cost incurred so far for the initiative.
            remaining_budget (Money): The remaining budget for the initiative.
        """
        self.id: str = id
        self.initiative_id: str = initiative_id
        self.budget: Money = budget
        self.cost: Money = cost
        self.remaining_budget: Money = remaining_budget
