import discord
import json
import random
from discord.ext import commands
import functs
from ore import recipe

LEVEL_UP = "level_up"
RAISE_UP = "raise_up"
ASCENSION_TO_BRONZE = "Возвышение до бронзовенят"
ASCENSION_TO_BRONZE1 = "Возвышение до Алюминиевой бронзы "


class offer(object):
    def __init__(self, name, tag, req_dict, out_funct, out_text):
        self.name = name
        self.tag = tag
        self.req_dict = req_dict
        self.out_funct = out_funct
        self.out_text = out_text

    def req_line(self):
        line = ""
        for i in self.req_dict:
            if self.req_dict[i] != 0:
                line += i + "=" + str(self.req_dict[i]) + ", "
        return line


def raise_up_funct():
    s = 1


offers = {ASCENSION_TO_BRONZE: offer(name=RAISE_UP, tag="BRZ", req_dict=recipe.res_dict(bronze_ore=1),
                     out_funct=raise_up_funct, out_text="Повышает вас до статуса бронзовенят, за жалкий один слиток "
                                                        "бронзы")}


class ore_unlocks(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=["магаз"])
    async def shop(self, ctx):
        embed = discord.Embed(
            Title='Title',
            description="Магаз",
            colour=discord.Color.light_grey()
        )
        for i in offers:
            embed.add_field(name=offers[i].name + " [" + offers[i].tag + "] ", value=offers[i].req_line(),
                            inline=True)
            embed.add_field(name="Описание:", value=offers[i].out_text, inline=True)
            embed.set_footer(text="используй !shop [tag] или используй !shop [num] (без [])")
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ore_unlocks(client))
