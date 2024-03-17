from typing import Dict, List, Optional, Type
from domain.aggregate_root import AggregateRoot
from domain.event import Event
from domain.eventsourcing_helpers import rebuild_aggregate
from domain.snapshot import Snapshot


class EventStore:
    def __init__(self):
        self._events: List["Event"] = []
        self._snapshots: List["Snapshot"] = []
        # self._snapshot_interval = 5
        self._aggregate_types: Dict[str, Type[AggregateRoot]] = (
            {}
        )  # New mapping of aggregate ID to type

    def add_event(self, event: Event):
        self._events.append(event)

    def get_events(self) -> List[Event]:
        return self._events

    def save_events(
        self, aggregate_id: str, events: List[Event], expected_version: int
    ):
        if events:
            last_event = events[-1]
            current_version = self. (aggregate_id)
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
        return [event for event in self._events if event.aggregate_id == aggregate_id]

    def _get_current_version(self, aggregate_id: str) -> int:
        if self._events:
            related_events = self.get_events_for_aggregate(aggregate_id)
            if related_events:
                return related_events[-1].version

        return 0

    def create_snapshot(self, aggregate_id: str, last_event: Event):
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
        snapshots = [
            snapshot
            for snapshot in self._snapshots
            if snapshot.aggregate_id == aggregate_id
        ]
        if snapshots:
            return max(snapshots, key=lambda s: s.version)
        return None
    
    def register_aggregate(self, aggregate_id: str, aggregate_type: Type[AggregateRoot]):
        if aggregate_id in self._aggregate_types:
            raise ValueError(f"Aggregate type for ID {aggregate_id} is already registered.")
        self._aggregate_types[aggregate_id] = aggregate_type


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
