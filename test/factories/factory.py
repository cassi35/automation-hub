from shared.db.entities.automation import AutomationModel

def make_automation(slug: str, **overrides) -> AutomationModel:
    defaults = {
        "slug": slug,
        "name": slug,
        "trigger": "system",
        "status": "active",
    }
    defaults.update(overrides)
    return AutomationModel(**defaults)