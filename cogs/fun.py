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

    @commands.command(aliases=['алексей'])
    async def aleksey(self, ctx):
        await ctx.send('СТУКОВ')

    @commands.command(aliases=['поконям'])
    async def pokonyam(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name='Хотсеры')
        await ctx.send(role.mention, ', по коням!')

def setup(client):
    client.add_cog(fun(client))