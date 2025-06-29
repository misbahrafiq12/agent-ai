from agents import Agent, Runner, OpenAIChatCompletionsModel
from openai.types.responses import ResponseTextDeltaEvent
from openai import AsyncOpenAI
from agents.run import RunConfig
from dotenv import load_dotenv
import asyncio
import os

# Load .env file
load_dotenv()

# Get API key
api_key = os.getenv("OPENROUTER_API_KEY")

# Validate key
if not api_key:
    raise ValueError("API key not found. Make sure OPENROUTER_API_KEY is set in your .env file.")

# Create OpenAI-compatible client
client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)
print(dir(RunConfig))
# Create agent

agent = Agent(
    name="basic_agent",
    instructions="You are a helpful assistant.",
    model=OpenAIChatCompletionsModel(
        model="meta-llama/llama-4-maverick:free",
        openai_client=client
    ),
)

# Run query
result =  Runner.run(agent, "What is animals",)
print(result.final_output) 



# ------------run

# async def main():
#     agent = Agent(
#     name="basic_agent",
#     instructions="You are a helpful assistant.",
#     model=OpenAIChatCompletionsModel(
#         model="meta-llama/llama-4-maverick:free",
#         openai_client=client
#     ),
# )

# # Run query
#     result = await Runner.run(agent, "What is animals")
#                             #   run_config=RunConfig(max_steps=3))
#     print(result.final_output)
# asyncio.run(main())
# run stream------------------------

# async def main():
#     agent = Agent(
#     name="Assistant",
#     instructions="You are an AI expert.",
#     model=OpenAIChatCompletionsModel(model="meta-llama/llama-4-maverick:free", openai_client=client),
#     )
#     query = input("Enter the query:")
#     result = Runner.run_streamed(agent, input=query)
#     async for event in result.stream_events():
#         if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
#             print(event.data.delta, end="", flush=True)


# asyncio.run(main())   