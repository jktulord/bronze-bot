import discord


def text_embed(text, name='BronzeTech-0.2.0'):
    embed = discord.Embed(
        Title='Title',
        description=text,
        colour=discord.Color.orange()
    )
    embed.set_author(name=name)

    return embed


def status_embed(ctx, likes, free_likes, recieved_likes):
    embed = discord.Embed(
        Title='Title',
        description='This is your stats',
        colour=discord.Color.orange()
    )
    embed.set_author(name=ctx.message.author.name)

    embed.add_field(name='Текущие Лайки', value=likes, inline=True)
    embed.add_field(name='Доступные Лайки', value=free_likes, inline=True)
    embed.add_field(name='Полученые Лайки', value=recieved_likes, inline=True)


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
