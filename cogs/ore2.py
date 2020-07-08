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

USER_ID = "user_id"
NAME = "name"
GUILD_ID = "guild_id"
COPPER_ORE = "copper_ore"  # 3
TIN_ORE = "tin_ore"  # 4
BRONZE_INGOT = "bronze_ingot"  # 5
UNDEFINED_ORE = "undefined_ore"  # 6

res_dict = {COPPER_ORE: "item_№1", TIN_ORE: "item_№2", BRONZE_INGOT: "item_№3", UNDEFINED_ORE: "item_№4"}

def convert_fetch_dict(fet):
    user_dict = {USER_ID: fet[0], NAME: fet[1], GUILD_ID: fet[2], BRONZE_INGOT: fet[3], UNDEFINED_ORE: fet[4],
                  COPPER_ORE: fet[5], TIN_ORE: fet[6]}
    return user_dict

# Функции execute
def create_user(cur, author_id, name, guild_id):
    cur.execute("INSERT INTO inventory_table "
                "(user_id, name, guild_id, "
                "item_№1, item_№2, item_№3, item_№4, item_№5, item_№6, item_№7, item_№8, item_№9, item_№10) "
                "VALUES (%s, %s, %s, "
                "0, 0, 0, 0, 0, 0, 0, 0, 0, 0)",
                (author_id, name, guild_id))


def get_user(message):
    con = DBconnect()
    cur = con.cursor()

    author_id = str(message.author.id)
    name = str(message.author.name)
    guild_id = str(message.guild.id)

    cur.execute("SELECT * FROM inventory_table WHERE user_id = %s AND guild_id = %s", (author_id, guild_id))
    user = cur.fetchone()

    if not user:
        print("user", author_id, guild_id, "created")
        create_user(cur, author_id, name, guild_id)

        cur.execute("SELECT * FROM inventory_table WHERE user_id = %s AND guild_id = %s", (author_id, guild_id))
        user = cur.fetchone()

    print(user)

    con.commit()

    cur.close()
    con.close()

    return user



class ore2(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.....")
    """
    @commands.command(aliases=['статус', 'Статус', 'Status'])
    async def status(self, ctx):
        user = get_user(ctx.message)
        embed = functs.status_embed(ctx, user)
        await ctx.send(embed=embed)
    """



def setup(client):
    client.add_cog(ore2(client))
