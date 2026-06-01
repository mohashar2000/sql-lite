import asyncio, json
from mcp import ClientSession, StdioServerParameters
from mcp.client.stdio import stdio_client

async def main():
    # Connect to the MCP server
    server_params = StdioServerParameters(
        command="python",
        args=["server-MCP-SqlLite.py"]
    )

    async with stdio_client(server_params) as (read, write):
        async with ClientSession(read, write) as session:

            # Initialize the session
            await session.initialize()

            # ── Run a query ──────────────────────────────
            result = await session.call_tool(
                "run_query",
                arguments={"sql": "SELECT * FROM students"}
            )

            # Parse and print the result
            rows = json.loads(result.content[0].text)
            print("Query result:")
            for row in rows:
                print(row)

            # ── Query with a filter ──────────────────────
            result2 = await session.call_tool(
                "run_query",
                arguments={"sql": "SELECT * FROM students WHERE grade = 'A'"}
            )
            top = json.loads(result2.content[0].text)
            print("\nGrade A students:")
            for row in top:
                print(row)

asyncio.run(main())