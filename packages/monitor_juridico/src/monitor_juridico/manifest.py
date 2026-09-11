from shared.registry.manifest import AutomationManifest
manifest = AutomationManifest(
    slug="monitor-juridico",
    name="Monitor Jurídico",
    description="Monitora novas comunicações e intimações através da API pública do CNJ e identifica publicações ainda não registradas.",
    trigger_type="github_actions",
    schedule="*30 11 * * *",
)
# esse manifest tira a idea manual do insert into automation
# packages/
#     invoice-reader/

# coloca

# manifest.py

# e acabou.

# O Hub registra sozinho.

# Isso é uma boa arquitetura.