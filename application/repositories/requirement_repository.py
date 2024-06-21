from typing import Protocol

from domain.requirement import Requirement


class RequirementRepository(Protocol):
    def add(self, requirement: Requirement) -> None: ...
