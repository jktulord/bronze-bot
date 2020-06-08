import discord
import json
import random
from discord.ext import commands
import psycopg2
from urllib.parse import urlparse
import functs
import time

COPPER_ORE = "Медная руда" #3
TIN_ORE = "Оловянная руда" #4
BRONZE_INGOT = "Бронзовые слитки" #5
UNDEFINED_ORE = "Неопределенная руда" #6


class res():
    def __init__(self, copper=0, tin=0, bronze=0):
        self.dict = {COPPER_ORE: copper, TIN_ORE: tin, BRONZE_INGOT: bronze}

    def line(self):
        line = ""
        for i in self.dict:
            if self.dict[i] != 0:
                line += i + str(self.dict[i]) + ' '
        return line



class recipe(object):
    def __init__(self, name, tag, req_dict, out_dict):
        self.name = name
        self.tag = tag
        self.req_dict = req_dict
        self.out_dict = out_dict

class recipe_shop(object):
    def __init__(self, name, tag, req_dict, out_funct):
        self.name = name
        self.tag = tag
        self.req_dict = req_dict
        self.out_funct = out_funct


bronze_recipe = recipe("Бронзовый Слиток", "bronze", res(copper=4, tin=2), res(bronze=2))
recipes = [bronze_recipe]

promote1 = recipe("Повышение до Бронзовенят", "promote", res(bronze=1), res())
choose_color = recipe("Выбрать цвет", "color", res(bronze=3), res())
call_to_max = recipe("Вовозвание к Максу", "call_to_Max", res(bronze=5), res())
shoplist = [promote1, choose_color, call_to_max]


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


def get_user(message):
    con = DBconnect()
    cur = con.cursor()

    author_id = str(message.author.id)
    name = str(message.author.name)
    guild_id = str(message.guild.id)

    cur.execute("SELECT * FROM users WHERE user_id = %s AND guild_id = %s", (author_id, guild_id))
    user = cur.fetchone()

    if not user:
        print("user", author_id, guild_id, "created")
        cur.execute("INSERT INTO users (user_id, name, guild_id, copper_ore, tin_ore, bronze_ore, undefined_ore) VALUES"
                    "(%s, %s, %s, 0, 0, 0, 3)", (author_id, name, guild_id))

    if user[3] is None:
        cur.execute(
            "UPDATE users SET copper_ore = %s, tin_ore=%s, bronze_ingot=%s, undefined_ore=%s WHERE user_id = %s AND guild_id = %s",
            (0, 0, 0, 3, author_id, guild_id))

    print(user)

    con.commit()

    cur.close()
    con.close()

    return user


def give_undefined_ore(message, name):
    con = DBconnect()
    cur = con.cursor()

    reciever = discord.utils.get(message.author.guild.members, name=name)

    author_id = str(message.author.id)
    guild_id = str(message.guild.id)
    reciever_id = str(reciever.id)

    cur.execute("SELECT * FROM users WHERE user_id = %s AND guild_id = %s", (author_id, guild_id))
    giv = cur.fetchone()
    cur.execute("SELECT * FROM users WHERE user_id = %s AND guild_id = %s", (reciever_id, guild_id))
    rec = cur.fetchone()

    res_given = res()
    print(giv[6] + 1)
    for i in range(giv[6]):
        rnd = random.randint(1, 100)
        if rnd > 33:
            cur.execute("UPDATE users SET copper_ore = %s WHERE user_id = %s AND guild_id = %s",
                        (rec[3] + 1, reciever_id, guild_id))
            res_given[COPPER_ORE] += 1
        else:
            cur.execute("UPDATE users SET tin_ore = %s WHERE user_id = %s AND guild_id = %s",
                        (rec[4] + 1, reciever_id, guild_id))
            res_given[TIN_ORE] += 1

    cur.execute("UPDATE users SET undefined_ore = %s WHERE user_id = %s AND guild_id = %s", (0, author_id, guild_id))

    print("апдейт епт")
    con.commit()

    cur.close()
    con.close()

    return [giv, rec, res_given]


def midnight_update():
    con = DBconnect()
    cur = con.cursor()

    cur.execute("SELECT * FROM users")
    users = cur.fetchall()

    for i in users:
        cur.execute("UPDATE users SET undefined_ore = %s WHERE user_id = %s AND guild_id = %s", (3, i[0], i[2]))

    print("апдейт епт")
    con.commit()

    cur.close()
    con.close()


class ore(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Bot is online.....")

    @commands.command(aliases=['статус', 'Статус', 'Status'])
    async def status(self, ctx):
        user = get_user(ctx.message)
        embed = functs.status_embed(ctx, user)
        await ctx.send(embed=embed)

    @commands.command()
    async def midnight(self, ctx):
        await ctx.send("Полночь")
        midnight_update()

    @commands.command()
    async def give(self, ctx, name):
        get_user(ctx.message)
        gl = give_undefined_ore(ctx.message, name)
        embed = functs.give_embed(ctx, gl[0], gl[1], gl[2])
        await ctx.send(embed=embed)

    @commands.command()
    async def craft(self, ctx, name="1"):
        if name == "1":
            embed = functs.craft_list_embed(ctx, recipes)
            await ctx.send(embed=embed)



def setup(client):
    client.add_cog(ore(client))
