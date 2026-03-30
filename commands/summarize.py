from core.ai_client import client

def setup(bot):
    @bot.command()
    async def summarize(ctx):
        
        if ctx.message.reference is None:
            await ctx.send("Please reply to a message to summarize it.")
            return

        replied_message = await ctx.channel.fetch_message(
            ctx.message.reference.message_id
        )

        prompt = (
            f"{replied_message.content}\n\n"
            "Summarize this message in a detailed but concise manner, "
            "keeping it under 1800 characters."
        )

        try:
            response = client.models.generate_content(
                model="gemini-2.5-flash",
                contents=prompt
            )
        except Exception:
            await ctx.send("An error occurred while generating the summary.")
            return

        reply = response.text or "No response"

        if len(reply) > 1900:
            reply = reply[:1897] + "..."

        await ctx.send(reply)