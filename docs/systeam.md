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

# test

subir testes automatizados com tests container depois de u8m pull request em uma branch criada ,
rodar testes ,de db , testes de api ,

1. github actions
2. pytest
3. testsDabtabaseHnalder
4. postgresql temporario
5. alembic upgreade head
6. testes

testes

1. subir PostgreSQL
2. obter URL
3. executar Alembic
4. criar engine
5. entregar engine para os testes
6. destruir PostgreSQL
