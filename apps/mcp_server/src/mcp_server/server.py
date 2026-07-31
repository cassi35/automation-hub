from fastmcp import FastMCP
from contextlib import asynccontextmanager
from rich import print
@asynccontextmanager
async def lifespan(app: FastMCP):
    print(f"[green]Starting up...[/green]")
    yield
    print(f"[green]Shutting down...[/green]")
mcp = FastMCP(
    name="FreeCodeCamp Feed Searcher",
    version="0.1.0",
    lifespan=lifespan
)
import mcp_server.tools.automation
def main()-> None:
    mcp.run() 

