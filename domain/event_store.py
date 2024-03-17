from typing import List
from domain.event import Event
from domain.snapshot import Snapshot


class EventStore:
    def __init__(self):
        self._events: List["Event"] = []
        self._snapshots: List["Snapshot"] = []

    def add_event(self, event: Event):
        self._events.append(event)

    def get_events(self) -> List[Event]:
        return self._events

    def save_events(
        self, aggregate_id: str, events: List[Event], expected_version: int
    ):
        if events:
            last_event = events[-1]
            current_version = self._get_current_version(aggregate_id)
            if expected_version != current_version:
                raise Exception(
                    f"Concurrency error, expected version {expected_version} but got {current_version}. Concurrency conflict detected; incorrect version of the aggregate"
                )
            self._events.extend(events)
            if(current_version + len(events)) % 5 == 0: # Snapshot every 5 events
                self.create_snapshot(aggregate_id, last_event)

    def get_events_for_aggregate(self, aggregate_id: str) -> List["Event"]:
        return [event for event in self._events if event.aggregate_id == aggregate_id]
    
    def _get_current_version(self, aggregate_id: str) -> int:
        if(self._events):
            related_events = self.get_events_for_aggregate(aggregate_id)
            if(related_events):
                return related_events[-1].version
        
        return 0
    
    def create_snapshot(self, aggregate_id: str, last_event: Event):
        aggregate = rebuild_aggregate(self, aggregate_id,upto_version=last_event.version)
        snapshot = Snapshot(aggregate_id, last_event.version, aggregate)
        self._snapshots.append(snapshot)


# Usage
# event_store = EventStore()
# event_store.add_event(Event("UserRegistered", {"user_id": "1234"}))
# events = event_store.get_events()
# for event in events:
#     print(f"Event Type: {event.type}, Data: {event.data}, Timestamp: {event.timestamp}")
