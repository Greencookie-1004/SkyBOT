import discord
import asyncio
import bs4
import youtube_dl
import beautifulsoup4

client = discord.Client()
 
@client.event
async def on_message(message):
    if message.content.startswith("//들어와"):
        channel = message.author.voice.voice_channel
        server = message.server
        voice_client = client.voice_client_in(server)
        print("들어와")
        print(voice_client)
        print("들어와")
        if voice_client== None:
            await message.channel.send('들어왔습니다') 
            await client.join_voice_channel(channel)
        else:
            await message.channel.send('봇이 이미 들어와있습니다.') 

client.run('NzM2MTM1NjcyODQyNDIwMzI2.XxqZxQ.qxhev3KcOcRWwQvqZNs1n2mzkTI')
