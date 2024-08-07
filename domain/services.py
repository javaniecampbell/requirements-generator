# Will store the abstract classes or interfaces for the domain services to be implemented in the infrastructure layer
from abc import ABC, abstractmethod
from typing import List
from domain.entities.feature import Feature
from domain.entities.requirement import Requirement


class AbstractService(ABC):
    """
    Abstract base class for domain services.
    """

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        Execute the service logic.
        """
        raise NotImplementedError


class RequirementGenerationService(ABC):
    """
    Abstract base class for the RequirementGenerationService.
    """

    @abstractmethod
    def generate_requirements(self, user_input: str) -> List[Requirement]:
        raise NotImplementedError

    @abstractmethod
    def generate_featurelist(self, requirements: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate_user_stories(self, featurelist: str) -> str:
        raise NotImplementedError

    @abstractmethod
    def generate_featurelist_from_requirements(
        self, requirements: List[Requirement]
    ) -> List[Feature]:
        raise NotImplementedError

    @abstractmethod
    def generate_user_stories_from_featurelist(
        self, featurelist: List[Feature]
    ) -> List[str]:
        raise NotImplementedError
