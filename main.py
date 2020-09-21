import discord
import os
from discord.ext import commands

TOKEN = 'NzE0OTM3ODIzNjE0MjA1OTg0.Xs17vA.Pbcr-IEBc8YOpCcHnxH9yh6auXI'

client = commands.Bot(command_prefix='!')
client.remove_command('help')

# the events------------------------'роб, Гроб, Кладбище, Пидор'
@client.event
async def on_ready():
    print('bot is ready')


@client.command()
async def load(ctx, extension):
    client.load_extension(f'cog.{extension}')


@client.command()
async def unload(ctx, extension):
    client.unload_extension(f'cog.{extension}')


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        client.load_extension(f'cogs.{filename[:-3]}')

client.run(TOKEN)
