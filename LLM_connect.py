#this fill contains all different ways to connect with LLMs

#connecting groq (with api)

from groq import AsyncGroq

client = AsyncGroq(api_key="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")

async def call_groq(prompt, modl, max_tokens    ):
    chat_completion = await client.chat.completions.create(messages=prompt, model="mixtral-8x7b-32768", max_tokens=200, stop=[r"/s"])
    chat_completion = chat_completion.choices[0].message.content