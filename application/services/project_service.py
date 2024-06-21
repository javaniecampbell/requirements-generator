from typing import Optional, Protocol

from domain.project import Project


class ProjectService(Protocol):

    def create_project(
        self, name: str, description: Optional[str] = None
    ) -> Project: ...
