from datetime import timedelta
from discord.utils import utcnow
import discord
from discord.ext import commands, tasks
from DANNIE import *

# Создаем экземпляр бота
intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix="!", intents=intents)
blacklist = ["мияги", "анна асти", "макан"]
ID = 1285234316456235090


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    await bot.change_presence(activity=discord.Game(name="хэви метал 2"))
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="хэви метал 2"))
    await bot.change_presence(activity=discord.Streaming(name="хэви метал 2", url="https://www.twitch.tv/fenecsofia"))
    await bot.change_presence(status=discord.Status.online)
    await bot.change_presence(status=discord.Status.idle)
    await bot.change_presence(status=discord.Status.do_not_disturb)
    await bot.change_presence(status=discord.Status.invisible)
    await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.competing, name="в чемпионате"))


@tasks.loop(seconds=3)
async def sec():
    mykanal = bot.get_channel(ID)
    if mykanal is not None:
        await mykanal.send("канал")


@bot.command(name="hello")
async def hello(ctx):
    await ctx.send("Hello! I'm a bot.")
    await ctx.message.delete()
    sec.start()


@bot.command(name="kick")
async def kick(ctx: discord.Message, user: discord.Member, *, reason=None):
    await user.kick(reason=reason)


@bot.command(name="mute")
async def timeout(ctx, member: discord.Member, mute_time=1, *, reason='Нарушение правил сервера'):
    time = utcnow()+timedelta(minutes=mute_time)
    print(time)
    await member.timeout(time)
    await ctx.send(f'Участник {member.mention} был замучен.\nПричина: {reason}')


@bot.command(name="ban")
async def ban(ctx: discord.Message, user: discord.Member, *, reason=None):
    await user.ban(reason=reason)
    await ctx.channel.send(file=discord.File("D:\Изображения\Картинки\d.jpg"))


@bot.command(name="join")
async def join(ctx: discord.Message):
    print(ctx.author.voice)
    if ctx.author.voice is None:
        await ctx.send('чел не в канале')
        return
    kanal = ctx.author.voice.channel
    if ctx.voice_client is not None:
        pass
    else:
        await kanal.connect()


@bot.command(name="unban")
async def kick(ctx: discord.Message, user: str):
    pass
    #await ctx.channel.send(file=discord.File("D:\Изображения\Картинки\d.jpg"))


@bot.event
async def on_message(ctx: discord.Message):
    if ctx.author == bot.user:
        return
    print(ctx.content)
    await bot.process_commands(ctx)
    if ctx.content.lower() in blacklist:
        await ctx.delete()
        await ctx.channel.send(f"{ctx.author.mention} написал - {ctx.content.lower()}")
        await ctx.channel.send(file=discord.File("D:\Изображения\Картинки\d.jpg"))


bot.run(TOKEN)


"""
1. 
"""