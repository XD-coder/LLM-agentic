#this fill contains all different ways to connect with LLMs

#connecting groq (with api)

from groq import AsyncGroq

client = AsyncGroq(api_key="") # add your groq API key here!

async def call_groq(prompt, modl, max_tokens    ):
    chat_completion = await client.chat.completions.create(messages=prompt, model="llama3-70b-8192", max_tokens=4096, stop=[r"/s"])
    chat_completion = chat_completion.choices[0].message.content
