#this fill contains all different ways to connect with LLMs

#connecting groq (with api)

from groq import AsyncGroq

client = AsyncGroq(api_key="")

async def call_groq(prompt, modl, max_tokens    ):
    chat_completion = await client.chat.completions.create(messages=prompt, model="mixtral-8x7b-32768", max_tokens=200, stop=[r"/s"])
    chat_completion = chat_completion.choices[0].message.content
