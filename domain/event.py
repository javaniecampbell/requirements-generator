from datetime import datetime
from typing import List, Any, Optional


from typing import Any, Optional
from datetime import datetime


class Event:
    """
    Represents an event in the system.

    Attributes:
        type (str): The type of the event.
        data (Any): The data associated with the event.
        timestamp (datetime): The timestamp when the event occurred. Defaults to the current datetime.
        aggregate_id (Optional[str]): The ID of the aggregate associated with the event. Defaults to None.
        version (Optional[int]): The version of the event. Defaults to None.
    """

    def __init__(
        self,
        type: str,
        data: Any,
        timestamp: datetime = datetime.now(),
        aggregate_id: Optional[str] = None,
    ):
        """
        Initialize a new Event object.

        Args:
            type (str): The type of the event.
            data (Any): The data associated with the event.
            timestamp (datetime, optional): The timestamp of the event. Defaults to the current datetime.
            aggregate_id (str, optional): The ID of the aggregate associated with the event. Defaults to None.
        """
        self.type = type
        self.data = data
        self.version: Optional[int] = None
        self.timestamp = timestamp
        self.aggregate_id = aggregate_id
