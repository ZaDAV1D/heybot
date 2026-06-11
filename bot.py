import discord
import os
from discord.ext import commands
from flask import Flask
import threading

# ---------- DISCORD BOT ----------
intents = discord.Intents.default()
intents.members = True

bot = commands.Bot(command_prefix="!", intents=intents)

WELCOME_CHANNEL_ID = 1514711028905021511

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_member_join(member):
    channel = bot.get_channel(WELCOME_CHANNEL_ID)
    if channel:
        await channel.send(f"👋 היי ברוך הבא {member.mention} לשרת!")

# ---------- WEB SERVER ----------
app = Flask(__name__)

@app.route("/")
def home():
    return "✅ הבוט עובד! הכל תקין."

def run_web():
    app.run(host="0.0.0.0", port=10000)

# ---------- RUN BOTH ----------
threading.Thread(target=run_web).start()
bot.run(os.getenv("TOKEN"))
