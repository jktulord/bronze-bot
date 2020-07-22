import discord
import json
import random
from discord.ext import commands
import functs


class imgur(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["бесонечность"])
    async def infinity(self, ctx):
        embed = functs.embed_picture(ctx)
        await ctx.send(embed=embed)



def setup(client):
    client.add_cog(imgur(client))