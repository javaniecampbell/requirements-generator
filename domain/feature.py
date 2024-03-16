from typing import List

from domain.user_story import UserStory


class Feature:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        parent_epic_id: str,
        user_stories: List["UserStory"],
        status: str,
    ):

        self.id = id
        self.title = title
        self.description = description
        self.parent_epic_id = parent_epic_id
        self.user_stories = user_stories
        self.status = status
