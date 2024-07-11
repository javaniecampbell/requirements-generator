from domain.value_objects.gherkin import Gherkin


from typing import List, Optional


class AcceptanceCriterion:
    """
    Represents an acceptance criterion which contains a list of Gherkin steps.

    Usage:
    Creating acceptance criteria

    AcceptanceCriterion([
        Gherkin("Given", "I am on the registration page"),
        Gherkin("When", "I enter my details and click on the sign-up button"),
        Gherkin("Then", "I should be registered on the platform"),
        Gherkin("And", "I should be redirected to my dashboard")
    ])

    Creating Gherkin steps

    gherkin_steps1 = [
        Gherkin("Given", "I am on the registration page"),
        Gherkin("When", "I enter my details and click on the sign-up button"),
        Gherkin("Then", "I should be registered on the platform"),
        Gherkin("And", "I should be redirected to my dashboard")
    ]

    gherkin_steps2 = [
        Gherkin("Given", "I am a new user"),
        Gherkin("When", "I navigate to the sign-up page"),
        Gherkin("Then", "I should see the registration form")
    ]

    Creating acceptance criteria

    acceptance_criterion1 = AcceptanceCriterion(gherkin_steps1)
    acceptance_criterion2 = AcceptanceCriterion(gherkin_steps2)

    Attributes:
        id (str): The unique identifier of the acceptance criterion.
        parent_user_story_id (str): The unique identifier of the parent user story.
        gherkin_steps (List[Gherkin]): The list of Gherkin steps.
    """

    def __init__(
        self, id: str, story_id: str, gherkin_steps: Optional[List["Gherkin"]] = None
    ):
        """
        Initializes a new instance of the AcceptanceCriterion class.

        Args:
            id (str): The unique identifier of the acceptance criterion.
            story_id (str): The unique identifier of the parent user story.
            gherkin_steps (Optional[List[Gherkin]]): The list of Gherkin steps.
        """
        self.id = id
        self.parent_user_story_id = story_id
        self.order = 0
        self.gherkin_steps = gherkin_steps if gherkin_steps else []

    def add_gherkin_step(self, gherkin_step: "Gherkin"):
        """
        Adds a Gherkin step to the acceptance criterion.

        Args:
            gherkin_step (Gherkin): The Gherkin step to add.
        """
        self.gherkin_steps.append(gherkin_step)

    def __str__(self):
        """
        Returns the string representation of the acceptance criterion.

        Returns:
            str: The formatted Gherkin steps.
        """
        return "\n".join([str(step) for step in self.gherkin_steps])

    def shift_order(self, order: int):
        """
        Shifts the order of the acceptance criterion.

        Args:
            order (int): The new order of the acceptance criterion.
        """
        self.order = order
