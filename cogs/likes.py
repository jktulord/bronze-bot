import discord
import json
import random
from discord.ext import commands
import psycopg2
from urllib.parse import urlparse
import functs
import time


def DBconnect():
    # for python 3+ use: from urllib.parse import urlparse
    result = urlparse(
        "postgres://rxzevzulpptnsi:2c4a3df53f8e0668ec61b0eba19cdd003f577a5321eb1b987e3c10bb0ed5ca63@ec2-54-247-122-209.eu-west-1.compute.amazonaws.com:5432/d2s131ckgn5o6k")
    # also in python 3+ use: urlparse("YourUrl") not urlparse.urlparse("YourUrl")
    username = result.username
    password = result.password
    database = result.path[1:]
    hostname = result.hostname
    con = psycopg2.connect(
        database=database,
        user=username,
        password=password,
        host=hostname,
        port=5432
    )
    return con


def create_user(message):
    con = DBconnect()
    cur = con.cursor()

    author_id = str(message.author.id)
    name = str(message.author.name)
    guild_id = str(message.guild.id)

    cur.execute("SELECT * FROM users WHERE user_id = %s AND guild_id = %s", (author_id, guild_id))
    user = cur.fetchone()

    if not user:
        print("user", author_id, guild_id, "created")
        cur.execute("INSERT INTO users (user_id, name, guild_id, level, xp, likes, recieved_likes, free_likes) VALUES "
                    "(%s, %s, %s, 1, 0, 0, 0, 0)", (author_id, name, guild_id))

    print(user)

    con.commit()

    cur.close()
    con.close()

    return user


def give_likes(message, name):
    con = DBconnect()
    cur = con.cursor()

    reciever = discord.utils.get(message.author.guild.members, name=name)

    author_id = str(message.author.id)
    guild_id = str(message.guild.id)
    reciever_id = str(reciever.id)

    cur.execute("UPDATE users SET free_likes = %s WHERE user_id = %s AND guild_id = %s", (0, author_id, guild_id))
    cur.execute("SELECT * FROM users WHERE user_id = %s AND guild_id = %s", (author_id, guild_id))
    giv = cur.fetchone()
    cur.execute("SELECT * FROM users WHERE user_id = %s AND guild_id = %s", (reciever_id, guild_id))
    rec = cur.fetchone()
    cur.execute("UPDATE users SET free_likes = %s WHERE user_id = %s AND guild_id = %s", (0, author_id, guild_id))
    cur.execute("UPDATE users SET likes = %s WHERE user_id = %s AND guild_id = %s", (rec[5] + 1, reciever_id, guild_id))
    cur.execute("UPDATE users SET recieved_likes = %s WHERE user_id = %s AND guild_id = %s",
                (rec[6] + 1, reciever_id, guild_id))

    print("апдейт епт")
    con.commit()

    cur.close()
    con.close()

    return [giv, rec]


def midnight_update():
    con = DBconnect()
    cur = con.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    for i in users:
        cur.execute("UPDATE users SET free_likes = %s WHERE user_id = %s AND guild_id = %s", (1, i[0], i[2]))

    print("апдейт епт")
    con.commit()

    cur.close()
    con.close()


class likes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.....")

    @commands.command(aliases=['статус', 'Статус', 'Status'])
    async def status(self, ctx):
        await ctx.send("Статус")
        user = create_user(ctx.message)
        embed = functs.status_embed(ctx, user)
        await ctx.send(embed=embed)

    @commands.command()
    async def midnight(self, ctx):
        await ctx.send("Полночь")
        midnight_update()

    @commands.command()
    async def give(self, ctx, name):
        create_user(ctx.message)
        gl = give_likes(ctx.message, name)
        embed = functs.give_embed(ctx, gl[0], gl[1])
        await ctx.send(embed=embed)

def setup(client):
    client.add_cog(likes(client))
