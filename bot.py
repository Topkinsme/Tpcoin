#a bot by top

import json
import discord
import logging
from discord.utils import get
from discord.ext import commands
from discord.ext.commands import Bot
import asyncio
import random
import time


token = "Your Token"
startcycle=0

cbot = commands.Bot(command_prefix = ".")
cbot.remove_command('help')

@cbot.event
async def on_ready():
   global money
   global rvalue
   global tpc
   global smnum
   print("Ye boi is up!")
   await cbot.change_presence(activity=discord.Game(name="Type .makeacc to get started!Type .help for more info !", type = 2))
   a=cbot.get_channel(533992960459538433)
   await a.send("Ye boi is up!")
   try:
        with open('money.json','r') as f:
            money = json.load(f)
            print(money)
   except:
            print("Could not load the data")
            money = {}
   try:
        with open('rvalue.json','r') as f:
            rvalue = json.load(f)
            print(rvalue)
   except:
            print("Could not load the data")
            rvalue = 16   
   try:
        with open('tpc.json','r') as f:
            tpc = json.load(f)
            print(rvalue)
   except:
            print("Could not load the data")
            tpc={}
   global loop
   store(money,rvalue,tpc)
   loop =1 
   smnum=1
   while loop==1:
      what= random.choice(value)
      if what == "up" :
         rvalue += 2
      elif what=="down":
         rvalue -=  2
         if rvalue<1:
            rvalue+=4
      print(rvalue)
      store(money,rvalue,tpc)
      await cbot.change_presence(activity=discord.Game(name="Type .makeacc to get started!Type .help for more info ! Current value=" + str(rvalue)))
      smnum=1
      await asyncio.sleep(3600)  
            

@cbot.event
async def on_member_join(a):
    global money
    global rvalue
    global tpc
    b= str(a.id)
    money[b]=64
    tpc[b]=0
    store(money,rvalue,tpc)





@cbot.command()
async def ping(ctx):
    '''Checks if the bot is online.'''
    print("pong")
    await ctx.send("Pong")

@cbot.command()
async def logout(ctx):
    '''Turns off the bot<Top only>'''
    global money
    global rvalue
    global tpc
    store(money,rvalue,tpc)
    ath=ctx.message.author
    id = int(ath.id) 
    if id== 299000787814842368 :
        await ctx.send("Bye bye!")
        await cbot.logout()
    else:
        await ctx.send("You do not have permission!")
        pass


loop=1

value=["up","down" ]

@cbot.command()
async def msg(ctx):
    '''send a message which updates you ont he vals'''
    global smnum
    aa=1
    while aa==1:
        await asyncio.sleep(600)
        while smnum==1:
            smunum=0
            await ctx.send("The current value for 1 money is :- {}" .format(rvalue))
            
   

@cbot.command()
async def assignmoney(ctx,user:discord.Member,val):
    '''Assigns money to people<Top only>'''
    global money
    global rvalue
    global tpc
    a = int(ctx.author.id)
    if a == 299000787814842368:
        id=str(user.id)
        money[id] =int(val)
        await ctx.send("Assigned.")
        store(money,rvalue,tpc)
    else:
        await ctx.send("You do not have permission!")
    
   
   

@cbot.command()
async def assigntpcoin(ctx,user:discord.Member,val):
    '''Assigns Tp Coins to people<Top only>'''
    global money
    global rvalue
    global tpc
    a = int(ctx.author.id)
    if a == 299000787814842368:
        id=str(user.id)
        tpc[id] =int(val)
        await ctx.send("Assigned.")
        store(money,rvalue,tpc)
    else:
        await ctx.send("You do not have permission!")

@cbot.command()
async def buy(ctx,aount):
    '''Use this to buy Tp coins.Type the amount of money you want to spend.'''
    global money
    global rvalue
    global tpc
    amount=int(aount)
    global rvalue
    id = str(ctx.author.id)
    num = rvalue * amount
    if amount > int(money[id]) :
        await ctx.send("You cannot afford this.")
    else:
        tpc[id] += num
        money[id] -= amount
        await ctx.send("You own {} tpcoin.Also your balance is {}" .format(tpc[id],money[id]))
    store(money,rvalue,tpc)

