from typing import List

from domain.domain_event import DomainEvent


class AggregateRoot:
    def __init__(self, id: str):
        self._id = id
        self._version = 0
        self._changes: List["DomainEvent"] = []
        self._domain_events: List["DomainEvent"] = []

    def add_domain_event(self, event: DomainEvent):
        self._domain_events.append(event)

    def clear_domain_events(self):
        self._domain_events.clear()

    def get_domain_events(self):
        return self._domain_events
    
    def apply(self, event: DomainEvent):
        # self.add_domain_event(event)
        self._changes.append(event)
        self.apply_event(event)
    
    def handle(self, event: DomainEvent):
        """This method will be overridden by derived aggregates to handle specific event types."""
        raise NotImplementedError()
    
    def clear_changes(self):
        self._changes.clear()

    def load_from_history(self, events:List["DomainEvent"]):
        for event in events:
            self.handle(event)
            self._version = event.version # Update the version to the event's version

