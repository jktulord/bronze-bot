import discord
import json
import random
from discord.ext import commands
import functs
import psycopg2
import time

def DBconnect():
    con = psycopg2.connect(dbname='d1q1hn2qfdpfnp', user='uazfysibugwxbd',
                        password='e05f0827db045c3f6ab032518c87a4c6590724a5558ff69434f427ab42fa5c72',
                        host='ec2-54-247-79-178.eu-west-1.compute.amazonaws.com',
                        port='5432')
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
        cur.execute("INSERT INTO users (user_id, name, guild_id, level, xp, likes, recived_likes, free_likes) VALUES "
                    "(%s, %s, %s, 1, 0, 0, 0, 0)", (author_id, name, guild_id))
    
    print(user)

    con.commit()

    cur.close()
    con.close()


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
        create_user(ctx.message)

    @commands.command()
    async def midnight(self, ctx):
        await ctx.send("Полночь")
        create_user(ctx.message)
        midnight_update()

def setup(client):
    client.add_cog(likes(client))