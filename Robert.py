#導入Discord.py
import os
import discord
from discord import message
from discord import channel
from discord.ext import commands
from discord.flags import Intents
from dotenv import load_dotenv

load_dotenv()

token = os.getenv('TOKEN')
channelID = os.getenv('CHANNEL_ID')


intents = discord.Intents.default()
intents.members = True
bot =commands.Bot(command_prefix='!',intents = intents)


@bot.event
async def on_ready():
  print('>>Bot Online:',bot.user,'<<')
  await bot.change_presence(activity=discord.Streaming(name="LIFE 2.O", url='https://www.youtube.com/watch?v=dQw4w9WgXcQ'))


@bot.command()
async def ping(ctx):
  await ctx.send(f'{round(bot.latency*1000)}(ms)')

@bot.event
async def on_typing(channel, user, when):
  #channel = bot.get_channel(channelID)
  await channel.send(f'{user} FQ!')

@bot.event
async def on_member_join(member):
  channel = bot.get_channel(channelID)
  await channel.send(f'{member} join!')

@bot.event
async def on_member_remove(member):
  channel = bot.get_channel(channelID)
  await channel.send(f'{member} leave!')



bot.run(token)



'''
@bot.event
async def on_message(message):
    #排除自己的訊息，避免陷入無限循環
    if message.author == bot.user:
      return
    #如果以「說」開頭
    if message.content.startswith('say'):
      #分割訊息成兩份
      tmp = message.content.split(" ",2)
      #如果分割後串列長度只有1
      if len(tmp) == 1:
        await message.channel.send( message.author.name +"你要我說什麼啦？")
      else:
        await message.channel.send(message.author.name +' '+ tmp[1] )
        
'''
 




'''
# Setting `Playing ` status
await bot.change_presence(activity=discord.Game(name="a game"))

# Setting `Streaming ` status
await bot.change_presence(activity=discord.Streaming(name="My Stream", url=my_twitch_url))

# Setting `Listening ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.listening, name="a song"))

# Setting `Watching ` status
await bot.change_presence(activity=discord.Activity(type=discord.ActivityType.watching, name="a movie"))
'''


