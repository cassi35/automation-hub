from dataclasses import dataclass
from datetime import datetime

@dataclass
class Step:
    id:int
    name:str
    status:str
    execution_id:int