# Epics, Features & Scenarios
from typing import List

from domain.feature import Feature


class Epic:
    def __init__(
        self,
        id: str,
        title: str,
        description: str,
        features: List["Feature"],
        status: str,
    ):
        self.id = id
        self.title = title
        self.description = description
        self.features = features
        self.status = status
