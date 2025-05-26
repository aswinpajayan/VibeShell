import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("VibeShell - your CLI boiler plate generator")


# Define the agent
@fast.agent(name='greeter',
            instruction="You are a helpful AI Agent."
                        "<tool_calling>"
                        "You have tools at your disposal to solve the coding task"
                        "ALWAYS follow the tool call schema exactly as specified and"
                        "make sure to provide all necessary parameters."
                        "The conversation may reference tools that are no longer available."
                        "NEVER call tools that are not explicitly provided."
                        "you can call a tools multiple times help the users"
                        "You can use the mcp servers exposed to you to help the user"
                        "</tool_calling>"
                        "use the mcp-roots to decode file paths"
                        "append all file paths to /projects/workspace folder before using filesystem tool"
                        "current working directory will be available at /projects/workspace",
            servers=["filesystem"])

# Define the clients
#@fast.agent(name='file_handler_agent', servers=[""]


async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
