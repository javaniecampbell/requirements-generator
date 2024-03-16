# Epics, Features & Scenarios
from typing import List, Optional
from domain.domain_event import DomainEvent
from domain.event_bus import EventBus

from domain.feature import Feature


class Epic:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        features: Optional[List["Feature"]],
        status: str,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.features = [] if features is None else features
        self.status = status  # "To Do", "In Progress", "Done"

    def add_feature(self, feature: Feature):
        self.features.append(feature)
        #  considering moving into a separate aggregate class called EpicAggregate
        EventBus.publish(
            DomainEvent("FeatureAdded", {"epic": self.title, "feature": feature.title})
        )
        print(f"Domain Event: Feature '{feature.title}' added to Epic '{self.title}'")
