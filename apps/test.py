import os
os.environ["DATABASE_URL"] = (
    "postgresql://postgres:postgres@localhost:5432/postgres"
)
from shared.config.config import Config
print(Config.DATABASE_URL)