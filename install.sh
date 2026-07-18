#!/bin/bash
echo "Installing uv..."
uv init 
mkdir ./vscode
echo "
> {
    "prisma.pinToPrisma6": true,
    "editor.formatOnSave": true,
  "editor.defaultFormatter": "esbenp.prettier-vscode",
  "editor.codeActionsOnSave": {
    "source.fixAll.eslint": "explicit"
  }
}" > settings.json 
 mv settings.json ./vscode/
 mkdir -p ./github/workflows
 touch .env 
echo "Installing uv dependencies..."
uv add prompt-toolkit psutil selenium fastmcp 