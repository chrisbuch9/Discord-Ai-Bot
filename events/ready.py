import discord

def setup(bot):
    @bot.event
    async def on_ready(): 
        await bot.change_presence(activity=discord.Activity(
            type=discord.ActivityType.listening, 
            name="!help | Ask me anything!"
        )
    )
    print(f"Logged in as {bot.user}")
    print(bot.commands)