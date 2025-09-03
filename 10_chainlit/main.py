import chainlit as cl

@cl.on_chat_start
async def main():
    await cl.Message(
        content="Hello! I'm your Chainlit assistant. How can I help you today?"
    ).send()


@cl.on_message
async def main(msg:cl.Message):
    user_input = msg.content
    await cl.Message(
        content=f"[AI] : {user_input}"
    ).send()