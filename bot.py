# bot.py

#Libraries
import os
import random
import discord
import time
from discord.ext import context
from discord.ext import commands
from random import randint
from dotenv import load_dotenv
#from word_banlist import banlist
from discord.utils import get
from variable import welcome_message
from variable import ignore_message
import asyncio
intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

client = discord.Client()
##Variables

### Shows that Lord Ratty has entered the server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
## Lord Ratty entered Server

#Lord Ratty will respond to Direct Messages
@client.event
async def on_message(message):
    if isinstance(message.channel, discord.channel.DMChannel) and message.author != client.user:
        await message.channel.send('This is a DM')
## End of Direct Message


#Lord Ratty will Ban words
#@client.event

#async def on_member_join(member):
#    if any(banned in member.name for banned in banlist):
 #       await member.ban()
#        return

### Direct Message new Members
#@client.event
#async def on_member_join(member):
#    await member.create_dm()
#    await member.dm_channel.send(
#        f' , Greetings {member.name}, Welcome to my trove.'
#    )


##This section includes various greetings Lord Ratty will say
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if message.content.lower() == 'hello':
        response = random.choice(welcome_message)
        await message.channel.send(response)
        return
    if "Lord Ratty" in message.content:
        response = random.choice(welcome_message)
        await message.channel.send(response)
        return
    if "lord ratty" in message.content:
        response = random.choice(ignore_message)
        await message.channel.send(response)
        return
    if message.content.lower() == 'roll20':
        response = random.randint(1, 20)
        await message.channel.send(response)
        return
    if message.content.lower() == 'roll6':
        response = random.randint(1, 6)
        await message.channel.send(response)
        return
    if message.content.lower() == 'roll4':
        response = random.randint(1, 4)
        await message.channel.send(response)
        return
    if message.content.lower() == 'roll12':
        response = random.randint(1, 12)
        await message.channel.send(response)
        return
    if message.content.lower() == 'roll8':
        response = random.randint(1, 8)
        await message.channel.send(response)
        return
    if message.content.lower() == 'roll100':
        response = random.randint(1, 100)
        await message.channel.send(response)
        return
    elif message.content == 'raise-exception':
        raise discord.DiscordException
        return

###This is end of Ratty one liners



client.run(TOKEN)