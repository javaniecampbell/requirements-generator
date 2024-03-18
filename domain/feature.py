from typing import List, Optional
from domain.requirement import Requirement
from domain.user_story import UserStory


class Feature:
    """
    Represents a feature in the requirements generator.

    Attributes:
        id (str): The unique identifier of the feature.
        title (str): The title of the feature.
        description (str): The description of the feature.
        parent_epic_id (str): The ID of the parent epic.
        user_stories (Optional[List[UserStory]]): The list of user stories associated with the feature.
        status (str): The status of the feature. Can be "To Do", "In Progress", or "Done".
        requirements (List[Requirement]): The list of requirements associated with the feature.
    """

    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        parent_epic_id: str,
        user_stories: Optional[List["UserStory"]],
        status: str,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.parent_epic_id = parent_epic_id
        self.user_stories = [] if user_stories is None else user_stories
        self.status = status
        self.requirements: List["Requirement"] = []

    def add_user_story(self, user_story: UserStory):
        """
        Adds a user story to the feature.

        Args:
            user_story (UserStory): The user story to be added.

        Returns:
            None
        """
        self.user_stories.append(user_story)
        print(
            f"Domain Event: User Story '{user_story.title}' added to Feature '{self.title}'"
        )

    def add_requirement(self, requirement: Requirement):
        """
        Adds a requirement to the feature.

        Args:
            requirement (Requirement): The requirement to be added.

        Returns:
            None
        """
        self.requirements.append(requirement)
        print(
            f"Domain Event: {requirement.type} Requirement added to Feature '{self.title}'"
        )
