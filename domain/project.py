from typing import List
from domain.epic import Epic


# domain models should contain the business logic without domain events being called


class Project:
    """
    Represents a project.

    Attributes:
        id (str): The unique identifier of the project.
        name (str): The name of the project.
        epics (List[Epic]): The list of epics associated with the project.
    """

    def __init__(self, id: str, name: str):
        """
        Initializes a new Project instance.

        Args:
            id (str): The unique identifier for the project.
            name (str): The name of the project.

        Attributes:
            id (str): The unique identifier for the project.
            name (str): The name of the project.
            epics (List[Epic]): The list of epics associated with the project.
        """
        self.id = id
        self.name = name
        self.epics: List["Epic"] = []
