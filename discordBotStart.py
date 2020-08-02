
import discord
import random
import youtube_dl
import os
from discord.ext import commands, tasks
from discord.utils import get
from itertools import cycle

TOKEN = ('NzM2MDYyOTAwMzI1NzExOTcz.XxpV_g.EWeX1rpNdCblY8_8B3IZ5hw_8Ds')
BOTPRE = '.'

client = commands.Bot(command_prefix = '.')
status = cycle(['Listening to music', 'Playing music'])

#showing bot is ready to be used (no errors)
@client.event
async def on_ready():
    #changing the status or the game the bot is "playing"
    change_status.start()
    print('bot is ready. . .')

#checks if i am using the bot
def is_it_me(ctx):
    return ctx.author.id == 205742475027939328

#checks if me
@client.command()
@commands.check(is_it_me)
async def example(ctx):
    await ctx.send(f'Hi im {ctx.author}')


#input error
@client.event
async def on_command_error(ctx, error):
    if isinstance(error, commands.CommandNotFound):
        await ctx.send('Invalid command used. . .')


#checks ping of the bot
@client.command(aliases=['ping'])
async def Ping(ctx):
    await ctx.send(f'Pong! {round(client.latency * 1000)} ms. . .')


#permission to clear messages
@client.command()
@commands.has_permissions(manage_messages=True)
async def clear(ctx, amount=10):
    amount = amount + 1
    #if amount is not stated then the limit is 10
    await ctx.channel.purge(limit=amount)


#someone joined the server for the first time
@client.event
async def on_member_join(member):
    print(f'{member} had joined a server. . .')


#someone leaves the server (kicked, banned, leaves)
@client.event
async def on_member_remove(member):
    print(f'{member} had left a server. . .')


#join voice channel
@client.command(pass_context=True, aliases=['j'])
async def join(ctx):
    global voice
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)

    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
    await voice.disconnect()
    if voice and voice.is_connected():
        await voice.move_to(channel)
    else:
        voice = await channel.connect()
        print(f'The bot has connected {channel}\n ')

    await ctx.send(f'joined {channel}')

#Bot leaving the channel it was called too
@client.command(pass_context=True, aliases=['l'])
async def leave(ctx):
    channel = ctx.message.author.voice.channel
    voice = get(client.voice_clients, guild=ctx.guild)
    if voice and voice.is_connected():
        await voice.disconnect()
        print(f'The bot has left {channel}')
        await ctx.send(f'Left {channel}')
    else:
        print(f'Bot was told to leave. . .\n Wan not in one')
        await ctx.send('Im not in a channel')

#play music from youtube
@client.command(pass_context=True, aliases=['p'])
async def play(ctx, url: str):
    song_there = os.path.isfile('song.mp3')
    try:
        if song_there:
            os.remove('song.mp3')
            print('Removed old song file')
    except PermissionError:
        print('Trying to delete song file but its playing')
        await ctx.send('ERROR. . .music playing')
        return

    await ctx.send('Getting ready. . .')

    voice = get(client.voice_clients, guild=ctx.guild)

    ydl_opts = {
        'format': 'bestaudio/best',
        'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        }],
    }

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        print('Downloading audio. . .\n')
        ydl.download([url])

    for file in os.listdir('./'):
        if file.endswith('.mp3'):
            name = file
            print(f'renamed file: {file}\n')
            os.rename(file, 'song.mp3')
    voice.play(discord.FFmpegPCMAudio('song.mp3'), after=lambda e: print(f'{name} has finished playing!'))
    voice.source = discord.PCMVolumeTransformer(voice.source)
    voice.source.volume = 0.07

    nname = name.rsplit('-', 2)
    await ctx.send(f'Playing {nname[0]}')
    print('Playing. . .')


#changes the status of the bot
@tasks.loop(seconds=10)
async def change_status():
    await client.change_presence(activity=discord.Game(next(status)))

#kick mentioned user
@client.command()
async def kick(ctx, member:discord.Member, *, reason=None):
    await member.kick(reason=reason)

#ban mentioned user
@client.command()
@commands.has_permissions(administrator=True)
async def ban(ctx, member:discord.Member, *, reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'Banned {member.name}#{member.mention}')

#unbanned mentioned user
@client.command()
@commands.has_permissions(administrator=True)
async def unban(ctx, *, member):
    banned_users = await ctx.guild.bans()
    member_name, member_discriminator = member.split('#')
    for ban_entry in banned_users:
        user = ban_entry.user
        if (user.name, user.discriminator) == (member_name, member_discriminator):
            await ctx.guild.unban(user)
            await ctx.send(f'Unbanned {user.mention}')
            return

#enter text to get random responce
@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question, ):
    responses = ["It is certain.",
    "It is decidedly so.",
    "Without a doubt.",
    "Yes - definitely.",
    "You may rely on it.",
    "As I see it, yes.",
    "Most likely.",
    "Outlook good.",
    "Yes.",
    "Signs point to yes.",
    "Reply hazy, try again.",
    "Ask again later.",
    "Better not tell you now.",
    "Cannot predict now.",
    "Concentrate and ask again.",
    "Don't count on it.",
    "My reply is no.",
    "My sources say no.",
    "Outlook not so good.",
    "Very doubtful."]
    await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')


# for filename in os.listdir('./Cogs'):
#     if filename.endswith('.py'):
#         client.load_extension(f'Cogs.{filename[:-3]}')

client.run(TOKEN)