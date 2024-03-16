# Domain Events
class DomainEvent:
    def __init__(self, name, data):
        self.name = name
        self.data = data
