from typing import List, Optional

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
        self.status = status

    def add_user_story(self, user_story: UserStory):
        self.user_stories.append(user_story)
