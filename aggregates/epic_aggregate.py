# aggregates/epic_aggregate.py

from domain.aggregate_root import AggregateRoot
from domain.domain_event import DomainEvent
from domain.epic import Epic
from domain.feature import Feature
from domain.user_story import UserStory
from domain.task import Task
from domain.scenario import Scenario


class EpicAggregate(AggregateRoot):

    def __init__(self, epic_id, title, desc):
        super().__init__(epic_id)
        self.epic = Epic(epic_id, title, desc)

    def add_feature(self, feature_id, title, desc):
        feature = Feature(feature_id, title, desc)
        self.epic.features.append(feature)

        self.add_domain_event(
            DomainEvent(
                "FeatureAdded", {"epic_id": self.epic.id, "feature_id": feature_id}
            )
        )

    def add_user_story(self, feature_id, story_id, title, desc):
        feature = next(f for f in self.epic.features if f.id == feature_id)
        story = UserStory(story_id, title, desc)
        feature.user_stories.append(story)

        self.add_domain_event(
            DomainEvent(
                "UserStoryAdded",
                {
                    "epic_id": self.epic.id,
                    "feature_id": feature_id,
                    "story_id": story_id,
                },
            )
        )

    # Similarly add methods for Task, Scenario
