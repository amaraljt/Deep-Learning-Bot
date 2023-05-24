import discord
import os
from discord.ext import commands
import random
import openai

openai.organization = os.getenv("OPENAI_ORG")
openai.api_key = os.getenv("OPENAI_API_KEY")
print(openai.Model.list())

intents=discord.Intents.all()

client = commands.Bot(command_prefix="$", intents=intents)

@client.event
async def on_ready():
    print(f'Logged in as {client.user} (ID: {client.user.id})')

# --------------
# OpenAI API
# --------------
@client.event
async def on_message(message):
        if(message.author.bot):
            return
        
        print(message.author + ": " + message.content)
        gpt_response = openai.Completion.create(model="text-davinci-003", prompt=message.content, temperature=0, max_tokens=50)
        await message.channel.send(gpt_response['choices'][0]['text'])


client.run(os.getenv('DISCORD_TOKEN'))
