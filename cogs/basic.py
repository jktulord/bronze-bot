import discord
from discord.ext import commands
import functs


class basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.....")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        print(f'{member} has joined the server')
        role = discord.utils.get(member.guild.roles, name='Новачки')
        await member.add_roles(role)

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    #@commands.command(aliases=['purge', 'CLEAR', 'PURGE'])
    #async def clear(self, ctx, arg=5):
    #    n = arg
    #    await ctx.channel.purge(limit=n)

    @commands.command(aliases=['getHotser'])
    async def getHots(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name='Хотсеры')
        if role in author.roles:
            roles = author.roles
            roles.remove(role)
            await author.edit(roles=roles)
            embed = functs.text_embed(author.name + ' теперь НЕ Хотсер')
            await ctx.send(embed=embed)
        else:
            await author.add_roles(role)
            embed = functs.text_embed(author.name + ' теперь Хотсер')
            await ctx.send(embed=embed)

    @commands.command()
    async def getNews(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name='Новостная подписка')
        if role in author.roles:
            roles = author.roles
            roles.remove(role)
            await author.edit(roles=roles)
            embed = functs.text_embed(author.name + ' теперь НЕ подписан')
            await ctx.send(embed=embed)
        else:
            await author.add_roles(role)
            embed = functs.text_embed(author.name + ' теперь подписан')
            await ctx.send(embed=embed)


def setup(client):
    client.add_cog(basic(client))
