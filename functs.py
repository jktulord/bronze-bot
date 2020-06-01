import discord


def text_embed(text, name='BronzeTech-0.1.9'):
    embed = discord.Embed(
        Title='Title',
        description=text,
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
