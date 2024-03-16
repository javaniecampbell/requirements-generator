# User Stories
from typing import List, Optional

from domain.requirement import Requirement
from domain.task import Task


class UserStory:
    def __init__(
        self,
        id: str,
        title: str,
        as_a: str,
        i_want: str,
        so_that: str,
        acceptance_criteria: Optional[List[str]],
        parent_feature_id: str,
        status: str,
    ):
        self.id = id
        self.title = title
        self.as_a = as_a
        self.i_want = i_want
        self.so_that = so_that
        self.acceptance_criteria = (
            [] if acceptance_criteria is None else acceptance_criteria
        )
        self.parent_feature_id = parent_feature_id
        self.status = status  # "To Do", "In Progress", "Done"
        self.requirements = []
        self.tasks = []

    def define_acceptance_criteria(self, criteria: str):
        self.acceptance_criteria.append(criteria)
        print(f"Domain Event: Acceptance Criteria added to {self.title}")

    def add_requirement(self, requirement: Requirement):
        self.requirements.append(requirement)
        print(f"Domain Event: {requirement.type} Requirement added to {self.title}")

    def add_task(self, task_description: str):
        new_task = Task(task_description)
        self.tasks.append(new_task)

    def complete_task(self, task_index: int):
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].complete_task()
        else:
            raise IndexError("Task index out of bounds")