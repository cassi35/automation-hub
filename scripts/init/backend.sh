#!/bin/bash
echo "init installing backend..."
cd apps 
mkdir automations-hub && cd automations-hub
uv init --package .
echo "adicinado dependencias"
uv add fastapi uvicorn[standard] sqlalchemy psycopg2-binary python-dotenv feedparser prompt-toolkit scrapy pytest
echo "crinado arquitetura do backend"
cd src
mkdir domain services infra
cd ../..