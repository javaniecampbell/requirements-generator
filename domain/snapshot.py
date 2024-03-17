class Snapshot:
    """
    Represents a snapshot of the state of an aggregate.

    Attributes:
        aggregate_id (str): The unique identifier of the aggregate.
        version (int): The version number of the snapshot.
        state: The state of the aggregate at the time of the snapshot.
    """

    def __init__(self, aggregate_id: str, version: int, state):
        """
        Initializes a new Snapshot object.

        Args:
            aggregate_id (str): The ID of the aggregate.
            version (int): The version number of the snapshot.
            state: The state of the aggregate at the time of the snapshot.
        """
        self.aggregate_id = aggregate_id
        self.version = version
        self.state = state
