from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api , function_tool
import os
from dotenv import load_dotenv

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)
# ------------------------------- Function Tool ------------------------------ #

@function_tool
def get_weather(city:str):
    """This is weather Tool for for all City"""

    return f"Today is raining for {city}"

# ---------------------------------------------------------------------------- #
agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model="gemini-2.0-flash" ,
    tools= [get_weather]
)

result = Runner.run_sync(
    agent,
    "what is the weather in dubai"
)

print(result.final_output)