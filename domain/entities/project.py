from typing import List, Optional
from domain.entities import theme
from domain.entities.initiative import Initiative
from domain.entities.theme import Theme
from domain.entities.epic import Epic


# domain models should contain the business logic without domain events being called


class Project:
    """
    Represents a project. Container class to hold and manage multiple initiatives.


    Attributes:
      id (str): The unique identifier for the project.
      name (str): The name of the project.
      has_initiatives (bool): Whether the project has initiatives.
      themes (List[Theme]): The list of themes associated with the project.
      initiatives (List[Initiative]): The list of initiatives.
    """

    # Attributes:
    # epics (List[Epic]): The list of epics associated with the project.

    def __init__(self, id: str, name: str, has_initiatives: bool):
        """
        Initializes a new Project instance.

        Args:
            id (str): The unique identifier for the project.
            name (str): The name of the project.
            has_initiatives (bool): Whether the project has initiatives.

        Attributes:
            id (str): The unique identifier for the project.
            name (str): The name of the project.
            has_initiatives (bool): Whether the project has initiatives.
            themes (List[Theme]): The list of themes associated with the project.
        """
        self.id = id
        self.name = name
        self.themes: List["Theme"] = []
        self.has_initiatives = has_initiatives
        self.initiatives: Optional[List[Initiative]] = None

    def init_initiatives(self):
        """
        Initializes the initiatives for the project if has_initiatives is True.
        """
        if self.has_initiatives:
            self.initiatives = []
            print(f"Domain Event: Initiatives initialized for Project '{self.name}'")

    def add_initiative(self, initiative: Initiative):
        """
        Adds an initiative to the container.

        Args:
            initiative (Initiative): The initiative to be added.
        """
        self.initiatives.append(initiative)
        print(f"Domain Event: Initiative '{initiative.title}' added to the container")

    def get_initiative_by_id(self, initiative_id: str) -> Optional[Initiative]:
        """
        Retrieves an initiative by its unique identifier.

        Args:
            initiative_id (str): The unique identifier of the initiative.

        Returns:
            Optional[Initiative]: The initiative with the specified ID, or None if not found.
        """
        for initiative in self.initiatives:
            if initiative.id == initiative_id:
                return initiative
        return None

    def remove_initiative(self, initiative_id: str):
        """
        Removes an initiative from the container by its unique identifier.

        Args:
            initiative_id (str): The unique identifier of the initiative to be removed.
        """
        self.initiatives = [
            initiative
            for initiative in self.initiatives
            if initiative.id != initiative_id
        ]
        print(
            f"Domain Event: Initiative with ID '{initiative_id}' removed from the container"
        )

    def link_epic_to_initiative(self, epic_id: str, initiative_id: str):
        """
        Links an epic to an initiative.

        Args:
            epic_id (str): The unique identifier of the epic.
            initiative_id (str): The unique identifier of the initiative.
        """

        for initiative in self.initiatives:
            if initiative.id == initiative_id:
                for theme in self.themes:
                    for epic in theme.epics:
                        if epic.id == epic_id:
                            initiative.add_epic(epic)
                            print(
                                f"Domain Event: Epic with ID '{epic_id}' linked to initiative with ID '{initiative_id}'"
                            )
                            return
                return
