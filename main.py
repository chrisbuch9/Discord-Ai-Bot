from core.bot import bot
from config.settings import DISCORD_BOT_TOKEN
from events.ready import setup as ready_setup
from commands.ping import setup as ping_setup
from commands.help import setup as help_setup
from commands.ask import setup as ask_setup
from commands.summarize import setup as summarize_setup


help_setup(bot) #registers help command
ping_setup(bot) #registers ping command
ask_setup(bot) #registers ask command
summarize_setup(bot) #registers summarize command
ready_setup(bot) #registers on_ready event

bot.run(DISCORD_BOT_TOKEN) #starts the bot using the token from environment variables