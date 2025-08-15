import os
from dotenv import load_dotenv
from agents import Agent , Runner
from agents.extensions.models.litellm_model import LitellmModel
import rich

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model=LitellmModel(
        model = "gemini/gemini-2.0-flash" , 
        api_key = gemini_api_key
    )
)

result = Runner.run_sync(
    agent,
    "Hello"
)

rich.print(result.final_output)