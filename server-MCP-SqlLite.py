import sqlite3, json, asyncio
from mcp.server import Server
from mcp.server.stdio import stdio_server
from mcp import types

app = Server("sqlite-server")

def run_sql(sql, params=()):
    conn = sqlite3.connect("school.db")
    conn.row_factory = sqlite3.Row
    cur = conn.cursor()
    cur.execute(sql, params)
    rows = cur.fetchall()
    conn.close()
    return [dict(r) for r in rows]

@app.list_tools()
async def list_tools():
    return [
        types.Tool(
            name="run_query",
            description="Run a SELECT query on the database",
            inputSchema={
                "type": "object",
                "properties": {
                    "sql": {"type": "string"}
                },
                "required": ["sql"]
            }
        )
    ]

@app.call_tool()
async def call_tool(name, arguments):
    if name == "run_query":
        rows = run_sql(arguments["sql"])
        return [types.TextContent(type="text", text=json.dumps(rows, indent=2))]

async def main():
    async with stdio_server() as (r, w):
        await app.run(r, w, app.create_initialization_options())

asyncio.run(main())