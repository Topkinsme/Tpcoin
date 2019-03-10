#a bot by top

import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time


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
    '''Checks if the bot is online.'''
    print("pong")
    await ctx.send("Pong")

@cbot.command()
async def logout(ctx):
    '''Turns off the bot<Top only>'''
    ath=ctx.message.author
    id = int(ath.id) 
    if id== 299000787814842368 :
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
    '''Starts the value cycle'''
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
    '''Assigns money to people<Top only>'''
    a = int(ctx.author.id)
    if a == 299000787814842368:
        id=ctx.author.id
        money[id] =int(val)
        await ctx.send("Assigned.")
    else:
        await ctx.send("You do not have permission!")

@cbot.command()
async def assigntpcoin(ctx,user:discord.Member,val):
    '''Assigns Tp Coins to people<Top only>'''
    a = int(ctx.author.id)
    if a == 299000787814842368:
        id=ctx.author.id
        tpc[id] =int(val)
        await ctx.send("Assigned.")
    else:
        await ctx.send("You do not have permission!")

@cbot.command()
async def buy(ctx,aount):
    '''Use this to buy Tp coins.Type the amount of money you want to spend.'''
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
    '''Use this to sell Tp coins.Type the number of Tp coins you want to sell.'''
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
    '''Tells you your balance'''
    id= ctx.author.id
    await ctx.send("You own {} tpcoin.Also your balance is{}" .format(tpc[id],money[id]))

@cbot.command()
async def lead(ctx):
    '''Shows the leader board <WARNING SPAM!!!!!>'''
    for a in money:
        await ctx.send("<@{}> , :- {}" .format(a,money[a]))

@cbot.command()
async def makeacc(ctx):
    '''Makes you an account.Use this is .buy and .sell are not working for you.'''
    if not ctx.author.id in money and not ctx.author.id in tpc:
        money[ctx.author.id]=64
        tpc[ctx.author.id]=0
        await ctx.send("Account made.")
    else:
        await ctx.send("You already have an account.")

@cbot.command()
async def cvalue(ctx):
    '''Tells you the current value of 1 money in Tp coins.'''
    global rvalue
    await ctx.send("The current value is {}" .format(rvalue))


cbot.run(token)
