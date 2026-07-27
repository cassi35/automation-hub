from shared.registry.manifest import AutomationManifest
manifest = AutomationManifest(
    slug="english-news",
    name="English News",
    description="Coleta notícias e gera tarefas no MS To-Do",
    trigger_type="github_actions",
    schedule="30 11 * * *",
)