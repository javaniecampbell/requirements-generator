from typing import List, Optional
from domain.entities.requirement import Requirement
from domain.entities.scenario import Scenario


class Feature:
    """
    Represents a feature in the requirements generator.

    Attributes:
        id (str): The unique identifier of the feature.
        title (str): The title of the feature.
        description (str): The description of the feature.
        parent_epic_id (str): The ID of the parent epic.
        scenarios (Optional[List[Scenario]]): The list of scenarios associated with the feature.
        status (str): The status of the feature. Can be "To Do", "In Progress", or "Done".
        requirements (List[Requirement]): The list of requirements associated with the feature.
    """

    def __init__(
        self, id: str, title: str, description: str, parent_epic_id: str, status: str
    ):
        """
        Initializes a new Feature object.

        Args:
            id (str): The unique identifier for the feature.
            title (str): The title of the feature.
            description (str): The description of the feature.
            parent_epic_id (str): The unique identifier of the parent epic.
            status (str): The status of the feature. Can be "To Do", "In Progress", or "Done".
        """
        self.id = id
        self.title = title
        self.description = description
        self.parent_epic_id = parent_epic_id
        self.status = status
        self.scenarios: List[Scenario] = []
        self.requirements: List[Requirement] = []

    def add_scenario(self, scenario: Scenario):
        """
        Adds a scenario to the feature.

        Args:
            scenario (Scenario): The scenario to be added.
        """
        self.scenarios.append(scenario)
        print(
            f"Domain Event: Scenario '{scenario.title}' added to Feature '{self.title}'"
        )

    def add_requirement(self, requirement: Requirement):
        """
        Adds a requirement to the feature.

        Args:
            requirement (Requirement): The requirement to be added.
        """
        self.requirements.append(requirement)
        print(
            f"Domain Event: {requirement.type} Requirement added to Feature '{self.title}'"
        )
