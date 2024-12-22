import discord
from discord.ext import commands
import re

from valorant import rank_ctrl
import log

from token_file import *

# Configuration du bot
intents = discord.Intents.default()
intents.members = True
intents.message_content = True

bot = commands.Bot(command_prefix='+', intents=intents)

@bot.event
async def on_ready():
    await log.log_bot_ready(bot)
    print("valorant-bot is online and ready.")

@bot.command()
async def ping(ctx):
    print("+ping command executed by : ", ctx.author)
    response = f"Pong! ``{round(bot.latency * 1000)}ms``"
    await ctx.send(response)
    await log.log_command(ctx, response)

@bot.command()
async def rank(ctx, *, username_tag):
    print("+rank command exexuted by : ", ctx.author)
    match = re.match(r"(.+?)#(\w+)", username_tag)
    if match:
        username, tag = match.groups()
    else:
        parts = username_tag.rsplit(' ', 1)
        if len(parts) == 2:
            username, tag = parts
        else:
            response = "Format invalide. Utiliser  ``+rank username#tag``  ou  ``+rank username tag``"
            await ctx.send(response)
            await log.log_command(ctx, response)
            return
    controller = rank_ctrl(ctx, username, tag)
    await controller.get_rank()
    response = f"rank data fetched for ``{username}#{tag}``"
    await log.log_command(ctx, response)

@bot.command()
async def aide(ctx):
    print(f"+aide command executed by : {ctx.author}")
    embed = discord.Embed(title="Aide valorant-bot", color=discord.Color.blue())
    embed.add_field(name="Préfixe :", value="``+``")
    embed.add_field(name="Commandes : ", value = "``+aide`` ``+ping`` ``+rank``")
    embed.add_field(name="Informations commandes :", value="", inline=False)
    embed.add_field(name="``+aide``", value="Afficher ce message d'aide", inline=False)
    embed.add_field(name="``+ping``", value="Vérifier la latence du bot",inline=False)
    embed.add_field(name="``+rank username#tag``", value="Afficher le rang Valorant d'un joueur", inline=False)
    await ctx.send(embed=embed)
    await log.log_command(ctx, "+aide command executed with embed")

# Lancer le bot
if __name__ == "__main__":
    if TOKEN:
        print("Starting the bot...")
        bot.run(TOKEN)
    else:
        print("Discord token not found. Please check the token_file.py file.")
