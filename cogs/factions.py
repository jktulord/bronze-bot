import discord
import json
import random
from discord.ext import commands
import functs


class factions(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command()
    async def getHorde(self, ctx):
        author = ctx.message.author
        Horde_role = discord.utils.get(author.guild.roles, name='Орда')
        Allience_role = discord.utils.get(author.guild.roles, name='Альянс')
        if Horde_role in author.roles:
            roles = author.roles
            roles.remove(Horde_role)
            await author.edit(roles=roles)
            embed = functs.text_embed(author.name + ' теперь НЕ Ордынец', color=discord.Color.red())
            await ctx.send(embed=embed)
        elif Allience_role in author.roles:
            embed = functs.text_embed(author.name + ' Пытается дезертировать (у него не получается).', color=discord.Color.red())
            await ctx.send(embed=embed)
        else:
            await author.add_roles(Horde_role)
            embed = functs.text_embed(author.name + ' теперь Ордынец', color=discord.Color.red())
            await ctx.send(embed=embed)

    @commands.command(aliases=['getAlliance'])
    async def getAllience(self, ctx):
        author = ctx.message.author
        Horde_role = discord.utils.get(author.guild.roles, name='Орда')
        Allience_role = discord.utils.get(author.guild.roles, name='Альянс')
        if Allience_role in author.roles:
            roles = author.roles
            roles.remove(Allience_role)
            await author.edit(roles=roles)
            embed = functs.text_embed(author.name + ' теперь НЕ Альянсер', color=discord.Color.blue())
            await ctx.send(embed=embed)
        elif Horde_role in author.roles:
            embed = functs.text_embed(author.name + ' пытается дезертировать (у него не получается).', color=discord.Color.blue())
            await ctx.send(embed=embed)
        else:
            await author.add_roles(Allience_role)
            embed = functs.text_embed(author.name + ' теперь Альянсер', color=discord.Color.blue())
            await ctx.send(embed=embed)

    @commands.command(aliases=['БоевойКлич'])
    async def battleCry(self, ctx):
        author = ctx.message.author
        Horde_role = discord.utils.get(author.guild.roles, name='Орда')
        Allience_role = discord.utils.get(author.guild.roles, name='Альянс')
        color = discord.Color.lighter_grey()
        if Allience_role in author.roles:
            color = discord.Color.blue()
            quote = " кричит 'ЗА АЛЬЯНС'"
        elif Horde_role in author.roles:
            color = discord.Color.red()
            quote = " кричит 'ЗА ОРДУ'"
        else:
            color = discord.Color.lighter_grey()
            quote = " издает звуки панд"
        embed = functs.text_embed("*" + author.name + quote + "*", color=color, name=None)
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(factions(client))
