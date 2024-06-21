# domain/models.py
from dataclasses import dataclasses
from typing import List

from domain.requirement import Requirement


@dataclasses
class Contract:
    def __init__(self, requirements: List[Requirement]):
        self.requirements = requirements
        # Add other contract-related attributes as needed


# Create a contract from the requirements
# contract = Contract(requirements)
