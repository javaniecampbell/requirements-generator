from application.repositories import RequirementRepository, UserStoryRepository
from domain.requirement import Requirement
from domain.user_story import UserStory

class AddRequirementToUserStoryUseCase:
    def __init__(self, requirement_repo: RequirementRepository, user_story_repo: UserStoryRepository):
        self.requirement_repo = requirement_repo
        self.user_story_repo = user_story_repo

    def execute(self, user_story_id: int, requirement_data: dict) -> Requirement:
        user_story = self.user_story_repo.get(user_story_id)
        if not user_story:
            raise ValueError(f"User story with id {user_story_id} not found")

        requirement = Requirement(**requirement_data)
        self.requirement_repo.add(requirement)
        user_story.requirements.append(requirement)
        self.user_story_repo.update(user_story)
        return requirement

