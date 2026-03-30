def setup(bot):
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