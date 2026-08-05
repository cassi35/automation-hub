from mcp_server.server import mcp
import httpx
@mcp.tool(
        name="mcp_endpoints",
        description="testa endpoints",
)
@mcp.tool()
async def test_endpoint(
    method: str,
    url: str,
    body: dict | None = None,
) -> dict:
    """
    Testa um endpoint HTTP e retorna status e resposta.
    """

    async with httpx.AsyncClient() as client:
        response = await client.request(
            method=method,
            url=url,
            json=body,
        )

    return {
        "status_code": response.status_code,
        "headers": dict(response.headers),
        "body": response.json()
        if response.headers.get("content-type", "").startswith("application/json")
        else response.text,
    }