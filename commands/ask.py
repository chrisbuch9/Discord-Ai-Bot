from core.ai_client import client

def setup(bot):
    @bot.command()
    async def ask(ctx):
        user_message = ctx.message.content

        prompt = (f"{user_message[5:]}\n\n"
            "If the answer is simple, keep it very short. "
            "If more detail is needed, still stay under 1800 characters. "
            "Be concise and avoid unnecessary explanation."
            )

        try:
            response = client.models.generate_content(
            model="gemini-2.5-flash",
            contents=prompt
            )
        except Exception:
            await ctx.send("An error occurred while generating a response.")
            return

        reply = response.text or "No response"

        if len(reply) > 1900:
            reply = reply[:1897] +"..."
    
        await ctx.send(reply)