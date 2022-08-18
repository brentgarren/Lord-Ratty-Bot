# bot.py
import os
import random
import discord
from discord.ext import context
from dotenv import load_dotenv
#from word_banlist import banlist
from discord.utils import get


intents = discord.Intents.default()
intents.members = True

load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')


client = discord.Client()
### Shows that Lord Ratty has entered the server
@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')
## Lord Ratty entered Server

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

    welcome_message = [
        'Welcome to my Trove, Subject',
        '***Eats Cheese***', '***shines ring*** Another one, Welcome', 'Hi there, Hello, Did you bring fresh cheese for Ratty?', 'You have chosen wisely.', 'Ohhh Shiny.'
    ]

    ignore_message = ['*Lord Ratty refuses to acknowledge you*', '*stares*', '*eats cheese*', '**You will address me properly!**' 
    
    ]
    if message.content.lower() == 'hello':
        response = random.choice(welcome_message)
        await message.channel.send(response)

    if "Lord Ratty" in message.content:
        response = random.choice(welcome_message)
        await message.channel.send(response)
    
    if "lord ratty" in message.content:
        response = random.choice(ignore_message)
        await message.channel.send(response)

    elif message.content == 'raise-exception':
        raise discord.DiscordException

###This is end of Ratty one liners






client.run(TOKEN)