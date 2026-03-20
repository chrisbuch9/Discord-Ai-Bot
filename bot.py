import os
import discord
from discord.ext import commands
from dotenv import load_dotenv

load_dotenv() #reads .env file

TOKEN = os.getenv("DISCORD_BOT_TOKEN") #grabs discord token

print(TOKEN)