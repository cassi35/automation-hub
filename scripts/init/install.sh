#!/bin/bash
echo "ativando ambiente virtual"
chmod +x scripts/init/arquitecture.sh
./scripts/init/arquitecture.sh
echo "beging instalation..."
echo "instaling apps"
chmod +x scripts/init/apps.sh
./scripts/init/apps.sh
echo "instalacao finalizada"