import discord

async def mute(ctx, member: discord.Member, duration=None):
    role = discord.utils.get(ctx.guild.roles, name='Muted')
    if not role:
        role = await ctx.guild.create_role(name='Muted')
        for channel in ctx.guild.channels:
            await channel.set_permissions(role, send_messages=False)
    await member.add_roles(role)
    await ctx.send(f'{member.mention} has been muted for {duration}.')