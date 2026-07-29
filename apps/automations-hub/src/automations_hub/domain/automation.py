from dataclasses import dataclass

@dataclass
class Automation:
    id: int
    slug: str
    name: str
    status: str
    trigger_type: str
    def can_start_execution(self) -> bool:
        return self.status == "active"   # regra de negócio pura, sem SQL