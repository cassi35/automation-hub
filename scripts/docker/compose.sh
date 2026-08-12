#!/bin/bash
echo "trocando context"
docker context use default
echo "rodando compose"
docker compose up --build