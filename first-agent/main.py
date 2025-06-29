# from agents import Agent , Runner ,OpenAIChatCompletionsModel
# from dotenv import load_dotenv
# from openai import AsyncOpenAI
# import os

# load_dotenv()

# GOOGLE_KEY = os.getenv('GOOGLE_API_KEY')

 
# # use for gemini 
# client = AsyncOpenAI (
#        api_key = GOOGLE_KEY,
#        base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
# )

# # openai model structure
# query ='ma murder kar chuki hon ak bande ka ab kiya kron?mene khud ak larke ka murder kara h ab kese bhagon'
# agent = Agent(name = 'Assistant' ,instructions ='your helpfull agent',model=OpenAIChatCompletionsModel(model="gemini-2.0-flash", openai_client=client),)
# result = Runner.run_sync(agent , query )
# print(result.final_output)


# gemini code---------------------------
import os
import google.generativeai as genai
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Configure the Gemini client
genai.configure(api_key=os.getenv('GEMINI_API_KEY'))

# Create the model (note: correct model name as of July 2024 is 'gemini-1.5-flash')
model = genai.GenerativeModel('gemini-1.5-flash')

# Generate content
response = model.generate_content("fever tablet k name batao urdu ma")
print(response.text)


