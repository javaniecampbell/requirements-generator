from typing import List
from application.use_cases import UseCase
from domain.services import RequirementGenerationService
from domain.requirement import Requirement


class GenerateRequirementsUseCase(UseCase):
    def __init__(self, requirement_generation_service: RequirementGenerationService):
        self.requirement_generation_service = requirement_generation_service

    def execute(self, request: dict) -> List[Requirement]:
        self.validate_request(request)
        user_input = request.get("user_input")
        requirements = self.requirement_generation_service.generate_requirements(
            user_input
        )
        return self.handle_response(requirements)

    def validate_request(self, request: dict) -> None:
        if not request.get("user_input"):
            raise ValueError("user_input is required")

    def handle_response(self, response: List[Requirement]) -> List[dict]:
        return [req.to_dict() for req in response]


# class GenerateRequirementsUseCaseFactory:
#     @staticmethod
#     def create() -> GenerateRequirementsUseCase:
#         requirement_generation_service = RequirementGenerationService()
#         return GenerateRequirementsUseCase(requirement_generation_service)
