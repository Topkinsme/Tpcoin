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

@cbot.event
async def on_member_join(a):
    b= a.id
    money[b]=64
    tpc[b]=0

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

money = {}
tpc= {}
rvalue = 16
loop=1


value=["up" , "down" , "nothing"]

@cbot.command()
async def start(ctx):
    global loop
    loop =1 
    while loop==1:
        what= random.choice(value)
        global rvalue
        if what == "up" :
            rvalue += 2
        elif what=="down":
            rvalue -=  2
        await ctx.send("The current value for 1 money is :- {}" .format( rvalue))
        print(rvalue)
        await asyncio.sleep(3600)

@cbot.command()
async def assignmoney(ctx,user:discord.Member,val):
    a = str(ctx.author.top_role)
    if a == "Bot_Maker":
        id=ctx.author.id
        money[id] =int(val)
        await ctx.send("Assigned.")
    else:
        await ctx.send("You do not have permission!")

@cbot.command()
async def assigntpcoin(ctx,user:discord.Member,val):
    a = str(ctx.author.top_role)
    if a == "Bot_Maker":
        id=ctx.author.id
        tpc[id] =int(val)
        await ctx.send("Assigned.")
    else:
        await ctx.send("You do not have permission!")

@cbot.command()
async def buy(ctx,aount):
    amount=int(aount)
    global rvalue
    id = ctx.author.id
    num = rvalue * amount
    if amount > int(money[id]) :
        await ctx.send("You cannot afford this.")
    else:
        tpc[id] += num
        money[id] -= amount
        await ctx.send("You own {} tpcoin.Also your balance is{}" .format(tpc[id],money[id]))

@cbot.command()
async def sell(ctx,aount):
    amount=int(aount)
    global rvalue
    id = ctx.author.id
    num = amount/rvalue
    if amount > int(tpc[id]):
        await ctx.send("You do not own that many tpcs.")
    else:
        tpc[id] -= amount
        money[id] += num
        await ctx.send("You own {} tpcoin.Also your balance is{}" .format(tpc[id],money[id]))
    
@cbot.command()
async def bal(ctx):
    id= ctx.author.id
    await ctx.send("You own {} tpcoin.Also your balance is{}" .format(tpc[id],money[id]))

@cbot.command()
async def lead(ctx):
    await ctx.send(money)

@cbot.command()
async def stop(ctx):
    global loop
    loop = 0


@cbot.command()
async def makeacc(ctx):
    if not ctx.author.id in money and not ctx.author.id in tpc:
        money[ctx.author.id]=64
        tpc[ctx.author.id]=0
        await ctx.send("Account made.")
    else:
        await ctx.send("You already have an account.")

cbot.run(token)
