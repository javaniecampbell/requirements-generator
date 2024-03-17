# Example of extending AggregateRoot
from domain.aggregate_root import AggregateRoot

# Aggregates should ensure the underlying domain models are valid before publishing domain events, should handle domain events and subscription to domain events


class ProjectAggregate(AggregateRoot):
    """
    Represents a project aggregate.

    Attributes:
        id (str): The unique identifier of the project.
        name (str): The name of the project.
    """

    def __init__(self, id, name):
        """
        Initializes a new instance of the ProjectAggregate class.

        Args:
            id (int): The ID of the project.
            name (str): The name of the project.
        """
        super().__init__(id)
        self.name = name
        # Additional project-specific initialization

    # Project-specific methods
