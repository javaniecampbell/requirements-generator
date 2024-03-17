from typing import List

from domain.domain_event import DomainEvent


class AggregateRoot:
    def __init__(self, id):
        self._id = id
        self._domain_events: List["DomainEvent"] = []

    def add_domain_event(self, event):
        self._domain_events.append(event)

    def clear_domain_events(self):
        self._domain_events.clear()

    def get_domain_events(self):
        return self._domain_events
