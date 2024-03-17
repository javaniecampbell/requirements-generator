# Domain Events
from typing import Any


class DomainEvent:
    def __init__(self, name: str, data: Any):
        self.name = name
        self.data = data
