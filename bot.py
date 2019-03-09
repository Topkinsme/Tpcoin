#a bot by top

import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random

token="NTUzNzc4NDI0MTMzNDUxODA0.D2TB4Q.bCBNKMnUOku_8yUt8-tUbgCrA6E"

cbot = commands.Bot(command_prefix = ".")

@cbot.event
async def on_ready():
   print("Ye boi is up!")
   await cbot.change_presence(activity=discord.Game(name="With Top!", type = 2))
   a=cbot.get_channel(533992960459538433)
   await a.send("Ye boi is up!")

@cbot.command()
async def ping(ctx):
    print("pong")
    await ctx.send("Pong")

@cbot.command()
async def logout(ctx):
    ath=ctx.message.author
    rol=str(ath.top_role)
    if rol=="Bot_Maker" or rol=="ADMINISTRATOR" :
        await ctx.send("Bye bye!")
        await cbot.logout()
    else:
        await ctx.send("You do not have permission!")
        pass

cbot.run(token)
