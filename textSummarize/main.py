from agents import Agent , Runner , OpenAIChatCompletionsModel
from dotenv import load_dotenv
from openai import AsyncOpenAI
import os
import asyncio


load_dotenv()
API_KEY=os.getenv("OPEN_ROUTER_KEY")

client =AsyncOpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=API_KEY
)

query = input("Enter your data: ")
instruction = """You are a smart student assistant. Your job is to help students in the following ways:

1. Answer academic questions clearly, but briefly — ideally within 3–4 sentences.
2. Provide helpful study tips in a concise format (a short list of bullet points or no more than 5 tips).
3. Summarize any text input—regardless of its length or language—into a concise summary of 2–5 lines. The summary should always be in the same language as the original input.

Keep all your responses brief and focused."""



async def main():

    agent = Agent(name="Text Summarize Agent",instructions=instruction,model=OpenAIChatCompletionsModel(
    model="meta-llama/llama-4-maverick:free",
    openai_client=client
))

    result = await Runner.run(agent , input=query)
    print(result.final_output)

asyncio.run(main())    