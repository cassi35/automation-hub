from dataclasses import dataclass


@dataclass
class AutomationDTO:
    id: int
    slug: str
    name: str
    status: str
    trigger: str
    description: str
    status: str