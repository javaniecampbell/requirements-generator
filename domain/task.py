class Task:
    def __init__(self, description: str, parent_user_story_id: str):
        self.description = description
        self.completed = False
        self.parent_user_story_id = parent_user_story_id

    def complete_task(self):
        self.completed = True
