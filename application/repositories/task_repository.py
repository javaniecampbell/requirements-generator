from typing import List, Protocol
from domain.task import Task


class TaskRepository(Protocol):
    def get_all(self) -> List[Task]: ...

    def get_by_id(self, id: int) -> Task: ...

    def create(self, task: Task) -> Task: ...

    def update(self, task: Task) -> Task: ...

    def delete(self, id: int) -> None: ...
