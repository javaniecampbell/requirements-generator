from typing import List
from domain.entities.epic import Epic


class Theme:
    """
    Represents a theme, which is a high-level grouping of related epics.

    Attributes:
        id (str): The unique identifier of the theme.
        title (str): The title of the theme.
        description (str): The description of the theme.
        epics (Optional[List[Epic]]): The list of epics associated with the theme.
        status (str): The status of the theme. Can be one of "To Do", "In Progress", or "Done".
    """

    def __init__(self, id: str, title: str, description: str, status: str):
        """
        Initializes a new instance of the Theme class.

        Args:
            id (str): The unique identifier of the theme.
            title (str): The title of the theme.
            description (str): The description of the theme.
            status (str): The status of the theme. Can be one of "To Do", "In Progress", or "Done".
        """
        self.id = id
        self.title = title
        self.description = description
        self.status = status
        self.epics: List[Epic] = []

    def add_epic(self, epic: Epic):
        """
        Adds an epic to the theme.

        Args:
            epic (Epic): The epic to be added.
        """
        self.epics.append(epic)
        print(f"Domain Event: Epic '{epic.title}' added to Theme '{self.title}'")
