# Domain Events
from typing import Any


class DomainEvent:
    """
    Represents a domain event.

    Attributes:
        name (str): The name of the domain event.
        data (Any): The data associated with the domain event.
    """

    def __init__(self, name: str, data: Any):
        """
        Initializes a new instance of the DomainEvent class.

        Args:
            name (str): The name of the domain event.
            data (Any): The data associated with the domain event.
        """
        self.name = name
        self.data = data
