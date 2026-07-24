echo "instaling db"
cd apps/automations-hub
uv add --dev alembic
uv run alembic init migrations