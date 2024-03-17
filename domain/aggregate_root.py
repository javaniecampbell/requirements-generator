from typing import List

from domain.domain_event import DomainEvent


class AggregateRoot:
    """
    Represents the base class for aggregate roots in a domain-driven design.
    """

    def __init__(self, id: str):
        """
        Initializes a new instance of the AggregateRoot class.

        Args:
            id (str): The unique identifier for the aggregate root.
        """
        self._id = id
        self._version = 0
        self._changes: List["DomainEvent"] = []
        self._domain_events: List["DomainEvent"] = []

    def add_domain_event(self, event: DomainEvent):
        """
        Adds a domain event to the aggregate root.

        Args:
            event (DomainEvent): The domain event to be added.

        Returns:
            None
        """
        self._domain_events.append(event)

    def clear_domain_events(self):
        """
        Clears the list of domain events associated with the aggregate root.
        """
        self._domain_events.clear()

    def get_domain_events(self):
        """
        Returns the domain events associated with the aggregate root.

        Returns:
            list: A list of domain events.
        """
        return self._domain_events

    def apply(self, event: DomainEvent):
        """
        Applies a domain event to the aggregate root, updating its state and version.

        Args:
            event (DomainEvent): The domain event to apply.
        """
        self.handle(event)
        self._version = event.version  # Update version based on event version
        self._changes.append(event)

    def handle(self, event: DomainEvent):
        """
        This method will be overridden by derived aggregates to handle specific event types.

        Args:
            event (DomainEvent): The domain event to handle.
        """
        raise NotImplementedError()

    def snapshot_state(self):
        """
        Return the current state of the aggregate root as a snapshot.
        """
        raise NotImplementedError

    def restore_from_snapshot(self):
        """
        Restore the state of the aggregate root from a snapshot.
        """
        raise NotImplementedError

    def clear_changes(self):
        """
        Clear the list of uncommitted changes.
        """
        self._changes.clear()

    def load_from_history(self, events: List["DomainEvent"]):
        """
        Load the aggregate root's state from a list of domain events.

        Args:
            events (List[DomainEvent]): The list of domain events to load from.
        """
        for event in events:
            self.apply(event)

    def get_uncommitted_changes(self):
        """
        Get the list of uncommitted changes made to the aggregate root.

        Returns:
            List[DomainEvent]: The list of uncommitted changes.
        """
        return self._changes

    def get_version(self):
        """
        Get the current version of the aggregate root.

        Returns:
            int: The current version.
        """
        return self._version

    def set_version(self, version):
        """
        Set the version of the aggregate root.

        Args:
            version (int): The version to set.

        Raises:
            ValueError: If the specified version is less than the current version.
        """
        if version < self._version:
            raise ValueError("Version must be greater than current version")

        self._version = version

    def get_id(self):
        """
        Get the ID of the aggregate root.

        Returns:
            str: The ID.
        """
        return self._id
