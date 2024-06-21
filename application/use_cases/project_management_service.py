# Service Layer
from domain.epic import Epic
from domain.feature import Feature
from domain.requirement import Requirement
from domain.user_story import UserStory


class ProjectManagementService:
    """
    A service that provides methods for managing projects, epics, features, user stories, and requirements.
    """

    def create_epic(self, id, title, description):
        """
        Create a new epic with the given id, title, and description.

        Args:
            id (int): The unique identifier for the epic.
            title (str): The title of the epic.
            description (str): The description of the epic.

        Returns:
            Epic: The newly created epic object.
        """
        return Epic(id, title, description)

    def create_feature(
        self, epic: Epic, id: str, title: str, description: str
    ) -> Feature:
        """
        Creates a new feature and adds it to the specified epic.

        Args:
            epic (Epic): The epic to which the feature belongs.
            id (str): The ID of the feature.
            title (str): The title of the feature.
            description (str): The description of the feature.

        Returns:
            Feature: The newly created feature.
        """
        feature = Feature(id, title, description, epic.id, None, "To Do")
        epic.add_feature(feature)
        return feature

    def create_user_story(
        self,
        feature: Feature,
        id: str,
        title: str,
        as_a: str,
        i_want: str,
        so_that: str,
    ) -> UserStory:
        """
        Creates a new user story and adds it to the specified feature.

        Args:
            feature (Feature): The feature to which the user story will be added.
            id (str): The ID of the user story.
            title (str): The title of the user story.
            as_a (str): The role of the user in the story.
            i_want (str): The user's goal or desired outcome.
            so_that (str): The reason or benefit of achieving the goal.

        Returns:
            UserStory: The created user story.

        """
        user_story = UserStory(
            id, title, as_a, i_want, so_that, None, feature.id, "To Do"
        )
        feature.add_user_story(user_story)
        return user_story

    def add_acceptance_criteria(self, user_story: UserStory, criteria: str):
        """
        Adds acceptance criteria to a user story.

        Parameters:
        - user_story (UserStory): The user story to add acceptance criteria to.
        - criteria (str): The acceptance criteria to add.

        Returns:
        - None
        """
        user_story.define_acceptance_criteria(criteria)

    def create_requirement(self, id: str, description: str, type: str) -> Requirement:
        """
        Creates a new requirement with the given ID, description, and type.

        Args:
            id (str): The ID of the requirement.
            description (str): The description of the requirement.
            type (str): The type of the requirement.

        Returns:
            Requirement: The newly created requirement object.
        """
        return Requirement(id, description, type, "Pending")

    def add_feature_to_epic(self, epic: Epic, feature: Feature):
        """
        Adds a feature to an epic.

        Args:
            epic (Epic): The epic to which the feature will be added.
            feature (Feature): The feature to be added to the epic.

        Returns:
            None
        """
        epic.add_feature(feature)


# Example Use Case
# service = ProjectManagementService()
# epic = service.create_epic("E1", "Epic Title", "Epic Description")
# feature = service.create_feature(epic, "F1", "Feature Title", "Feature Description")
# user_story = service.create_user_story(feature, "US1", "User Story Title", "Developer", "Create a login feature", "Ease user access")
# service.add_acceptance_criteria(user_story, "Successful login within 2 seconds")

# Usage Example
# service = ProjectManagementService()
# epic = service.create_epic("E1", "Login Feature", "Epic for user login")
# feature = service.create_feature(epic, "F1", "User Authentication", "Feature for authenticating users")
# user_story = service.create_user_story(feature, "US1", "Successful Login", "User should be able to log in successfully")
# requirement = service.create_requirement("R1", "System should authenticate user in less than 2 seconds", "Functional")

# user_story.add_requirement(requirement)
# feature.add_requirement(requirement)