@cbot.command()
async def sell(ctx,aount):
    '''Use this to sell Tp coins.Type the number of Tp coins you want to sell.'''
    global money
    global rvalue
    global tpc
    amount=int(aount)
    global rvalue
    id = str(ctx.author.id)
    num = amount//rvalue
    if amount > int(tpc[id]):
        await ctx.send("You do not own that many tpcs.")
    else:
        tpc[id] -= amount
        money[id] += num
        await ctx.send("You own {} tpcoin.Also your balance is{}" .format(tpc[id],money[id]))
    store(money,rvalue,tpc)
    
@cbot.command()
async def bal(ctx):
    '''Tells you your balance'''
    id= str(ctx.author.id)
    await ctx.send("You own {} tpcoin.Also your balance is{}" .format(tpc[id],money[id]))

@cbot.command()
async def lead(ctx):
    '''Shows the leader board <WARNING SPAM!!!!!>'''
    global money
    global rvalue
    global tpc
    store(money,rvalue,tpc)
    for a in money:
        msg= await ctx.send("LOADING")
        await msg.edit(content = "<@{}> , :- {}" .format(a,money[a]))

@cbot.command()
async def makeacc(ctx):
    '''Makes you an account.Use this is .buy and .sell are not working for you.'''
    global money
    global rvalue
    global tpc
    user= str(ctx.author.id)
    if not user in money and not user in tpc:
        money[user]=64
        tpc[user]=0
        await ctx.send("Account made.")
        store(money,rvalue,tpc)
    else:
        await ctx.send("You already have an account. Try using .bal")
    print(money)

    
@cbot.command()
async def cvalue(ctx):
    '''Tells you the current value of 1 money in Tp coins.'''
    global money
    global rvalue
    global tpc
    store(money,rvalue,tpc)
    await ctx.send("The current value is {}" .format(rvalue))

@cbot.command()
async def help(ctx):
    help=discord.Embed(colour=discord.Colour.blue())
    help.set_author(name="HELP (Prefix = . )")
    help.add_field(name="What is this game?/I don't understand how to use this bot",value="This is a simulation of a sort of bitcoin simulator written by <@299000787814842368> \n You basically start with 64 currency which you can trade for TpCoins. The value of these TpCoins change every hour. The value can either be inflated or be depreciated. Trading doen't change the value , the value only changes periodically by the action of the bot.\n The aim is to collect the most coins(currency not TpCoins) and see the best way to do it .",inline="false")
    help.add_field(name="How can I get started?",value="To get started , you need an account.To make an account , type in .makeacc  .Then you can start buying and selling by .buy and .sell respectively.You can only buy and sell with what you own,(Obviously). To check your balance , use .bal and to check the value of the coins , use .cvalue  .That should be it. \n\n A list of all commands and what they do are given below. Have fun!",inline="false")
    help.add_field(name="Help",value="Displays this message",inline="false")
    help.add_field(name="Ping",value="Returns pong",inline="false")
    help.add_field(name="Logout",value="Turns off the bot",inline="false")
    help.add_field(name="msg",value="Sends an update message each time the value of 1 cp coin changes.(WARNING VERY BUGGY DOESN'T QUIET WORK....)",inline="false")
    help.add_field(name="Buy (Syntax = .buy <Number of coins>)",value="Allows you to buy TpCoins using currency",inline="false")
    help.add_field(name="Sell (Syntax = .sell <Number of TpCoins>)",value="Allows you to sell TpCoins for Currency",inline="false")
    help.add_field(name="Bal",value="Tells you your account balance.",inline="false")
    help.add_field(name="Lead",value="Prints out all the players and the currency they own. (WARNING CAUSES SPAM)",inline="false")
    help.add_field(name="Makeacc",value="Use this to make an account. Use this command if .buy and .sell or .bal aren't working for you.",inline="false")
    help.add_field(name="cvalue",value="Tell you the value of 1 currency in terms of TpCoins.",inline="false")
    await ctx.send(embed=help)

def store(money,rvalue,tpc):    
    with open('money.json', 'w+') as f:
        json.dump(money, f)
    with open('rvalue.json', 'w+') as f:
        json.dump(rvalue, f)
    with open('tpc.json', 'w+') as f:
        json.dump(tpc, f)

cbot.run(token)
