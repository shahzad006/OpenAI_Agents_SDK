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

# ---------------------------------- Handoff --------------------------------- #


math_agent = Agent(
    name="math_teacher",
    instructions="You are math teacher just solve math question and any math related quires",
    model="gemini-2.0-flash",
    handoff_description="Your are math Teacher"

)


# ---------------------------------------------------------------------------- #

englih_agent = Agent(
    name="english_teacher",
    instructions="You are English teacher just solve english question and any english related quires",
    model="gemini-2.0-flash",
    handoff_description="Your are English Teacher"

)

# ---------------------------------------------------------------------------- #


urdu_agent = Agent(
    name="urdu_teacher",
    instructions="You are urdu teacher just solve urdu question and any urdu related quires",
    model="gemini-2.0-flash",
    handoff_description="Your are urdu Teacher"

)


# ---------------------------------------------------------------------------- #
main_agent: Agent = Agent(
    name="Main_Agnet", 
    instructions="""You are main agent
    1: any question math related you cell math agent 
    2: any question english related you cell english agent 
    3: any quires urdu realted you cell urdu agnet 
    don't reply you and you cell agents """, 
    model="gemini-2.0-flash" ,
    
)
user_input = input("Enter your Question : ")
result = Runner.run_sync(
    starting_agent=main_agent,
    input=user_input,
    
)

print(result.final_output)
print(f"❤ {result.last_agent}")