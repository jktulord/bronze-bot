import discord
from discord.ext import commands
import psycopg2
from urllib.parse import urlparse
import time
import random
import functs
from ore import recipe


def DBconnect():
    # for python 3+ use: from urllib.parse import urlparse
    result = urlparse(
        "postgres://rxzevzulpptnsi:2c4a3df53f8e0668ec61b0eba19cdd003f577a5321eb1b987e3c10bb0ed5ca63@ec2-54-247-122"
        "-209.eu-west-1.compute.amazonaws.com:5432/d2s131ckgn5o6k")
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
COPPER_ORE = "Медная руда"  # 3
TIN_ORE = "Оловянная руда"  # 4
BRONZE_INGOT = "Бронзовый слиток"  # 5
UNDEFINED_ORE = "Неопределенная руда"  # 6

res_keys_dict = {COPPER_ORE: "item_№1", TIN_ORE: "item_№2", BRONZE_INGOT: "item_№3", UNDEFINED_ORE: "item_№4"}


def convert_to_dict(user_array):
    user_dict = [{USER_ID: user_array[0], NAME: user_array[1], GUILD_ID: user_array[2]},
                 recipe.res_dict(copper_ore=user_array[3], tin_ore=user_array[4], bronze_ore=user_array[5],
                                 undefined_ore=user_array[6])]
    return user_dict


def convert_to_dict_and_delete(user_array):
    user_dict = [{USER_ID: user_array[0], NAME: user_array[1], GUILD_ID: user_array[2]},
                 recipe.res_dict(copper_ore=user_array[3], tin_ore=user_array[4], bronze_ore=user_array[5],
                          undefined_ore=user_array[6])]
    del user_array
    return user_dict


def convert_fetch_dict_to_array(user_dict):
    user_array = []
    for i in user_dict:
        for j in i:
            user_array.append(j[i])

    return user_array


def check_craft_items(user_dict, req_dict):
    result = True
    for i in user_dict[1]:
        if user_dict[1][i] < req_dict[i]:
            result = False
            print(i, user_dict[1][i], "<", req_dict[i])
    return result


def add_items(user_dict, add_dict):
    for i in user_dict[1]:
        user_dict[1][i] += add_dict[i]
    return user_dict


def sub_items(user_dict, add_dict):
    for i in user_dict[1]:
        user_dict[1][i] -= add_dict[i]
    return user_dict


# Функции execute
def create_user(cur, author_id, name, guild_id):
    command_line = "INSERT INTO inventory_table (user_id, name, guild_id, item_№1, item_№2, item_№3, item_№4, " \
                   "item_№5, item_№6, item_№7, item_№8, item_№9, item_№10) VALUES (%s, %s, %s, 0, 0, 0, 0, 0, 0, 0, " \
                   "0, 0, 0) "
    cur.execute(command_line, (author_id, name, guild_id))


def update_items_to_user(cur, author_id, guild_id, copper_ore=0, tin_ore=0, bronze_ingot=0, undefined_ore=0):
    command_line_update = "UPDATE inventory_table "
    command_line_set = "SET"
    command_line_values = []
    dot_trigger = False

    if copper_ore != 0:
        if dot_trigger:
            command_line_set += ","
        command_line_set += " " + res_keys_dict[COPPER_ORE] + "=%s"
        command_line_values.append(copper_ore)
        dot_trigger = True

    if tin_ore != 0:
        if dot_trigger:
            command_line_set += ","
        command_line_set += " " + res_keys_dict[TIN_ORE] + "=%s"
        command_line_values.append(tin_ore)
        dot_trigger = True

    if bronze_ingot != 0:
        if dot_trigger:
            command_line_set += ","
        command_line_set += " " + res_keys_dict[BRONZE_INGOT] + "=%s"
        command_line_values.append(bronze_ingot)
        dot_trigger = True

    if undefined_ore != 0:
        if dot_trigger:
            command_line_set += ","
        command_line_set += " " + res_keys_dict[UNDEFINED_ORE] + "=%s"
        command_line_values.append(undefined_ore)
        dot_trigger = True

    command_line = command_line_update + command_line_set + " WHERE user_id=%s AND guild_id=%s"
    command_line_values.append(author_id)
    command_line_values.append(guild_id)
    cur.execute(command_line, command_line_values)


