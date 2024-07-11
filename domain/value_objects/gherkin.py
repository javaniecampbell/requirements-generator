from domain.value_objects.value_object import ValueObject


class Gherkin(ValueObject):
    """
    Represents a Gherkin step in the acceptance criteria.

    Usage:
    Creating Gherkin steps

    Gherkin("Given", "I am on the registration page")

    Gherkin("When", "I enter my details and click on the sign-up button")

    Gherkin("Then", "I should be registered on the platform")

    Gherkin("And", "I should be redirected to my dashboard")

    gherkin_steps = [
        Gherkin("Given", "I am on the registration page"),
        Gherkin("When", "I enter my details and click on the sign-up button"),
        Gherkin("Then", "I should be registered on the platform"),
        Gherkin("And", "I should be redirected to my dashboard")
    ]

    Attributes:
        keyword (str): The Gherkin keyword (Given, When, Then, And, But).
        text (str): The step description.
    """

    def __init__(self, keyword: str, text: str):
        """
        Initializes a new instance of the Gherkin class.

        Args:
            keyword (str): The Gherkin keyword.
            text (str): The step description.
        """
        self.keyword = keyword
        self.text = text

    def __str__(self):
        """
        Returns the string representation of the Gherkin step.

        Returns:
            str: The formatted Gherkin step.
        """
        return f"{self.keyword} {self.text}"

    def __eq__(self, other):
        """
        Checks if the current Gherkin step is equal to another Gherkin step.
        """
        if isinstance(other, Gherkin):
            return self.keyword == other.keyword and self.text == other.text
        return False
