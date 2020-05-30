import discord
import json
import random
from discord.ext import commands
import functs


class basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
    #    print("Bot is online.....")

    @commands.command(aliases=['стуков'])
    async def stukhov(self, ctx):
       await ctx.send('АЛЕКСЕЙ')

    @commands.command(aliases=['алексей'])
    async def aleksey(self, ctx):
        await ctx.send('СТУКОВ')

def setup(client):
    client.add_cog(basic(client))