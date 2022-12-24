import discord
import datetime
from discord.ext import commands

from urllib import parse
import requests
import re
import json

with open('config.json') as f:
    data = json.load(f)

intents = discord.Intents.all()
token = data[token]
prefix = data[prefix]
bot = commands.Bot(command_prefix=prefix, intents=intents)

@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command()
async def sum(ctx, numOne: int, numTwo: int):
    await ctx.send(numOne + numTwo)
    
@bot.command()
async def stats(ctx):
    embed = discord.Embed(title=f"{ctx.guild.name}",description="owo", timestamp=datetime.datetime.utcnow(), color=discord.Color.blue())
    embed.add_field(name="Server created at", value=f"{ctx.guild.created_at}")
    embed.add_field(name="Server Owner", value=f"{ctx.guild.owner}")
    await ctx.send(embed=embed)
    
@bot.command()
async def pic(ctx):
    response = requests.get("https://dog.ceo/api/breeds/image/random")
    image_link = response.json()["message"]
    await ctx.send(image_link)

# Events
@bot.event
async def on_ready():
    await bot.change_presence(activity=discord.Game(name="Siendo webon"))
    print("My bot is ready")

bot.run(token)
