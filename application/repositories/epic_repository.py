from typing import Protocol

from domain.epic import Epic


class EpicRepository(Protocol):
    def get(self, epic_id: int) -> "Epic": ...
