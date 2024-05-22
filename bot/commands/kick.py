import discord

async def kick(ctx, member: discord.Member, reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'{member.mention} has been kicked.')