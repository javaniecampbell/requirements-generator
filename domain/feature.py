from typing import List, Optional

from pkg_resources import Requirement

from domain.user_story import UserStory


class Feature:
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
        self.status = status  # "To Do", "In Progress", "Done"
        self.requirements: List["Requirement"] = []

    def add_user_story(self, user_story: UserStory):
        # add parent_feature_id to user_story
        self.user_stories.append(user_story)
        print(
            f"Domain Event: User Story '{user_story.title}' added to Feature '{self.title}'"
        )

    def add_requirement(self, requirement: Requirement):
        self.requirements.append(requirement)
        print(
            f"Domain Event: {requirement.type} Requirement added to Feature '{self.title}'"
        )
