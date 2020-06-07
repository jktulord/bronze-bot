import discord
import json
import random
from discord.ext import commands
import functs


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client



    @commands.command(aliases=['стуков'])
    async def stukhov(self, ctx):
       await ctx.send('АЛЕКСЕЙ')



def setup(client):
    client.add_cog(fun(client))