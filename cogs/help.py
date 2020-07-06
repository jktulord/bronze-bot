import discord
import json
import random
from discord.ext import commands
import functs


class help(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.command(aliases=['помощь'])
    async def help(self, ctx):
        embed = discord.Embed(
            color=discord.Color.orange()
        )

        embed.set_author(name=functs.NAME)

        embed.add_field(name='---!help----', value="Показывает это сообщение", inline=False)

        embed.add_field(name='-', value="-----Ролевые команды-----", inline=False)
        embed.add_field(name='---!getHots---', value="Получение Роли Хотсеры", inline=False)
        embed.add_field(name='---!getNews---', value="Новостная Подписка", inline=False)
        embed.add_field(name='---!pokonyam---', value="Зовет всех Хотсеров в Хотс", inline=False)
        embed.add_field(name='---!randomHero---',
                        value="Выдает случайного героя. Для работы требуются Теги. (список всех тегов: Все, ААтакеры, "
                              "Маги, Жир, Танки, Брузяхи, Лекари, Поддержка, Ебоклаки)",
                        inline=False)

        embed.add_field(name='-', value="-----Фановые команды-----", inline=False)
        embed.add_field(name='---!infinity---', value="Показывает Бесконечность", inline=False)
        embed.add_field(name='---!aleksey---', value="Отправляет сообщение СТУКОВ", inline=False)
        embed.add_field(name='---!stukhov---', value="Отправляет сообщение АЛЕКСЕЙ", inline=False)

        await ctx.send(embed=embed)


def setup(client):
    client.add_cog(help(client))