def update_items_to_user_from_dict(cur, author_id, guild_id, user_dict):
    update_items_to_user(cur, author_id, guild_id, copper_ore=user_dict[1][COPPER_ORE], tin_ore=user_dict[1][TIN_ORE],
                         bronze_ingot=user_dict[1][BRONZE_INGOT], undefined_ore=user_dict[1][UNDEFINED_ORE])


def get_user_inventory(message):
    con = DBconnect()
    cur = con.cursor()

    author_id = str(message.author.id)
    name = str(message.author.name)
    guild_id = str(message.guild.id)

    cur.execute("SELECT * FROM inventory_table WHERE user_id=%s AND guild_id=%s", (author_id, guild_id))
    user_array = cur.fetchone()

    if not user_array:
        print("user", author_id, guild_id, "created")
        create_user(cur, author_id, name, guild_id)

        cur.execute("SELECT * FROM inventory_table WHERE user_id=%s AND guild_id=%s", (author_id, guild_id))
        user_array = cur.fetchone()

    print(user_array)

    con.commit()

    cur.close()
    con.close()

    return user_array


def craft_item(message, user_array, cur_recipe):
    con = DBconnect()
    cur = con.cursor()

    author_id = str(message.author.id)
    name = str(message.author.name)
    guild_id = str(message.guild.id)

    user_dict = convert_to_dict(user_array)
    result = False

    if check_craft_items(user_dict, cur_recipe.req_dict):
        sub_items(user_dict, cur_recipe.req_dict)
        add_items(user_dict, cur_recipe.out_dict)
        update_items_to_user_from_dict(cur, author_id, guild_id, user_dict)
        result = True
    else:
        result = False

    con.commit()
    cur.close()
    con.close()

    return result


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
        
    @commands.command()
    async def midnight(self, ctx):
        await ctx.send("Полночь")
        midnight_update()
    """

    @commands.command()
    async def get_copper(self, ctx, amount):
        await ctx.send("Полночь")
        user_dict = convert_to_dict(get_user_inventory(ctx.message))
        con = DBconnect()
        cur = con.cursor()

        update_items_to_user(cur, user_dict[0][USER_ID], user_dict[0][GUILD_ID], copper_ore=amount)

        del user_dict
        con.commit()
        cur.close()
        con.close()

    @commands.command()
    async def get_tin(self, ctx, amount):
        await ctx.send("Полночь")
        user_dict = convert_to_dict(get_user_inventory(ctx.message))
        con = DBconnect()
        cur = con.cursor()

        update_items_to_user(cur, user_dict[0][USER_ID], user_dict[0][GUILD_ID], tin_ore=amount)

        del user_dict
        con.commit()
        cur.close()
        con.close()

    @commands.command()
    async def craft(self, ctx, word=None):
        if word is None:
            embed = functs.craft_list_embed(ctx)
            await ctx.send(embed=embed)
        else:
            user_array = get_user_inventory(ctx.message)
            try:
                word = int(word)
                cur_recipe = recipe.get_recipe(num=word)
            except ValueError:
                cur_recipe = recipe.get_recipe(name=word, tag=word)
            if cur_recipe is not None:
                if craft_item(ctx.message, user_array, cur_recipe):
                    embed = functs.text_embed(text=ctx.message.author.name + " скрафтил " + cur_recipe.name)
                    await ctx.send(embed=embed)
                else:
                    embed = functs.text_embed(text=ctx.message.author.name + " НЕ скрафтил " + cur_recipe.name)
                    await ctx.send(embed=embed)
            else:
                embed = functs.text_embed(text="Не найден рецепт")
                await ctx.send(embed=embed)


def setup(client):
    client.add_cog(ore2(client))
