import discord
from discord.utils import get
from discord.ext import commands
from datetime import datetime, timedelta
from music import songAPI

#client = discord.Client()

message_lastseen = datetime.now()
message2_lastseen = datetime.now()

# Prtfix หรือ เครื่องหมายคำสั่ง
bot = commands.Bot(command_prefix='!')

songsInstance = songAPI()


#Login Status
@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

#open music เปิดเพลง
@bot.command() 
async def play(ctx,* ,search: str):
    await songsInstance.play(ctx, search)

@bot.command()
async def stop(ctx):
    await songsInstance.stop(ctx)

@bot.command()
async def pause(ctx):
    await songsInstance.pause(ctx)

@bot.command()
async def resume(ctx):
    await songsInstance.resume(ctx)

@bot.command()
async def leave(ctx):
    await songsInstance.leave(ctx)

@bot.command()
async def queueList(ctx):
    await songsInstance.queueList(ctx)

@bot.command()
async def skip(ctx):
    await songsInstance.skip(ctx)

# Token Key
bot.run('token')