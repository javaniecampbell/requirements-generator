from typing import List


class Scenario:
    """
    Represents a scenario in the requirements generator.

    Attributes:
        id (str): The unique identifier of the scenario.
        title (str): The title of the scenario.
        steps (List[str]): The list of steps in the scenario.
        parent_feature_id (str): The unique identifier of the parent feature.
        status (str): The status of the scenario. Can be "To Do", "In Progress", or "Done".
    """

    def __init__(
        self, id: str, title: str, steps: List[str], parent_feature_id: str, status: str
    ):
        """
        Initializes a new Scenario object.

        Args:
            id (str): The unique identifier of the scenario.
            title (str): The title of the scenario.
            steps (List[str]): The list of steps for the scenario.
            parent_feature_id (str): The unique identifier of the parent feature.
            status (str): The status of the scenario.

        Returns:
            None
        """
        self.id = id
        self.title = title
        self.steps = steps
        self.parent_feature_id = parent_feature_id
        self.status = status
