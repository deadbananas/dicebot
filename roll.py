import discord
from discord.ext.commands import Bot
from discord.ext import commands
import asyncio
import time
import random
from discord import Game


Client = discord.client
client = commands.Bot(command_prefix = '!')
Clientdiscord = discord.Client()


@client.event
async def on_ready():
    await client.change_presence(game=Game(name='      '))
    print('Ready, Freddy') 


@client.event
async def on_message(message):
    if ('heck') in message.content:
       await client.delete_message(message)
    if ('frick') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!d20'):
        randomlist = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',]
        await client.send_message(message.channel,(random.choice(randomlist)))

client.run('NTEyMDk2ODIzNzIxMzI4NjUw.Ds4t0g.6QwYHlZ9EGKAq8xN61WNGExyyHE')
