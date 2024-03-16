from typing import List


class Scenario:
    def __init__(
        self, id: str, title: str, steps: List[str], parent_feature_id: str, status: str
    ):
        self.id = id
        self.title = title
        self.steps = steps
        self.parent_feature_id = parent_feature_id
        self.status = status  # "To Do", "In Progress", "Done"
