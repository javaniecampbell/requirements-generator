from typing import Any
from application.repositories.epic_repository import EpicRepository
from application.repositories.feature_repository import FeatureRepository
from application.use_cases import UseCase
from domain.feature import Feature
from domain.epic import Epic


class AddFeatureToEpicUseCase(UseCase):
    def __init__(
        self, feature_repository: FeatureRepository, epic_repository: EpicRepository
    ):
        self.feature_repository = feature_repository
        self.epic_repository = epic_repository

    def execute(self, request: dict) -> None:
        feature_id, epic_id = request["feature_id"], request["epic_id"]

        feature: Feature = self.feature_repository.get(feature_id)
        epic: Epic = self.epic_repository.get(epic_id)

        if feature is None or epic is None:
            return

        epic.add_feature(feature)
        self.epic_repository.update(epic)

    def validate_request(self, request: Any) -> None:
        if not isinstance(request, dict):
            raise ValueError("Request must be a dictionary.")
        if "feature_id" not in request:
            raise ValueError("Feature ID is required.")
        if "epic_id" not in request:
            raise ValueError("Epic ID is required.")
        if not isinstance(request["feature_id"], int):
            raise ValueError("Feature ID must be an integer.")
        if not isinstance(request["epic_id"], int):
            raise ValueError("Epic ID must be an integer.")
        if not self.feature_repository.exists(request["feature_id"]):
            raise ValueError("Feature does not exist.")
        if not self.epic_repository.exists(request["epic_id"]):
            raise ValueError("Epic does not exist.")
