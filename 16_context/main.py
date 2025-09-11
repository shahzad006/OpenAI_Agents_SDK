from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api , function_tool , RunContextWrapper
import os
from dotenv import load_dotenv
from pydantic import BaseModel

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


class UserInfo(BaseModel):
    name : str 
    age : int 
    roll_num : int


# ---------------------------------------------------------------------------- #

my_info = UserInfo(
    name="Muhammad Shahzad" , 
    age = 21 ,
    roll_num= 45435
)


# ---------------------------------------------------------------------------- #


def dymanic_inst(wrapper:RunContextWrapper[UserInfo] , agent : Agent):
    return f"whenever user ask for a roll_number you use the given tool user_inforamation User name is {wrapper.context.name} and user age is {wrapper.context.age}."



# ---------------------------------------------------------------------------- #

@function_tool
async def user_inforamation(wrapper : RunContextWrapper [UserInfo]):
    """This Function is to tell about user roll number"""
    return f"roll number of the user is {wrapper.context.roll_num}"

# ---------------------------------------------------------------------------- #
agent: Agent = Agent[UserInfo](
    name="", 
    instructions=dymanic_inst, 
    model="gemini-2.0-flash" ,
    tools=[user_inforamation]
   
    
)
user_input = input("Enter ...... : ")
result = Runner.run_sync(
    starting_agent=agent,
    input=user_input,
    context=my_info,
    
)

print(result.final_output)