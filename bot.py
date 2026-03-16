# This example requires the 'message_content' intent.

import discord
from config import token
from ai import ReveAPI
from datetime import datetime

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

api = ReveAPI("papi.e5d0316e-ecda-4492-81b8-ef3eb2d67217.NGMZSBn8CyybBvHMhRIe21iStJGJe9rU")

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$generate_image'):
        filename = str(datetime.now())
        api.generate_reve_image(message.content, file_name=filename)
        await message.channel.send(file=discord.File(filename))

client.run(token)
