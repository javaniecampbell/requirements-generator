# Example of extending AggregateRoot
from domain.aggregate_root import AggregateRoot

# Aggregates should ensure the underlying domain models are valid before publishing domain events, should handle domain events and subscription to domain events


class ProjectAggregate(AggregateRoot):
    def __init__(self, id, name):
        super().__init__(id)
        self.name = name
        # Additional project-specific initialization

    # Project-specific methods
