from datetime import datetime
from typing import List, Any


class Event:
    def __init__(self, type: str, data: Any, timestamp: datetime = datetime.now()):
        self.type = type
        self.data = data
        self.timestamp = timestamp
