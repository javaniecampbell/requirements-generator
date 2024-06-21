# Example of extending AggregateRoot
from domain.aggregate_root import AggregateRoot
from domain.domain_event import DomainEvent
from domain.epic import Epic
from domain.feature import Feature
from domain.project import Project
from domain.requirement import Requirement
from domain.scenario import Scenario
from domain.task import Task
from domain.user_story import UserStory

# Aggregates should ensure the underlying domain models are valid before publishing domain events, should handle domain events and subscription to domain events


class ProjectAggregate(AggregateRoot):
    """
    Represents a project aggregate.

    Attributes:
        id (str): The unique identifier of the project.
        name (str): The name of the project.
    """

    def __init__(self, id, name):
        """
        Initializes a new instance of the ProjectAggregate class.

        Args:
            id (int): The ID of the project.
            name (str): The name of the project.
        """
        super().__init__(id)
        self.project = Project(id, name)

        # Additional project-specific initialization

    # Project-specific methods
    def add_epic(self, epic_id, epic_title, epic_desc):
        epic = Epic(epic_id, epic_title, epic_desc)
        self.project.epics.append(epic)
        self.add_domain_event(
            DomainEvent("EpicAdded", {"epic_id": epic_id, "epic_title": epic_title})
        )

    def add_feature(self, epic_id, feature_id, feature_title, feature_desc):
        epic = next(epic for epic in self.project.epics if epic.id == epic_id)
        feature = Feature(feature_id, feature_title, feature_desc, epic.id)
        epic.add_feature(feature)
        self.add_domain_event(
            DomainEvent("FeatureAdded", {"epic_id": epic_id, "feature_id": feature_id})
        )

    def add_user_story(self, epic_id, feature_id, user_story_id, title, details):
        epic = next(epic for epic in self.project.epics if epic.id == epic_id)
        feature = next(f for f in epic.features if f.id == feature_id)

        user_story = UserStory(
            id=user_story_id, title=title, details=details, feature_id=feature_id
        )

        feature.user_stories.append(user_story)

        self.add_domain_event(
            DomainEvent(
                "UserStoryAdded",
                {
                    "epic_id": epic_id,
                    "feature_id": feature_id,
                    "user_story_id": user_story_id,
                },
            )
        )

    def add_task(self, user_story_id, task_id, description):
        user_story = next(us for us in self.user_stories if us.id == user_story_id)

        task = Task(id=task_id, description=description)
        user_story.tasks.append(task)

        self.add_domain_event(
            DomainEvent(
                "TaskAdded", {"user_story_id": user_story_id, "task_id": task_id}
            )
        )

    def complete_task(self, user_story_id, task_id):
        # Lookup user story and task
        user_story = next(us for us in self.user_stories if us.id == user_story_id)

        task = next(t for t in self.user_stories)
        task.complete()

        self.add_domain_event(
            DomainEvent(
                "TaskCompleted", {"user_story_id": user_story_id, "task_id": task_id}
            )
        )

    def add_scenario(self, feature_id, scenario_id, title, steps):
        feature = next(f for f in self.features if f.id == feature_id)

        scenario = Scenario(id=scenario_id, title=title, steps=steps)
        feature.scenarios.append(scenario)

        self.add_domain_event(
            DomainEvent(
                "ScenarioAdded", {"feature_id": feature_id, "scenario_id": scenario_id}
            )
        )

    def add_requirement(self, feature_id, req_id, type, text):
        feature = next(f for f in self.features if f.id == feature_id)

        requirement = Requirement(id=req_id, type=type, text=text)
        feature.requirements.append(requirement)

        self.add_domain_event(
            DomainEvent(
                "RequirementAdded", {"feature_id": feature_id, "requirement_id": req_id}
            )
        )
