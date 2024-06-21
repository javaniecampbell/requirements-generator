from typing import Protocol

from domain.feature import Feature


class FeatureRepository(Protocol):
  def get(self, epic_id: int) -> "Feature": ...
