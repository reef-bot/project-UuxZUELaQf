import discord

async def warn(ctx, member: discord.Member, reason=None):
    # Custom logic for warning a member
    await ctx.send(f'{member.mention} has been warned for: {reason}')