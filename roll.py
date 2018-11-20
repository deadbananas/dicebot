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
    if ('frick') in message.content:
       await client.delete_message(message)
    if message.content.startswith('!d20'):
        randomlist = ['1','2','3','4','5','6','7','8','9','10','11','12','13','14','15','16','17','18','19','20',]
        await client.send_message(message.channel,(random.choice(randomlist)))



      
       
    if message.content.startswith('!d12'):
        randomlist = ['1','2','3','4','5','6','7','8','9','10','11','12',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!d10'):
        randomlist = ['1','2','3','4','5','6','7','8','9','10',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!d8'):
        randomlist = ['1','2','3','4','5','6','7','8',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content.startswith('!d6'):
        randomlist = ['1','2','3','4','5','6',]
        await client.send_message(message.channel,(random.choice(randomlist)))
    if message.content == '!bard':
        await client.send_message(message.channel,'https://www.youtube.com/watch?v=aAeU2SrLlQM')
    if message.content == '!dnd':
        await client.send_message(message.channel,'"math"')

     


    if message.content == '!zane':
        await client.send_message(message.channel,'hecka gay')



    
    if message.content.startswith('!d4'):
        randomlist = ['1','2','3','4',]
        await client.send_message(message.channel,(random.choice(randomlist)))
client.run('NTEyMDk2ODIzNzIxMzI4NjUw.Ds1BRA.8bCCKf1jP1g0ntOiZ5xlh9N-PX0')
