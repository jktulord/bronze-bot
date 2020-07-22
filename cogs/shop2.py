import discord
import json
import random
from discord.ext import commands
import functs
from ore import recipe

LEVEL_UP = "level_up"
RAISE_UP = "raise_up"


class offer(object):
    def __init__(self, name, tag, req_dict, out_funct):
        self.name = name
        self.tag = tag
        self.req_dict = req_dict
        self.out_funct = out_funct

    def req_line(self):
        line = ""
        for i in self.req_dict:
            if self.req_dict[i] != 0:
                line += i + "=" + str(self.req_dict[i]) + ", "
        return line


def raise_up_funct():
    s = 1


offers = {RAISE_UP: offer(name=RAISE_UP, tag="BRZ", req_dict=recipe.res_dict(bronze_ore=1),
                          out_funct=raise_up_funct)}


class ore_unlocks(commands.Cog):

    def __init__(self, client):
        self.client = client

    """
    @commands.command(aliases=["бесонечность"])
    async def unlock(self, ctx):
        embed = discord.Embed(
            Title='Title',
            description="Магаз",
            colour=discord.Color.light_grey()
        )
        await ctx.send(embed=embed)
    """


def setup(client):
    client.add_cog(ore_unlocks(client))
