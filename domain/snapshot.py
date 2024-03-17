class Snapshot:
    def __init__(self, aggregate_id: str, version: int, state):
        self.aggregate_id = aggregate_id
        self.version = version
        self.state = state
