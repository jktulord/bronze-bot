import discord
from discord.ext import commands
import functs


class basic(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.....")

    @commands.command()
    async def ping(self, ctx):
        await ctx.send('Pong!')

    @commands.command(aliases=['purge', 'CLEAR', 'PURGE'])
    async def clear(self, ctx, arg=5):
        n = arg
        await ctx.channel.purge(limit=n)

    @commands.command()
    async def get(self, ctx):
        author = ctx.message.author
        role = discord.utils.get(author.guild.roles, name='Новачки')
        await author.add_roles(role)
        embed = functs.text_embed(author.name + ' теперь Хотсер')
        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(basic(client))
