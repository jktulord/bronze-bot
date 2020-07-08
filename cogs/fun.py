import discord
import json
import random
from discord.ext import commands
import functs


class fun(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['алексей'])
    async def aleksey(self, ctx):
        await ctx.send('СТУКОВ')

    @commands.command(aliases=['стуков'])
    async def stukhov(self, ctx):
        await ctx.send('АЛЕКСЕЙ')

    @commands.command(aliases=['поконям'])
    async def pokonyam(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name='Хотсеры')
        TEXTS = [f'{role.mention}, у нас дейлик. Возможно криминал. По коням!',
                 f'{role.mention}, вылезайте уже из Лола!',
                 f'{role.mention}, хватит играть в chess royal!',
                 f'{role.mention}, пошли в старкра... Нет? Ладно, идем в хотс!',
                 f'{role.mention}, общий сбор!',
                 f'{role.mention}, настало ваше время!']
        await ctx.send(random.choice(TEXTS))

    @commands.command(aliases=['поконям'])
    async def pokonyam(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name='Старкрафтеры')
        TEXTS = [f'{role.mention}, новый кооп командир вышел. Инфа 100%!',
                 f'{role.mention}, в батлчесте еще остались не открытые скины!',
                 f'{role.mention}, общий сбор!',
                 f'{role.mention}, время кастомок!']
        await ctx.send(random.choice(TEXTS))

def setup(client):
    client.add_cog(fun(client))