# User Stories
from typing import List, Optional

from domain.entities.acceptance_criterion import AcceptanceCriterion
from domain.entities.task import Task


class UserStory:
    """
    Represents a user story in the requirements generator.

    Attributes:
        id (str): The unique identifier of the user story.
        title (str): The title of the user story.
        as_a (str): The role of the user who will benefit from the user story.
        i_want (str): The desired action or functionality described by the user story.
        so_that (str): The reason or benefit of implementing the user story.
        acceptance_criteria (Optional[List[AcceptanceCriterion]]): The acceptance criteria for the user story.
        parent_feature_id (str): The unique identifier of the parent feature.
        status (str): The status of the user story ("To Do", "In Progress", "Done").
        tasks (List[Task]): The list of tasks associated with the user story.
    """

    def __init__(
        self,
        id: str,
        title: str,
        as_a: str,
        i_want: str,
        so_that: str,
        acceptance_criteria: Optional[List[AcceptanceCriterion]],
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
        self.tasks = []

    def add_acceptance_criterion(self, criterion: AcceptanceCriterion):
        """
        Adds the given acceptance criterion to the user story.

        Args:
            criterion (AcceptanceCriterion): The acceptance criterion to be added.

        Returns:
            None
        """
        self.acceptance_criteria.append(criterion)
        print(f"Domain Event: Acceptance Criteria added to {self.title}")

    def add_task(self, task_description: str):
        """
        Adds a new task to the user story.

        Parameters:
        - task_description (str): The description of the task.

        Returns:
        - None
        """
        new_task = Task(task_description)
        self.tasks.append(new_task)

    def complete_task(self, task_index: int):
        """
        Completes a task at the specified index.

        Args:
            task_index (int): The index of the task to complete.

        Raises:
            IndexError: If the task index is out of bounds.
        """
        if 0 <= task_index < len(self.tasks):
            self.tasks[task_index].complete_task()
        else:
            raise IndexError("Task index out of bounds")
