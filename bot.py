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

#response = client.models.generate_content(
 #   model="gemini-2.5-flash",
 #   contents="Explain what a discord bot is in one sentence"
#)

#print(response.text)


intents = discord.Intents.default() #
intents.message_content = True #enables reading messages

bot = commands.Bot(command_prefix="!", intents=intents)


@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")
    print(bot.commands)


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
    


bot.run(TOKEN)