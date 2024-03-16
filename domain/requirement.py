from typing import List


# Functional & Non-Functional Requirements
class Requirement:
    def __init__(
        self, id: str, description: str, priority: str, status: str, type: str
    ):
        self.id = id
        self.description = description
        self.priority = priority
        self.status = status  # "Pending", "Approved", "Implemented"
        self.type = type  # "Functional" or "Non-Functional"


class NonFunctionalRequirement(Requirement):
    def __init__(
        self, id: str, description: str, priority: str, status: str, category: str
    ):
        super().__init__(id, description, priority, status, "Non-Functional")
        self.category = (
            category  # "Performance", "Security", "Usability", "Reliability"
        )
