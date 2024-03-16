# Epics, Features & Scenarios
from typing import List, Optional

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
        self.status = status
    
    def add_feature(self, feature: Feature):
        self.features.append(feature)
