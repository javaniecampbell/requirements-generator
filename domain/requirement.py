from typing import List


# Functional & Non-Functional Requirements
class Requirement:
    """
    Represents a requirement.

    Attributes:
        id (str): The unique identifier of the requirement.
        description (str): The description of the requirement.
        priority (str): The priority of the requirement.
        status (str): The status of the requirement. Can be "Pending", "Approved", or "Implemented".
        type (str): The type of the requirement. Can be "Functional" or "Non-Functional".
    """

    def __init__(
        self, id: str, description: str, priority: str, status: str, type: str
    ):
        """
        Initialize a Requirement object.

        Args:
            id (str): The unique identifier for the requirement.
            description (str): The description of the requirement.
            priority (str): The priority of the requirement.
            status (str): The status of the requirement.
            type (str): The type of the requirement.
        """
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status
        self.type = type


class NonFunctionalRequirement(Requirement):
    """
    Represents a non-functional requirement.

    Attributes:
        id (str): The unique identifier of the requirement.
        description (str): The description of the requirement.
        priority (str): The priority of the requirement.
        status (str): The status of the requirement.
        category (str): The category of the non-functional requirement.
            Possible values are "Performance", "Security", "Usability", "Reliability".
    """

    def __init__(
        self, id: str, description: str, priority: str, status: str, category: str
    ):
        """
        Initializes a Requirement object.

        Args:
            id (str): The unique identifier for the requirement.
            description (str): The description of the requirement.
            priority (str): The priority of the requirement.
            status (str): The status of the requirement.
            category (str): The category of the requirement.

        Returns:
            None
        """
        super().__init__(id, description, priority, status, "Non-Functional")
        self.category = category
