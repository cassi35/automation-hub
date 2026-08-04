from shared.db.settings.connection import BDConnectionHandler
from shared.db.entities.automation import AutomationModel
from automations_hub.domain.automation import Automation
from shared.registry.manifest import AutomationManifest
from automations_hub.infra.db import get_database
class AutomationRepository:
    def __init__(self):
        self._db_factory = get_database
    def upsert_automation(self,manifest:AutomationManifest)->Automation:
        with self._db_factory() as db:

            automation = (
                db.session.query(AutomationModel)
                .filter_by(slug=manifest.slug)
                .first()
            )
            if automation:
                automation.name = manifest.name
                automation.description = manifest.description
                automation.trigger = manifest.trigger_type

            else:
                automation = AutomationModel(
                    slug=manifest.slug,
                    name=manifest.name,
                    description=manifest.description,
                    trigger=manifest.trigger_type,
                    status="active",
                )

                db.session.add(automation)

            db.session.commit()
            db.session.refresh(automation)

            return Automation(
                id=automation.id,
                slug=automation.slug,
                name=automation.name,
                status=automation.status,
                trigger_type=automation.trigger,
            )
    def get_by_slug(self, slug: str) -> Automation | None:
        with self._db_factory() as db:
            automation = (
                db.session
                .query(AutomationModel)
                .filter_by(slug=slug)
                .first()
            )

            if automation is None:
                return None

            return Automation(
                id=automation.id,
                slug=automation.slug,
                name=automation.name,
                status=automation.status,
                trigger_type=automation.trigger,
            )
