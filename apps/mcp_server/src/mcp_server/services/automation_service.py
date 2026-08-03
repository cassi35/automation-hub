from shared.db.settings.connection import BDConnectionHandler
from shared.db.entities.automation import AutomationModel
from mcp_server.dto.automation import AutomationDTO
class AutomationService:
    def __init__(self):
        pass
    def get_all_automation(self) -> list[AutomationDTO]:

        with BDConnectionHandler() as db:
            automations = (
                db.session
                .query(AutomationModel)
                .all()
            )

            return [
                AutomationDTO(
                    id=a.id,
                    slug=a.slug,
                    name=a.name,
                    status=a.status,
                    trigger=a.trigger,
                    description=""
                )
                for a in automations
            ]
    def get_automation_by_slug(self,slug:str)->AutomationDTO | None:
        with BDConnectionHandler() as db:
            automation = db.session.query(AutomationModel).filter_by(slug=slug).first()
            if automation is None:
                return None
            return AutomationDTO(
                id=automation.id,
                slug=automation.slug,
                name=automation.name,
                status=automation.status,
                trigger=automation.trigger,
                description=""
            )