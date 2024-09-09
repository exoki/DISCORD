import discord
from discord.ext import commands
from DANNIE import *

# Создаем экземпляр бота
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello! I'm a bot.")


@bot.command(name="kick")
async def kick(ctx: discord.Message, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)


@bot.event
async def on_message(ctx):
    if ctx.author == bot.user:
        return
    print(ctx.content)
    await bot.process_commands(ctx)

bot.run(TOKEN)


"""
1. Чекнуть, как можно удалить сообщение в дискорде на пайтоне
2. Чекнуть, как можно поменять статус бота (типа: стримит/слушает/не беспокоить и т.д.)
"""