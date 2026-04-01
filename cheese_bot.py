import discord
import os

TOKEN = os.getenv("MTQ4ODIxOTMwODE4OTU1Mjg3Mg.GZF7aG.l8eAa1aN7yPjPkp6woAnttHbdUlyMDMuRLfpWQ")
YOUR_USER_ID = 1317149550850342922

CHEESE_PUNS = [
    "That's grate! 🧀", "Cheese the day!", "You're looking sharp today!",
    "You gouda be kidding me!", "This is nacho average message!", "I'm cheddar than you!"
]

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"✅ Cheese Bot is online as {client.user}")
    print("🧀 Auto-reaction + random puns ENABLED (with debug)")

@client.event
async def on_message(message):
    if message.author.bot:
        return

    content = message.content.lower()
    if "cheese" in content:
        words = message.content.split()
        cheesy_word = next((w for w in words if "cheese" in w.lower()), "cheese")

        # === AUTO REACTION WITH DEBUG ===
        try:
            await message.add_reaction("🧀")
            print(f"✅ Added 🧀 reaction to message in {message.channel.name}")
        except Exception as e:
            print(f"❌ Reaction failed: {e}")

        # === RANDOM PUN (35% chance) ===
        if message.guild and random.random() < 0.35:
            pun = random.choice(CHEESE_PUNS)
            try:
                await message.channel.send(pun)
                print(f"✅ Sent pun in {message.channel.name}")
            except Exception as e:
                print(f"❌ Pun failed: {e}")

        # === DM YOU ===
        user = await client.fetch_user(YOUR_USER_ID)
        if user:
            try:
                await user.send(
                    f"**someone sayed \"{cheesy_word}\"** 🧀\n"
                    f"**Server:** {message.guild.name if message.guild else 'DM'}\n"
                    f"**Channel:** {message.channel.mention if message.guild else 'DM'}\n"
                    f"**Message:** {message.content}\n"
                    f"**Jump:** {message.jump_url}"
                )
            except:
                print("⚠️ Could not DM you")

client.run(TOKEN)

