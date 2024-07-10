from abc import ABC, abstractmethod

class ValueObject(ABC):
    @abstractmethod
    def __eq__(self, other):
        pass

class CustomerId(ValueObject):
    def __init__(self, id):
        self.id = id

    def __eq__(self, other):
        if isinstance(other, CustomerId):
            return self.id == other.id
        return False
