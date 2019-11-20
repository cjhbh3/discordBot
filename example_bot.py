import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.author == client.user:
        return 
    elif message.content.startswith('hello') or message.content.startswith('Hello'):
        return message.channel.send('Hello!')
    elif message.content.startswith('Yikes'):
        return message.channel.send('Big yikes!')

@client.event
async def on_member_join(member):
    await member.create_dm()
    await member.dm_channel.send(
        f'Hi {member.name}, welcome to my Discord server!'
    )


# Bot token: 'NjQ2NDgzNjM2Njk0MTU1Mjc1.XdSMhg.yNw872CawvNs6vr5IblYAFIxhCI'
client.run('NjQ2NDgzNjM2Njk0MTU1Mjc1.XdSMhg.yNw872CawvNs6vr5IblYAFIxhCI')