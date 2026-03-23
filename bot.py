import os
import discord
from discord.ext import commands
from dotenv import load_dotenv
from google import genai
import certifi

load_dotenv() #reads .env file
os.environ["SSL_CERT_FILE"] = certifi.where()

TOKEN = os.getenv("DISCORD_BOT_TOKEN") #grabs discord token


client = genai.Client(api_key=os.getenv("GEMINI_API_KEY"))

intents = discord.Intents.default() #
intents.message_content = True #enables reading messages

bot = commands.Bot(command_prefix="!", intents=intents, help_command=None) #creates bot instance with ! as command prefix and disables default help command


@bot.event
async def on_ready():
    
    await bot.change_presence(
        activity = discord.Activity(type=discord.ActivityType.listening, name="!help | Ask me anything!"))

    print(f"Logged in as {bot.user}")
    print(bot.commands)

@bot.command()
async def help(ctx):
    help_message = (
        "**Bot Commands**\n"
        "- !ping - Check if the bot is responsive.\n"
        "- !ask <question> - Ask the bot a question.\n"
        "- !summarize - Reply to a message with this command to get a summary of that message.\n"
        "- !help - Display this help message."
    )
    await ctx.send(help_message)

@bot.command()
async def ping(ctx):
    await ctx.send("Pong!")

@bot.command()
async def ask(ctx):
    user_message = ctx.message.content

    prompt = (f"{user_message[5:]}\n\n"
            "If the answer is simple, keep it very short. "
            "If more detail is needed, still stay under 1800 characters. "
            "Be concise and avoid unnecessary explanation."
            )

    response = client.models.generate_content(
    model="gemini-2.5-flash",
    contents=prompt
    )

    reply = response.text or "No response"

    if len(reply) > 1900:
        reply = reply[:1897] +"..."
    
    await ctx.send(reply)
    

@bot.command()
async def summarize(ctx):
    if ctx.message.reference is None:
        await ctx.send("Please reply to a message to summarize it.")
        return
    
    replied_message = await ctx.channel.fetch_message(ctx.message.reference.message_id)

    prompt = (f"{replied_message.content}\n\n"
              "Summarize this message in a detailed but concise manner,"
              "keeping it under 1800 characters."
              )
    
    response = client.models.generate_content(
        model="gemini-2.5-flash",
        contents=prompt
    )

    reply = response.text or "No response"

    if len(reply) > 1900:
        reply = reply[:1897] + "..."

    await ctx.send(reply)


bot.run(TOKEN)