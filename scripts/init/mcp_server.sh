#!/bin/bash
echo "initing mcp server"
cd apps
mkdir mcp_server && cd mcp_server
uv init --package .
echo "adcinando dependencias"
uv add fastmcp 
uv add rich uvicorn
echo "criando arquitetura"
cd src/mcp_server
mkdir tools services
cd ../..