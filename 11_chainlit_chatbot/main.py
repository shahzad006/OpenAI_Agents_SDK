from agents import Agent, Runner, AsyncOpenAI, set_default_openai_client, set_tracing_disabled, set_default_openai_api
import os
from dotenv import load_dotenv
import chainlit as cl

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

history = []
# ---------------------------------------------------------------------------- #



agent: Agent = Agent(
    name="Assistant", 
    instructions="You are a helpful assistant", 
    model="gemini-2.0-flash"
)

# ---------------------------------------------------------------------------- #

@cl.on_chat_start
async def start_message():
   await cl.Message(
        content="Wellcome! JUTT Chatbot"
    ).send()


@cl.on_message
async def main(msg:cl.Message):
    user_input = msg.content

    history.append(
        {
            "role": "user",
            "content": user_input
        }
    )

    result = Runner.run_sync(
        agent, 
        history
    )

    await cl.Message(
        content=result.final_output
    ).send()