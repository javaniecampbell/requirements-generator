from datetime import datetime
from typing import List, Any, Optional


class Event:
    def __init__(self,  type: str, data: Any, timestamp: datetime = datetime.now(), aggregate_id: Optional[str] = None):
        self.type = type
        self.data = data
        self.timestamp = timestamp
        self.aggregate_id = aggregate_id
