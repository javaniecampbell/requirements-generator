from typing import List
from domain.epic import Epic


# domain models should contain the business logic without domain events being called
class Project:
    def __init__(self, id: str, name: str):
        self.id = id
        self.name = name
        self.epics: List["Epic"] = []
