import discord

client = discord.Client()
test_ch = client.get_channel(#Channel ID)

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))
    if (test_ch != None):
        await test_ch.send("Bot started!")

@client.event
async def on_message(message):
    if message.author.bot:
        return
    elif message.content.startswith('Hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('Yikes'):
        await message.channel.send('Big yikes!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )

@client.event
async def on_member_remove(member):
    await test_ch.send(f'Goodbye {member.name}, you will be missed.')


client.run(#Bot token)
