from application.repositories.requirement_repository import RequirementRepository
from domain.requirement import Requirement


# class GenerateRequirementsUseCase:
#     def __init__(self, requirement_repository: RequirementRepository):
#         self.requirement_repository = requirement_repository

#     def execute(self, project_details):
#         requirements = self.requirement_repository.get_requirements(project_details)
#         return requirements


class GenerateContractUseCase:
    def __init__(self, requirement_repository: RequirementRepository):
        self.requirement_repository = requirement_repository

    def execute(self, requirements):
        contract = self.requirement_repository.create_contract(requirements)
        return contract
