from abc import ABC, abstractmethod
from typing import Optional

from domain.entities.project import Project


class ProjectService(ABC):

    @abstractmethod
    def create_project(self, name: str, description: Optional[str] = None) -> Project:
        raise NotImplementedError
