#!/bin/bash
echo "instaling frontend"
chmod +x scripts/init/frontend.sh
echo "instaling frontend"
./scripts/init/frontend.sh
echo "instaling backend"
chmod +x scripts/init/backend.sh
./scripts/init/backend.sh