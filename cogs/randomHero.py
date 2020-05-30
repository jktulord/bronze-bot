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

    @commands.command()
    async def randHero(self, ctx):
        with open("Heroes.json", "r") as read_file:
            data = json.load(read_file)
        chosen_hero = random.choice(data["Heroes"])
        embed = functs.text_embed("БОГ РАНДОМА ПОВЕЛЕВАЕТ, пикай ето: " + chosen_hero)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(basic(client))
