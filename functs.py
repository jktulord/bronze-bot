import discord

NAME = 'BronzeTech-0.3.4 "Крикливый" Апдейт '

COPPER_ORE = "Медная руда"
TIN_ORE = "Оловянная руда"
BRONZE_INGOT = "Бронзовые слитки"
UNDEFINED_ORE = "Неопределенная руда"


def text_embed(text, name=NAME, color=discord.Color.orange()):
    embed = discord.Embed(
        Title='Title',
        description=text,
        colour=color
    )
    if name is not None:
        embed.set_author(name=name)

    return embed


def status_embed(ctx, user):
    embed = discord.Embed(
        Title='Title',
        description='Ваш баланс руды',
        colour=discord.Color.orange()
    )
    embed.set_author(name=ctx.message.author.name)

    embed.add_field(name='Медная руда', value=user[3], inline=True)
    embed.add_field(name='Оловянная руда', value=user[4], inline=True)
    embed.add_field(name='Бронзовые слитки', value=user[5], inline=True)
    embed.add_field(name='Неопределенная руда', value=user[6], inline=True)

    return embed


def give_embed(ctx, giv, rec, res_given, name=NAME):
    first = giv[1] + " великодушно отдал "
    second = ""
    for i in res_given:
        if res_given[i] > 0:
            second += str(res_given[i]) + i + ","
    third = "пользователю " + rec[1]
    embed = discord.Embed(
        Title='Title',
        description=first + second + third,
        colour=discord.Color.orange()
    )
    embed.set_author(name=name)

    return embed


def stats_embed(ctx):
    embed = discord.Embed(
        Title='Title',
        description='This is your stats',
        colour=discord.Color.orange()
    )
    embed.set_author(name=ctx.message.author.name)
    embed.add_field(name='Str', value='5', inline=True)
    embed.add_field(name='Dex', value='3', inline=True)
    embed.add_field(name='Hp', value='60/60', inline=True)

    embed.add_field(name='Agi', value='2', inline=True)
    embed.add_field(name='Int', value='3', inline=True)
    embed.add_field(name='Attk', value='8-5', inline=True)

    embed.add_field(name='Reg', value='+1,5', inline=True)
    embed.add_field(name='Crt', value='1,5%', inline=True)
    embed.add_field(name='AAspd', value='1,08', inline=True)
    embed.add_field(name='Ddg', value='4%', inline=True)

    return embed


def craft_list_embed(ctx, recipes):
    embed = discord.Embed(
        Title='Title',
        description='Рецепты',
        colour=discord.Color.light_grey()
    )
    for i in recipes:
        embed.add_field(name=i.name + " [" + i.tag + "] ", value=i.req_dict.line(), inline=True)
        embed.add_field(name="Получаемые ресурсы:", value=i.out_dict.line(), inline=True)
        embed.set_footer(text="используй !сraft [tag]")

    return embed

def embed_picture(ctx, name=NAME):
    embed = discord.Embed(
        Title='Title',
        colour=discord.Color.orange()
    )
    embed.set_author(name=name)
    embed.set_image(url="https://imgur.com/random")

    return embed