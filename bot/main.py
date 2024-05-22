import discord
from discord.ext import commands
import os

# Load environment variables
from dotenv import load_dotenv
load_dotenv()
TOKEN = os.getenv('DISCORD_TOKEN')

# Create bot instance
bot = commands.Bot(command_prefix='!')

# Load all commands
bot.load_extension('commands.kick')
bot.load_extension('commands.ban')
bot.load_extension('commands.mute')
bot.load_extension('commands.warn')

# Run the bot
bot.run(TOKEN)