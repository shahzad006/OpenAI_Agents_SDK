from agents import Agent , Runner ,AsyncOpenAI , set_default_openai_api , set_default_openai_key , set_tracing_disabled , OpenAIChatCompletionsModel

OpenRouter_api_key = "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"
set_tracing_disabled(True)
set_default_openai_api("chat_completions")


clint = AsyncOpenAI(
    api_key=OpenRouter_api_key,
    base_url= "https://openrouter.ai/api/v1"
)

set_default_openai_key(clint)

agent = Agent(
    name="Assistant",
    instructions="You are a helpful assistant",
    model = OpenAIChatCompletionsModel(model="deepseek/deepseek-chat-v3-0324:free" , openai_client=clint  )
   
)

result = Runner.run_sync(
    agent,
    "Hi who are you?"
)


print(result.final_output)