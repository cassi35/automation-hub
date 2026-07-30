from shared.registry.manifest import AutomationManifest
manifest = AutomationManifest(
    slug="english-news",
    name="aqui é nome atualizado",
    description="Coleta notícias e gera tarefas no MS To-Do",
    trigger_type="github_actions",
    schedule="30 11 * * *",
)
# esse manifest tira a idea manual do insert into automation
# packages/
#     invoice-reader/

# coloca

# manifest.py

# e acabou.

# O Hub registra sozinho.

# Isso é uma boa arquitetura.