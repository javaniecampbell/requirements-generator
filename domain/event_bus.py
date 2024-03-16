from typing import List, Callable

from domain.domain_event import DomainEvent


class EventBus:
    _subscribers: List[Callable] = []

    @classmethod
    def subscribe(cls, event_handler: Callable):
        cls._subscribers.append(event_handler)

    @classmethod
    def publish(cls, event: DomainEvent):
        for handler in cls._subscribers:
            handler(event)
