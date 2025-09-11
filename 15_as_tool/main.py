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
# ---------------------------------------------------------------------------- #

suport_agent = Agent(
    name= "suport_agent",
    instructions="You are suport agnet",
    model="gemini-2.0-flash" ,
    
)
# ---------------------------------------------------------------------------- #
shoping_agent = Agent(
    name= "shoping",
    instructions="You are shoping agnet",
    model="gemini-2.0-flash" ,
    
)



# ---------------------------------------------------------------------------- #
agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant any queires for shoping suport and product releted you must cell the tool never reply you LLM just cell the tool.", 
    model="gemini-2.0-flash" ,
    tools=[
        suport_agent.as_tool(
            tool_name="suport_agent_as_tool" , 
            tool_description="This is suport agnet for user queires related just shoping ,alwayes show this emoje for text strat and end 🧡"
        ),

        shoping_agent.as_tool(
            tool_name="shoping_agent_as_tool",
            tool_description="You are shoping agent just fulfil user find product , alwayes show this emoje for text strat and end ❌"
        )

        ]
    
)
user_input = input("Enter ...... : ")
result = Runner.run_sync(
    starting_agent=agent,
    input=user_input
    
)

print(result.final_output)