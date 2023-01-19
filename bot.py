# bot.py
import os

import discord
from dotenv import load_dotenv
import re

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
intents.members = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    contentmsg = (re.sub(r"\W+", " ", message.content)).replace("  "," ")
        
    alljokes = ["i m ", "i am ", "im "]
    for j in alljokes:
        if j in contentmsg.lower():
            response = contentmsg[contentmsg.lower().index(j)+len(j)::]
            await message.channel.send(f"hi {response}, i'm your missing dad")
            try:
                await message.author.edit(nick=response if len(response) < 33 else response[:33])
            except:
                pass
            finally:
                break


client.run(TOKEN)
