import discord
import json
import random
from discord.ext import commands
import functs

def listmerge3(lstlst):
    all=[]
    for lst in lstlst:
      all.extend(lst)
    return all

class random_Hero(commands.Cog):

    def __init__(self, client):
        self.client = client

    # @commands.Cog.listener()
    # async def on_ready(self):
    #    print("Bot is online.....")

    #@commands.command()
    #async def randHero(self, ctx):
    #    with open("Heroes.json", "r") as read_file:
    #        data = json.load(read_file)
    #    chosen_hero = random.choice(data["Heroes"])
    #    embed = functs.text_embed("БОГ РАНДОМА ПОВЕЛЕВАЕТ, пикай ето: " + chosen_hero)
    #    await ctx.send(embed=embed)

    @commands.command()
    async def randomHero(self, ctx, tag="Help"):
        with open("Heroes.json", "r") as read_file:
            data = json.load(read_file)
            chosen_hero = "....пропиши !randomHero help, чувак..."
        if tag in ["All", "all", "все", "Все"]:
            chosen_hero = random.choice(data["Heroes"])
        elif tag in ["ААтакеры", "ААтакер", "AA", "АА"]:
            chosen_hero = random.choice(data["ААтакеры"])
        elif tag in ["Маги", "Маг", "маг", "маги"]:
            chosen_hero = random.choice(data["Маги"])

        elif tag in ["Жир", "жир"]:
            chosen_hero = random.choice(data["Жир"])
        elif tag in ["Танк", "танк", "танки", "Танки"]:
            chosen_hero = random.choice(data["Танки1"])
        elif tag in ["Брузяхи", "брузяхи", "Брузяха", "брузяха", "брузеры", "Брузеры", "брузер", "Брузер"]:
            chosen_hero = random.choice(data["Брузяхи1"])

        elif tag in ["Лекари", "Лекарь", "лекари", "лекарь"]:
            chosen_hero = random.choice(data["Лекари"])
        elif tag in ["Поддержка", "поддержка"]:
            chosen_hero = random.choice(data["Поддержка"])
        elif tag in ["Ебоклаки", "ебоклаки", "Ебоклака", "ебоклака"]:
            chosen_hero = random.choice(data["Ебоклаки"])

        if tag in ["Help", "help"]:
            embed = functs.text_embed('Команде randomHero требуется тег '
                                      '(Доступные теги:Вcе, Маги, ААтакеры, Ебоклаки, Лекари, Жир, Танки, Брузяхи, '
                                      'Поддержка)')

            await ctx.send(embed=embed)
        else:
            embed = functs.text_embed("БОГ РАНДОМА ПОВЕЛЕВАЕТ, пикай вот это: " + chosen_hero, name="БОГ РАНДОМА")
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(random_Hero(client))
