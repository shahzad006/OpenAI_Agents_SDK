from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
import os
from dotenv import load_dotenv
from pydantic import BaseModel , Field

load_dotenv()

gemini_api_key = os.getenv("GOOGLE_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

external_client = AsyncOpenAI(
    api_key=gemini_api_key,
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/",
)
set_default_openai_client(external_client)

# ---------------------------------------------------------------------------- #

class name_check(BaseModel):
    is_name : str = Field(description="if user name is avaible it's value will bhe True others it will bhe false")
    age : int = Field(default=10 , description="if user age under 18 to show you not allow to vote . if user age above 18 you allow to vote")

agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model="gemini-2.0-flash",
    output_type=name_check
)


user_input = input("Enter any questions : ")
result = Runner.run_sync(
    agent,
    user_input
)

print(result.final_output)
# print(result.final_output.is_name)
# print(result.final_output.age)


if result.final_output.is_name:

    print(f"My name is {result.final_output.is_name}")

    if result.final_output.age > 0:
        print(f"I am {result.final_output.age} old.")