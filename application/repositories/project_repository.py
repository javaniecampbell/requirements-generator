from typing import Protocol

from domain.project import Project


class ProjectRepository(Protocol):
    def get(self, project_id: int) -> "Project": ...

    def update(self, project: "Project") -> None: ...

    def save(self, project: Project) -> None: ...
