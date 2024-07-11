from typing import List
from application.use_cases import UseCase
from domain.entities import requirement
from domain.entities.feature import Feature
from domain.services import RequirementGenerationService


class GenerateFeatureListFromRequirementsUseCase(UseCase):
    def __init__(self, requirement_generation_service: RequirementGenerationService):
        self.requirement_generation_service = requirement_generation_service

    def execute(self, request: dict) -> List[Feature]:
        self.validate_request(request)
        user_input = request.get("user_input")
        requirementsData = self.requirement_generation_service.generate_featurelist(
            user_input
        )
        # Might need instructor here to convert to Feature list
        featurelist = (
            self.requirement_generation_service.generate_featurelist_from_requirements(
                []
            )
        )

        return self.handle_response(featurelist)

    def validate_request(self, request: dict) -> None:
        if not request.get("user_input"):
            raise ValueError("user_input is required")

    def handle_response(response: List[Requirement]) -> List[Feature]:
        return [req.to_dict() for req in response]
