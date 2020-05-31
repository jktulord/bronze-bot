import discord
import json
import random
from discord.ext import commands
import functs
import psycopg2

def DBconnect():
    con = psycopg2.connect(dbname='d1q1hn2qfdpfnp', user='uazfysibugwxbd',
                        password='e05f0827db045c3f6ab032518c87a4c6590724a5558ff69434f427ab42fa5c72',
                        host='ec2-54-247-79-178.eu-west-1.compute.amazonaws.com',
                        port='5432')
    return con


def users_show():
    con = DBconnect()
    cur = con.cursor()

    cur.execute("INSERT INTO id")

    cur.execute("SELECT id, name FROM users")

    rows = cur.fetchall

    for r in rows:
        print(f"id{r[0]} name {r[1]}")

    cur.close()
    con.close()

def update_user(message):
    con = DBconnect()
    cur = con.cursor()

    author_id = str(message.author.id)
    guild_id = str(message.guild.id)

    user = cur.fetch("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)

    if not user:
        await cur.fetch.execute("INSERT INTO users (user_id, guild_id, level, likes, free_likes) VALUES ($1, $2, 1, 0, 0")

    user = cur.fetchrow("SELECT * FROM users WHERE user_id = $1 AND guild_id = $2", author_id, guild_id)
    await cur.execute("UPDATE users SET free_likes = $1 WHERE user_id = $2 AND guild_id = $3", 1, user['user_id'], user['guild_id'])
    print(user)

class likes(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.....")

    @commands.command(aliases=['статус', 'Статус', 'Status'])
    async def status(self, ctx):
        ctx.send("Статус")
        update_user(ctx.message)


def setup(client):
    client.add_cog(likes(client))