import asyncio
import discord
from discord.channel import VoiceChannel
from discord.utils import get
import time
import datetime
from discord.ext import commands


client = commands.Bot(command_prefix="!")

@client.command
async def play(ctx, url : str):
    voiceChannel = discord.utils.get(ctx.guild.voice_channels, name="General")
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if not voice,is_connected():
        await voiceChannel.connect()

@client.command
async def leave(ctx):
    voice=discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_connected():
        await voice.disconnect()
    else:
        await ctx.send("Der Bot ist mit keinem Channel verbunden")

@client.command
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients, guild=ctx.guild)
    if voice.is_playing():
        voice.pause()
    else:
        await ctx.send("Es spielt keine Musik")


    
client = client()
client.run('ODU1NTM3NTk1MjIwMjMwMTk0.YMz7eQ.R-Wm2oUmNM5Xe04JHf241cv7HB8')
