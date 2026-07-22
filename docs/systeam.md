# objetivo

estrtura systeam

# rodar fastapi

```
# /etc/systemd/system/automations-platform.service
[Unit]
Description=Automations Platform
Requires=docker.service
After=docker.service

[Service]
Type=oneshot
RemainAfterExit=true
WorkingDirectory=/home/cassiano/automations-platform/infra
ExecStart=/usr/bin/docker compose up -d
ExecStop=/usr/bin/docker compose down

[Install]
WantedBy=multi-user.target
```

# comando

> systemctl enable --now automations-platform.service

# docker compose

1. template

```
# infra/docker-compose.yml
services:
  postgres:
    image: postgres:16-alpine
    environment:
      POSTGRES_USER: automations
      POSTGRES_PASSWORD: ${DB_PASSWORD}
      POSTGRES_DB: automations_hub
    volumes:
      - pgdata:/var/lib/postgresql/data
    ports:
      - "5432:5432"   # só no ambiente local/dev; em produção, tira essa linha (fica só interno)

volumes:
  pgdata:
```

1. inicializar docker file
2. automatizzar com docker compose
