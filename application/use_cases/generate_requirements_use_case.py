from typing import List
from application.use_cases import UseCase
from domain.services import RequirementGenerationService
from domain.requirement import Requirement


class GenerateRequirementsUseCase(UseCase):
    def __init__(self, requirement_generation_service: RequirementGenerationService):
        self.requirement_generation_service = requirement_generation_service

    def execute(self, request: dict) -> List[Requirement]:
        user_input = request.get("user_input")
        requirements = self.requirement_generation_service.generate_requirements(
            user_input
        )
        return requirements
