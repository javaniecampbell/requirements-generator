# Will store the abstract classes or interfaces for the repositories to be implemented in the infrastructure layer
from abc import ABC, abstractmethod
from typing import List, Optional, Type

from domain.aggregate_root import AggregateRoot
from domain.event import Event
from domain.requirement import Requirement
from domain.snapshot import Snapshot


class AbstractRepository(ABC):
    """
    Abstract base class for domain repositories.
    """

    @abstractmethod
    def add(self, entity):
        """
        Add a new entity to the repository.
        """
        raise NotImplementedError

    @abstractmethod
    def get(self, id):
        """
        Get an entity from the repository by its ID.
        """
        raise NotImplementedError

    # Add more abstract methods as needed
    @abstractmethod
    def get_events(self) -> List[Event]:
        """
        Retrieves all events from the event store.

        Returns:
            A list of events.
        """
        raise NotImplementedError

    @abstractmethod
    def clear_events(self):
        """
        Clears all events from the event store.
        """
        raise NotImplementedError

    @abstractmethod
    def save_events(
        self, aggregate_id: str, events: List[Event], expected_version: int
    ):
        """
        Saves all events to the event store.
        """
        raise NotImplementedError

    @abstractmethod
    def get_events_for_aggregate(self, aggregate_id: str) -> List["Event"]:
        """
        Retrieves all events for a specific aggregate.

        Args:
            aggregate_id: The ID of the aggregate.

        Returns:
            A list of events for the specified aggregate.
        """
        raise NotImplementedError

    @abstractmethod
    def create_snapshot(self, aggregate_id: str, last_event: Event):
        """
        Creates a snapshot for an aggregate.

        Args:
            aggregate_id: The ID of the aggregate.
            last_event: The last event of the aggregate.

        Raises:
            ValueError: If no aggregate type is registered for the specified ID.
        """
        raise NotImplementedError

    @abstractmethod
    def get_latest_snapshot(self, aggregate_id: str) -> Optional[Snapshot]:
        """
        Retrieves the latest snapshot for an aggregate.

        Args:
            aggregate_id: The ID of the aggregate.

        Returns:
            The latest snapshot for the specified aggregate, or None if no snapshot is found.
        """
        raise NotImplementedError

    @abstractmethod
    def get_snapshots(self) -> List[Snapshot]:
        """
        Retrieves all snapshots from the snapshot store.

        Returns:
            A list of snapshots.
        """
        raise NotImplementedError

    @abstractmethod
    def register_aggregate_type(
        self, aggregate_id: str, aggregate_type: Type[AggregateRoot]
    ):
        """
        Registers an aggregate type for a specific ID.

        Args:
            aggregate_id: The ID of the aggregate.
            aggregate_type: The type of the aggregate.

        Raises:
            ValueError: If an aggregate type is already registered for the specified ID.
        """
        raise NotImplementedError


class RequirementRepository(ABC):
    """
    Abstract base class for the RequirementRepository.
    """

    @abstractmethod
    def add(self, requirement: Requirement):
        raise NotImplementedError

    @abstractmethod
    def get(self, id: int) -> Requirement:
        raise NotImplementedError

    @abstractmethod
    def get_requirements(self, project_details) -> List[Requirement]:
        raise NotImplementedError

    @abstractmethod
    def create_contract(self, requirements: List[Requirement]) -> Contract:
        raise NotImplementedError
