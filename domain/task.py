class Task:
    """
    Represents a task in the requirements generator.

    Attributes:
        description (str): The description of the task.
        completed (bool): Indicates whether the task is completed or not.
        parent_user_story_id (str): The ID of the parent user story.
    """

    def __init__(self, description: str, parent_user_story_id: str):
        """
        Initializes a new Task object.

        Args:
            description (str): The description of the task.
            parent_user_story_id (str): The ID of the parent user story.

        Attributes:
            description (str): The description of the task.
            completed (bool): Indicates whether the task is completed or not.
            parent_user_story_id (str): The ID of the parent user story.
        """
        self.description = description
        self.completed = False
        self.parent_user_story_id = parent_user_story_id

    def complete_task(self):
        """
        Marks the task as completed.
        """
        self.completed = True
