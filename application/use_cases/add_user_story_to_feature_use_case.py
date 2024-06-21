from application.repositories.feature_repository import FeatureRepository
from application.repositories.user_story_repository import UserStoryRepository

class AddUserStoryToFeatureUseCase:
    def __init__(self, feature_repository: FeatureRepository, user_story_repository: UserStoryRepository):
        self.feature_repository = feature_repository
        self.user_story_repository = user_story_repository

    def execute(self, feature_id: int, user_story_id: int):
        feature = self.feature_repository.get(feature_id)
        user_story = self.user_story_repository.get(user_story_id)

        if feature and user_story:
            feature.user_stories.append(user_story)
            self.feature_repository.update(feature)
            return True
        else:
            return False
