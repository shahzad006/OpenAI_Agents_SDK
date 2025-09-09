from agents import Agent , Runner ,AsyncOpenAI , set_default_openai_api , set_default_openai_key , set_tracing_disabled , OpenAIChatCompletionsModel
import os 
import chainlit as cl
from dotenv import load_dotenv
load_dotenv()

OpenRouter_api_key = os.getenv("OPENROUTER_API_KEY")
set_tracing_disabled(True)
set_default_openai_api("chat_completions")

# ---------------------------------------------------------------------------- #
history = []
# ---------------------------------------------------------------------------- #

models = {
    "DeepSeek" : "deepseek/deepseek-chat-v3.1:free",
    "Qwen"  : "qwen/qwen3-coder:free",
    "Meta" : "meta-llama/llama-3.3-70b-instruct:free",
    "Google" : "google/gemini-2.0-flash-exp:free" ,
    "Openai" : "openai/gpt-oss-20b:free"
}

# ---------------------------------------------------------------------------- #


@cl.on_chat_start
async def main():
    await cl.Message(
        content="Wellcome",
    ).send()

    settings = await cl.chat_context(
        [
            cl.input_widget.Select(
                id= "Model" ,
                label = "Choose any LLM Model" ,
                values=list(models.keys) ,
                initial_index=0

            )
        ]

    ).send()

    await setup_chat(settings)

    
# ---------------------------------------------------------------------------- #


@cl.on_settings_update
async def setup_chat(settings):
    model_name = settings["Model"]

    cl.user_session.set(model_name , models[model_name])

    await cl.Message(
        content=f"You have selected {model_name} AI model. "
    ).send()

# ---------------------------------------------------------------------------- #


# ---------------------------------------------------------------------------- #


@cl.on_message
async def main(msg:cl.Message):
    user_input = msg.content

    history.append(
        {
            "role": "user",
            "content": user_input
        }
    )


    
    selected_model=  cl.user_session.get("models")

    clint = AsyncOpenAI(
        api_key=OpenRouter_api_key,
        base_url= "https://openrouter.ai/api/v1"
    )

    set_default_openai_key(clint)
    # 


    agent = Agent(
        name="Assistant",
        instructions="You are a helpful assistant",
        model = OpenAIChatCompletionsModel(model=selected_model , openai_client=clint  )

    )


    result = Runner.run_sync(
        agent, 
        history
    )

    await cl.Message(
        content=result.final_output
    ).send()
