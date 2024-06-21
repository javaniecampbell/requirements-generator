from dataclasses import dataclass
from typing import Optional

from application.repositories.project_repository import ProjectRepository
from application.services.project_service import ProjectService
from domain.project import Project


@dataclass
class CreateProjectRequest:
    name: str
    description: Optional[str] = None


class CreateProjectUseCase:
    def __init__(
        self, project_repository: ProjectRepository, project_service: ProjectService
    ):
        self.project_repository = project_repository
        self.project_service = project_service

    def execute(self, request: CreateProjectRequest):
        project: Project = self.project_service.create_project(
            request.name, request.description
        )
        self.project_repository.save(project)
        return project
