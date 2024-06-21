from typing import List, Protocol

from domain.models import Contract
from domain.entities.requirement import Requirement


class RequirementRepository(Protocol):
    def add(self, requirement: Requirement) -> None: ...

    def get(self, id: int) -> Requirement: ...

    def get_requirements(self, project_details) -> List[Requirement]: ...

    def create_contract(self, requirements: List[Requirement]) -> Contract: ...
