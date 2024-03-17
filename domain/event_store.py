from typing import List
from domain.event import Event


class EventStore:
    def __init__(self):
        self._events: List["Event"] = []

    def add_event(self, event: Event):
        self._events.append(event)

    def get_events(self) -> List[Event]:
        return self._events

    def save_events(
        self, aggregate_id: str, events: List[Event], expected_version: int
    ):
        self._events.extend(events)

    def get_events_for_aggregate(self, aggregate_id: str) -> List["Event"]:
        return [event for event in self._events if event.aggregate_id == aggregate_id]


# Usage
# event_store = EventStore()
# event_store.add_event(Event("UserRegistered", {"user_id": "1234"}))
# events = event_store.get_events()
# for event in events:
#     print(f"Event Type: {event.type}, Data: {event.data}, Timestamp: {event.timestamp}")
