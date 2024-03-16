# Service Layer
from domain.epic import Epic
from domain.feature import Feature
from domain.requirement import Requirement
from domain.user_story import UserStory


class ProjectManagementService:
    def create_epic(self, id, title, description):
        return Epic(id, title, description)

    def create_feature(
        self, epic: Epic, id: str, title: str, description: str
    ) -> Feature:
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
        user_story = UserStory(
            id, title, as_a, i_want, so_that, None, feature.id, "To Do"
        )
        feature.add_user_story(user_story)
        return user_story

    def add_acceptance_criteria(self, user_story: UserStory, criteria: str):
        user_story.define_acceptance_criteria(criteria)

    def create_requirement(self, id: str, description: str, type: str) -> Requirement:
        return Requirement(id, description, type, "Pending")


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
