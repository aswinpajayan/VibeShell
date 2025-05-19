import asyncio
from mcp_agent.core.fastagent import FastAgent

# Create the application
fast = FastAgent("VibeShell - your CLI boiler plate generator")


# Define the agent
@fast.agent(name='greeter', instruction="You are a helpful AI Agent. You can use the mcp servers exposed to you to help the user",
            servers=["filesystem"])

# Define the clients
#@fast.agent(name='file_handler_agent', servers=[""]


async def main():
    # use the --model command line switch or agent arguments to change model
    async with fast.run() as agent:
        await agent.interactive()


if __name__ == "__main__":
    asyncio.run(main())
