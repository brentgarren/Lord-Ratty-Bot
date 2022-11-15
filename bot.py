# bot.py

#Libraries
from asyncio import events
import os
from py_compile import _get_default_invalidation_mode
import random
import discord
import time
from easy_pil import Editor, load_image_async, Font
from discord.ext import context
from discord.ext import commands
from discord import File
from random import randint
from dotenv import load_dotenv
#from word_banlist import banlist
from discord.utils import get
from variable import welcome_message
from variable import ignore_message
from word_banlist import banlist

import asyncio


load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

class MyClient(discord.Client):


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        


    async def on_ready(self):
        print('Ready')
    
    
    async def on_raw_reaction_add(self, payload):
        #if payload.message_id != self.target_message_id:
        #    return
        
        guild = client.get_guild(payload.guild_id)
        
        if payload.emoji.name == '🐲' and payload.message_id == 1008821437416611950:
            role = discord.utils.get(guild.roles, name="TTRPG")
            await payload.member.add_roles(role)
        if payload.emoji.name == '🃏' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Card Gamer')
           await payload.member.add_roles(role)
        if payload.emoji.name == '✅' and payload.message_id == 1021276883322675270:
          role = discord.utils.get(guild.roles, name='Subject')
          await payload.member.add_roles(role)
        if payload.emoji.name == '♟️' and payload.message_id == 1008821437416611950:
            role = discord.utils.get(guild.roles, name="Tabletop Simulator")
            await payload.member.add_roles(role)
        if payload.emoji.name == '⚔️' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Total War')
           await payload.member.add_roles(role)
        if payload.emoji.name == '✈️' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Warthunder')
           await payload.member.add_roles(role)
        if payload.emoji.name == '🌑' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='7 Days 2 Die')
           await payload.member.add_roles(role)
        if payload.emoji.name == '🇱' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='League of Legends')
           await payload.member.add_roles(role)
        if payload.emoji.name == '⚓' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Barotrauma')
           await payload.member.add_roles(role)
        if payload.emoji.name == '🧀' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Vermintide')
           await payload.member.add_roles(role)
        if payload.emoji.name == '🇻' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Valorant')
           await payload.member.add_roles(role)
        if payload.emoji.name == '🇩' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Darktide')
           await payload.member.add_roles(role)
    async def on_raw_reaction_remove(self, payload):
        
        #if payload.message_id != self.target_message_id:
        #    return
        
        guild = client.get_guild(payload.guild_id)
        member = guild.get_member(payload.user_id)

        if payload.emoji.name == '🐲' and payload.message_id == 1008821437416611950:
            role = discord.utils.get(guild.roles, name="TTRPG")
            await member.remove_roles(role)
        if payload.emoji.name == '🃏' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Card Gamer')
           await member.remove_roles(role)
        if payload.emoji.name == '✅' and payload.message_id == 1021276883322675270:
           role = discord.utils.get(guild.roles, name='Subject')
           await member.remove_roles(role)
        if payload.emoji.name == '♟️' and payload.message_id == 1008821437416611950:
            role = discord.utils.get(guild.roles, name="Tabletop Simulator")
            await member.remove_roles(role)
        if payload.emoji.name == '⚔️' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Total War')
           await member.remove_roles(role)
        if payload.emoji.name == '✈️' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Warthunder')
           await member.remove_roles(role)
        if payload.emoji.name == '🌑' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='7 Days 2 Die')
           await member.remove_roles(role)
        if payload.emoji.name == '🇱' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='7 Days 2 Die')
           await member.remove_roles(role)
        if payload.emoji.name == '⚓' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Barotrauma')
           await member.remove_roles(role)
        if payload.emoji.name == '🧀' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Vermintide')
           await member.remove_roles(role)
        if payload.emoji.name == '🇻' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Valorant')
           await member.remove_roles(role)
        if payload.emoji.name == '🇩' and payload.message_id == 1008821437416611950:
           role = discord.utils.get(guild.roles, name='Valorant')
           await member.remove_roles(role)

intents = discord.Intents.default()
intents.members = True 


client = MyClient(intents=intents)


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

@client.event
async def on_member_join(member):
    
    intents = discord.Intents.all()
    role = get(member.guild.roles, id=1008820038825934989)
    await member.add_roles(role)
    channel = member.guild.get_channel(1007437376882212956)

    background = Editor("background1.png")
    profile_image = await load_image_async(str(member.avatar_url))

    profile = Editor(profile_image).resize((150, 150)).circle_image()
    poppins = Font.poppins(size=50, variant="bold")

    poppins_small = Font.poppins(size=32, variant="light")

    background.paste(profile, (325,90))
    background.ellipse((325, 90), 150, 150, outline="white",stroke_width=5)

    background.text((400, 260), f"Greetings Subject,", color="white", font=poppins, align="center",)
    background.text((400, 325), f"{member.name}#{member.discriminator}", color="white", font=poppins_small, align="center")

    file = File(fp=background.image_bytes, filename="background1.jpg")
    await channel.send(f"Hello {member.mention}! Welcome to The **{member.guild.name} **")
    await channel.send(file=file)



##This section includes various greetings Lord Ratty will say
@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if any(word in message.content.lower() for word in banlist):
        await message.author.send('Silence, Hold your tongue!')
        await message.delete()
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