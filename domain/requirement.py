from typing import List


# Functional & Non-Functional Requirements
class Requirement:
    def __init__(self, id: str, description: str, priority: str, status: str):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status


class NonFunctionalRequirement(Requirement):
    def __init__(
        self, id: str, description: str, priority: str, status: str, category: str
    ):
        super().__init__(id, description, priority, status)
        self.category = category
