echo "instaling db"
cd apps/automations-hub
uv add --dev alembic
uv run alembic init migrations
echo "configurar models"
uv run alembic revision --autogenerate -m "cria tabelas automation, executions, steps, metrics"
uv run alembic upgrade head # aplica pro nneon