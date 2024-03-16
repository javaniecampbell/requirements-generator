# User Stories
from typing import List, Optional


class UserStory:
    def __init__(
        self,
        id: str,
        title: str,
        as_a: str,
        i_want: str,
        so_that: str,
        acceptance_criteria: Optional[List[str]],
        parent_feature_id: str,
        status: str,
    ):
        self.id = id
        self.title = title
        self.as_a = as_a
        self.i_want = i_want
        self.so_that = so_that
        self.acceptance_criteria = [] if acceptance_criteria is None else acceptance_criteria
        self.parent_feature_id = parent_feature_id
        self.status = status
    
    def define_acceptance_criteria(self, criteria):
        self.acceptance_criteria.append(criteria)
