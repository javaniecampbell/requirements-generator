from typing import Dict, List, Optional, Type
from multipledispatch import dispatch

from domain.aggregate_root import AggregateRoot
from domain.event import Event
from domain.snapshot import Snapshot


class EventStore:
    """
    Represents an event store that stores and retrieves events for aggregates.
    """

    def __init__(self):
        self._events: List["Event"] = []
        self._snapshots: List["Snapshot"] = []
        # self._snapshot_interval = 5
        self._aggregate_types: Dict[str, Type[AggregateRoot]] = ({}) # New mapping of aggregate ID to type

    def add_event(self, event: Event):
        """
        Adds an event to the event store.

        Args:
            event: The event to be added.
        """
        self._events.append(event)

    def get_events(self) -> List[Event]:
        """
        Retrieves all events from the event store.

        Returns:
            A list of events.
        """
        return self._events

    def save_events(
        self, aggregate_id: str, events: List[Event], expected_version: int
    ):
        """
        Saves a list of events for a specific aggregate.

        Args:
            aggregate_id: The ID of the aggregate.
            events: The list of events to be saved.
            expected_version: The expected version of the aggregate.

        Raises:
            Exception: If a concurrency conflict is detected.
        """
        if events:
            last_event = events[-1]
            current_version = self._get_current_version(aggregate_id)
            if expected_version != current_version:
                raise Exception(
                    f"Concurrency error, expected version {expected_version} but got {current_version}. Concurrency conflict detected; incorrect version of the aggregate"
                )
            for event in events:
                event.version = current_version + 1  # Increment event version
                self._events.append(event)
                current_version += 1
            if (current_version + len(events)) % 5 == 0:  # Snapshot every 5 events
                self.create_snapshot(aggregate_id, last_event)

    def get_events_for_aggregate(self, aggregate_id: str) -> List["Event"]:
        """
        Retrieves all events for a specific aggregate.

        Args:
            aggregate_id: The ID of the aggregate.

        Returns:
            A list of events for the specified aggregate.
        """
        return [event for event in self._events if event.aggregate_id == aggregate_id]

    def _get_current_version(self, aggregate_id: str) -> int:
        """
        Retrieves the current version of an aggregate.

        Args:
            aggregate_id: The ID of the aggregate.

        Returns:
            The current version of the aggregate.
        """
        if self._events:
            related_events = self.get_events_for_aggregate(aggregate_id)
            if related_events:
                return related_events[-1].version

        return 0

    def create_snapshot(self, aggregate_id: str, last_event: Event):
        """
        Creates a snapshot for an aggregate.

        Args:
            aggregate_id: The ID of the aggregate.
            last_event: The last event of the aggregate.

        Raises:
            ValueError: If no aggregate type is registered for the specified ID.
        """
        aggregate_type = self._aggregate_types.get(aggregate_id)
        if not aggregate_type:
            raise ValueError(f"No aggregate type registered for ID {aggregate_id}")

        aggregate = rebuild_aggregate(
            self, aggregate_type, aggregate_id, upto_version=last_event.version
        )
        snapshot = Snapshot(
            aggregate_id, last_event.version, aggregate.snapshot_state()
        )  # Assuming snapshot_state returns the state
        self._snapshots.append(snapshot)

    def get_latest_snapshot(self, aggregate_id: str) -> Optional[Snapshot]:
        """
        Retrieves the latest snapshot for an aggregate.

        Args:
            aggregate_id: The ID of the aggregate.

        Returns:
            The latest snapshot for the specified aggregate, or None if no snapshot is found.
        """
        snapshots = [
            snapshot
            for snapshot in self._snapshots
            if snapshot.aggregate_id == aggregate_id
        ]
        if snapshots:
            return max(snapshots, key=lambda s: s.version)
        return None

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
        if aggregate_id in self._aggregate_types:
            raise ValueError(
                f"Aggregate type for ID {aggregate_id} is already registered."
            )
        self._aggregate_types[aggregate_id] = aggregate_type


# Event sourcing helpers


@dispatch(EventStore, type, str)
def rebuild_aggregate(
    event_store: EventStore, aggregate_class: type, aggregate_id: str
):
    """
    Rebuilds an aggregate by loading its history of events from the event store.

    Args:
        event_store (EventStore): The event store used to retrieve events.
        aggregate_class (type): The class of the aggregate to rebuild.
        aggregate_id (str): The ID of the aggregate to rebuild.

    Returns:
        AggregateRoot: The rebuilt aggregate.

    Raises:
        ValueError: If the aggregate class does not inherit from AggregateRoot.
    """
    if not issubclass(aggregate_class, AggregateRoot):
        raise ValueError("Aggregate class must inherit from AggregateRoot.")

    aggregate = aggregate_class(aggregate_id)
    events = event_store.get_events_for_aggregate(aggregate_id)
    aggregate.load_from_history(events)
    return aggregate


@dispatch(EventStore, type, str, int)
def rebuild_aggregate(event_store, aggregate_class, aggregate_id, upto_version=None):
    """
    Rebuilds an aggregate by applying events from the event store.

    Args:
        event_store (EventStore): The event store containing the events.
        aggregate_class (type): The class of the aggregate to rebuild.
        aggregate_id (str): The ID of the aggregate to rebuild.
        upto_version (int, optional): The maximum version of events to apply. Defaults to None.

    Returns:
        AggregateRoot: The rebuilt aggregate.

    Raises:
        ValueError: If the aggregate class does not inherit from AggregateRoot.
    """
    if not issubclass(aggregate_class, AggregateRoot):
        raise ValueError("Aggregate class must inherit from AggregateRoot.")

    snapshot = event_store.get_latest_snapshot(aggregate_id)
    if snapshot:
        aggregate = aggregate_class(aggregate_id)
        aggregate.restore_from_snapshot(snapshot)
        starting_version = snapshot.version
    else:
        aggregate = aggregate_class(aggregate_id)
        starting_version = 0

    events = event_store.get_events_for_aggregate(
        aggregate_id, after_version=starting_version
    )
    for event in events:
        if upto_version is not None and event.version > upto_version:
            break
        aggregate.apply(event)

    return aggregate


# Usage
# event_store = EventStore()
# event_store.add_event(Event("UserRegistered", {"user_id": "1234"}))
# events = event_store.get_events()
# for event in events:
#     print(f"Event Type: {event.type}, Data: {event.data}, Timestamp: {event.timestamp}")

# # Register the BankAccount aggregate type
# # Initialize the EventStore
# event_store = EventStore()

# # Register a BankAccount aggregate type for a specific aggregate ID
# event_store.register_aggregate_type("123", BankAccount)

# # Assume you have a BankAccount instance with ID "123" and some events applied to it
# # bank_account.apply(AccountCreated("123", "John Doe"))
# # bank_account.apply(MoneyDeposited("123", 100))

# # Add events to the EventStore
# event_store.add_event(AccountCreated("123", "John Doe"))
# event_store.add_event(MoneyDeposited("123", 100))

# # The EventStore can now create a snapshot for the BankAccount with ID "123"
# last_event = MoneyDeposited("123", 100)  # Assuming this is the last event applied
# event_store.create_snapshot("123", last_event)

# # The snapshot for the BankAccount with ID "123" is now stored in the EventStore
