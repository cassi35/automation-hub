echo "atiavando ambiente virtual"
uv init --package .
echo "
[tool.uv.workspace]
members = ["apps/*", "packages/*"]
" >> pyproject.toml
echo "criando pastas"
mkdir -p apps packages
mkdir systemd
uv init --package packages/shared
uv sync --all-packages
uv add --dev pytest ruff
mkdir -p infra/docker 
cd infra/docker
touch Dockerfile.api docker-compose.yml
cd ../..
mkdir -p .github/workflows
echo "finalizando criacao de pastas"