# bot.py
import os

import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'{client.user} is connected')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    contentmsg = message.content.lower()
    if "im " in contentmsg:
        response = message.content[contentmsg.index("im ")+3::]
        await message.channel.send(f"hi {response}, i'm your missing dad")
    
    elif "i'm " in contentmsg:
        response = message.content[contentmsg.index("i'm ")+4::]
        await message.channel.send(f"hi {response}, i'm your missing dad")
    
    elif "i am" in contentmsg:
        response = message.content[contentmsg.index("i am")+4::]
        await message.channel.send(f"hi{response}, i'm your missing dad")
    elif message.content == 'raise-exception':
        raise discord.DiscordException


client.run(TOKEN)
