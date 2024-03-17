from typing import List, Callable

from domain.domain_event import DomainEvent


class EventBus:
    """
    A simple event bus implementation that allows subscribing to and publishing events.
    """

    _subscribers: List[Callable] = []

    @classmethod
    def subscribe(cls, event_handler: Callable):
        """
        Subscribe a callable event handler to the event bus.

        Args:
            event_handler (Callable): The event handler function to be subscribed.

        """
        cls._subscribers.append(event_handler)

    @classmethod
    def publish(cls, event: DomainEvent):
        """
        Publish an event to all the subscribed event handlers.

        Args:
            event (DomainEvent): The event to be published.

        """
        for handler in cls._subscribers:
            handler(event)
