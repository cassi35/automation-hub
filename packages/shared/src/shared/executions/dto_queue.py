from dataclasses import dataclass
from typing import Any


@dataclass
class ExecutionEvent:
    operation: str
    args: tuple[Any, ...]