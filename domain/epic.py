# Epics, Features & Scenarios
from typing import List, Optional
from domain.domain_event import DomainEvent
from domain.event_bus import EventBus

from domain.feature import Feature


class Epic:
    """
    Represents an epic, which is a large user story or a collection of related user stories.
    """

    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        features: Optional[List["Feature"]],
        status: str,
    ):
        """
        Initializes a new instance of the Epic class.

        Args:
            id (str): The unique identifier of the epic.
            title (str): The title of the epic.
            description (str): The description of the epic.
            features (Optional[List[Feature]]): The list of features associated with the epic.
            status (str): The status of the epic. Can be one of "To Do", "In Progress", or "Done".
        """
        self.id = id
        self.title = title
        self.description = description
        self.features = [] if features is None else features
        self.status = status  # "To Do", "In Progress", "Done"

    def add_feature(self, feature: Feature):
        """
        Adds a feature to the epic.

        Args:
            feature (Feature): The feature to be added.
        """
        self.features.append(feature)
        #  considering moving into a separate aggregate class called EpicAggregate
        EventBus.publish(
            DomainEvent("FeatureAdded", {"epic": self.title, "feature": feature.title})
        )
        print(f"Domain Event: Feature '{feature.title}' added to Epic '{self.title}'")
