import discord
from discord.ext import commands

intents = discord.Intents.default() #
intents.message_content = True #enables reading messages

bot = commands.Bot(
    command_prefix="!", 
    intents=intents, 
    help_command=None
) #creates bot instance with ! as command prefix and disables default help command