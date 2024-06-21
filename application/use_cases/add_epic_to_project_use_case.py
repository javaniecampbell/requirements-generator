from typing import Protocol

from application.repositories.project_repository import ProjectRepository
from application.repositories.epic_repository import EpicRepository
from application.use_cases import UseCase


class AddEpicToProjectUseCase(UseCase):
    def __init__(
        self,
        project_repository: ProjectRepository,
        epic_repository: EpicRepository,
    ):
        self.project_repository = project_repository
        self.epic_repository = epic_repository

    def execute(self, request: dict) -> None:
        project_id, epic_id = request["project_id"], request["epic_id"]

        project = self.project_repository.get(project_id)
        epic = self.epic_repository.get(epic_id)

        project.add_epic(epic)

        self.project_repository.update(project)

    def validate_request(self, request: dict) -> None:
        if not isinstance(request, dict):
            raise ValueError("Request must be a dictionary.")

        if "project_id" not in request:
            raise ValueError("Project ID is required.")

        if "epic_id" not in request:
            raise ValueError("Epic ID is required.")

        if not isinstance(request["project_id"], int):
            raise ValueError("Project ID must be an integer.")

        if not isinstance(request["epic_id"], int):
            raise ValueError("Epic ID must be an integer.")

        if request["project_id"] <= 0:
            raise ValueError("Project ID must be greater than 0.")

        if request["epic_id"] <= 0:
            raise ValueError("Epic ID must be greater than 0.")

        if not self.project_repository.get(request["project_id"]):
            raise ValueError("Project not found.")

        if not self.epic_repository.get(request["epic_id"]):
            raise ValueError("Epic not found.")
