from datetime import datetime
import traceback
import os
from dotenv import load_dotenv

from nwprbygrl7.cogs.data import add_giveaway, get_prefix

import discord
from discord.ext import commands

intents = discord.Intents().all()


load_dotenv()


def _get_prefix(b, message):

    prefix = get_prefix()

    return commands.when_mentioned_or(prefix)(b, message)


bot = commands.Bot(command_prefix=_get_prefix, intents=intents, case_insensitive=True)
bot.remove_command("help")

cogs = [
    "cogs.commands",
    "cogs.events",
    "cogs.moderation",
    "cogs.owner"
]

bot.uptime = datetime.utcnow()
bot.giveaways = []

if __name__ == "__main__":
    for i, cog in enumerate(cogs, start=1):
        try:
            bot.load_extension(cog)
            print(f"{i}/{len(cogs)}: {cog.split('.')[1].title()}.py successfully loaded!")
        except Exception as e:
            print(e)
            traceback.print_exc()


try:
    t = os.getenv("TOKEN")
    bot.run(t)
except Exception as e:
    print(e)
finally:
    for g in bot.giveaways:
        add_giveaway(*g)
    traceback.print_exc()
