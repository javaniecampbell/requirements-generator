from typing import Protocol

from domain.user_story import UserStory


class UserStoryRepository(Protocol):
    def get(self, user_story_id: int) -> UserStory: ...
    def update(self, user_story: UserStory) -> None: ...
