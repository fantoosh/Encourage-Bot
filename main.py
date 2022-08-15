import discord
import os
import requests
import json

from discord.ext import commands, tasks


TOKEN = os.environ['DISCORD_TOKEN']

client = commands.Bot(command_prefix="$")

def get_quote():
  response = requests.get("https://zenquotes.io/api/random")

  data = json.loads(response.text)
  quote = data[0]['q'] + " -" + data[0]['a']
  return quote

@tasks.loop(minutes=10.0)
async def non_stop(channel):
  quote = get_quote()
  await channel.send(quote)

@client.event
async def on_ready():
  print('we have logged in as {0.user}'.format(client))
  channel = client.get_channel(951434880678502432)
  non_stop.start(channel)

@client.event
async def on_message(ctx):
  if ctx.author == client.user:
    return

  if ctx.content.startswith('$inspire'):
    quote = get_quote()
    await ctx.channel.send(quote)


client.run(TOKEN)