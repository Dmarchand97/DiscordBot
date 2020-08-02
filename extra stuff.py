client = commands.Bot(command_prefix = '.')
status = cycle(['Coolin', 'Boolin'])


@client.event
async def on_ready():
    change_status.start()
    print('Bot is ready. . .')


# @client.event
# async def on_member_join(member):
#     print(f'{member} had joined a server. . .')
#
#
# @client.event
# async def on_member_remove(member):
#     print(f'{member} had left a server. . .')




# @client.event
# async def on_command_error(ctx, error):
#     if isinstance(error, commands.CommandNotFound):
#         await ctx.send('Invalid command used. . .')



# @client.command(aliases=['ping'])
# async def Ping(ctx):
#     await ctx.send(f'{round(client.latency * 1000)} ms. . .')


# @client.command()
# @commands.has_permissions(manage_messages=True)
# async def clear(ctx, amount=10):
#     await ctx.channel.purge(limit=amount)


# def is_it_me(ctx):
#     return ctx.author.id == 205742475027939328

# @client.command()
# @commands.check(is_it_me)
# async def example(ctx):
#     await ctx.send(f'Hi im {ctx.author}')


# @clear.error
# async def clear_error(ctx, error):
#     if isinstance(error, commands.MissingRequiredArgument):
#         await ctx.send('Please specify an amount of messages to delete.')


# @client.command()
# async def kick(ctx, member:discord.Member, *, reason=None):
#     await member.kick(reason=reason)


# @client.command()
# async def ban(ctx, member:discord.Member, *, reason=None):
#     await member.ban(reason=reason)
#     await ctx.send(f'Banned {member.name}#{member.mention}')
#
#
# @client.command()
# async def unban(ctx, *, member):
#     banned_users =  await ctx.guild.bans()
#     member_name, member_discriminator = member.split('#')
#     for ban_entry in banned_users:
#         user = ban_entry.user
#         if (user.name, user.discriminator) == (member_name, member_discriminator):
#             await ctx.guild.unban(user)
#             await ctx.send(f'Unbanned {user.mention}')
#             return
#

# @tasks.loop(seconds=10)
# async def change_status():
#     await client.change_presence(activity=discord.Game(next(status)))




# @client.command()
# async def load(ctx, extension):
#     client.load_extension(f'cogs.{extension}')
#
# @client.command()
# async def unload(ctx, extension):
#     client.unload_extension(f'cogs.{extension}')


# @client.command(aliases=['8ball', 'test'])
# async def _8ball(ctx, *, question):
#     responses = ["It is certain.",
#     "It is decidedly so.",
#     "Without a doubt.",
#     "Yes - definitely.",
#     "You may rely on it.",
#     "As I see it, yes.",
#     "Most likely.",
#     "Outlook good.",
#     "Yes.",
#     "Signs point to yes.",
#     "Reply hazy, try again.",
#     "Ask again later.",
#     "Better not tell you now.",
#     "Cannot predict now.",
#     "Concentrate and ask again.",
#     "Don't count on it.",
#     "My reply is no.",
#     "My sources say no.",
#     "Outlook not so good.",
#     "Very doubtful."]
#     await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
