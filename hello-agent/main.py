from agents import Agent, Runner, OpenAIChatCompletionsModel, RunConfig
from dotenv import load_dotenv
import os
from openai.types.responses import ResponseTextDeltaEvent
from openai import AsyncOpenAI
import asyncio

load_dotenv()
api_key = os.getenv('OPENROUTER_API_KEY')

client = AsyncOpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

smart_instructions = """
You are Smart JokeBot 🤖.

1. **Intent check**  
   - If the user message contains words like joke / funny / chutkula / mazak / 😂 etc. (even miss‑spelled) → proceed.  
   - Otherwise reply: "Sorry! Main sirf jokes sunata hoon 😅. Please ask me for a joke!"

2. **Detect topic**  
   - Look for keywords: father, mother, teacher, student, doctor, animal, technology, etc.  
   - If no clear keyword → choose a random light‑hearted universal joke.

3. **Detect mood intensity**  
   - Words like "pagal hansa do", "bohot funny", "zordar" → give extra‑funny, exaggerated joke.  
   - Words like "light joke", "chhota sa" → give short gentle joke.

4. **Answer style**  
   - Write in the user’s language (English / Roman Urdu mix).  
   - End with a smiley (😄 / 😂).  
   - One joke per response, max 3‑4 lines.
"""

async def main():
    agent = Agent(
        name="SmartJokeBot",
        instructions=smart_instructions,
        model=OpenAIChatCompletionsModel(
            model="meta-llama/llama-4-maverick:free",
            openai_client=client
        ),
    )

    while True:
        query = input('Ask for a joke: ')
        result = Runner.run_streamed(agent, input=query)

        print("\nJokeBot says:\n")
        async for event in result.stream_events():
            if event.type == "raw_response_event" and isinstance(event.data, ResponseTextDeltaEvent):
                print(event.data.delta, end="", flush=True)

        again = input("\n\nYou want another joke (yes/no): ")
        if again.lower() not in ["haan", "yes", "y"]:
            print("JokeBot says: Theek hai! Fir milte hain, hasta raho! 😄")
            break

# Run the main loop
asyncio.run(main())
