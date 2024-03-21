# Project Models

Outlined below are some core classes that could be used to several work item types in a project management system. The classes are designed to be reusable across projects.

## Epic

The Epic class represents a large body of work that can be broken down into smaller stories. It acts as a container for related stories.

- name (str): The name of the epic
- description (str): A long description of the epic
- stories (List[Story]): The stories associated with this epic

```python
epic = Epic('Customer profiles', 'Includes all functionality related to customer profiles and accounts')
epic.add_story(story1)
epic.add_story(story2)
```

## Task

The Task class represents a single unit of work to be completed. Tasks can be associated with stories and epics.

- name (str): The short name of the task
- description (str): Longer description of the task
- status (str): The current status of the task (todo, in progress, done)
- effort (int): The estimated effort in hours
- assignee (str): The person this task is assigned to

```python
task = Task('Fix login bug', 'Debug issue with login redirect', effort=4, assignee='Mary')
task.complete()
```

## Feature

The Feature class represents a shippable capability or end-user functionality. Features consist of related stories and tasks.

- name (str): The name of the feature
- description (str): Longer description
- status (str): The development status (ideas, dev, testing, - done)
- stories (List[Story]): Stories related to this feature

```python
feature = Feature('Profiles', 'User profiles and account management')
feature.add_story(story1)
feature.add_story(story2)
```

## Project

The Project class represents a software project and tracks features.

- name (str): Name of the project
- features (List[Feature]): Features planned for this project

```python
project = Project('Customer Portal')
project.add_feature(profiles_feature)
project.add_feature(billing_feature)
```

## Requirement

The Requirement class represents a capability or feature the system must have.

- title (str): Short title/name of requirement
- description (str): Longer description with details
- priority (str): Priority level (high/medium/low)
- status (str): Current status of requirement (proposed/approved/implemented)

```python
req = Requirement('Export reports', 'Allow exporting data to CSV/PDF')
req.priority = 'high'
req.status = 'approved'
```

## Scenario

The Scenario class represents a specific workflow or user journey.

- title (str): Title summarizing the scenario
- description (str): Details of the scenario
- steps (List[Step]): The sequence of steps/actions

```python
scenario = Scenario('User login', 'Details of user logging in')
scenario.add_step('User goes to login page')
scenario.add_step('User enters credentials')
scenario.add_step('User is redirected to dashboard')
```

## User Story

The UserStory class represents a user-centric feature or requirement.

- title (str): Short summary of the story
- description (str): More details on the story
- priority (str): Priority level (high/medium/low)
- points (int): Story points estimating complexity
- status (str): Current status (todo, in progress, done)

```python
story = UserStory('User login', 'As a user I want to login')
story.priority = 'high'
story.points = 3
story.status = 'done'

```
