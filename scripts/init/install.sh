#!/bin/bash
echo "beging instalation..."
echo "instaling apps"
chmod +x scripts/init/apps.sh
./scripts/init/apps.sh
echo "instaling dependencies"
chmod +x scripts/init/dependencies.sh
./scripts/init/dependencies.sh
