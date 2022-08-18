import typing
import discord

import emojis
from discord.ext import commands

class ReactionROlesNotSetup(commands.CommandError):
    """Reaction roles are not setup for this guild."""
    pass
def is_setup():
    async def wrap_func(ctx):
        data = await ctx.bot.config.find(ctx.guild.id)
            if data is None:
                raise ReactionsRolesNotSetup

            if data.get("message_id") is None:
             raise ReactionRolesNotSetup

             Return True
        return commands.check(wrap_func)

class Reactions(commands.Cog, nam="ReactionRoles"):
    def __init__(self, bot):
        self.bot = bot

def setup(bot):
    bot.add_cog(Reactions(bot))