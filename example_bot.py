import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('hello') or message.content.startswith('Hello'):
        await message.channel.send('Hello!')
    elif message.content.startswith('Yikes'):
        await message.channel.send('Big yikes!')

# Bot token: 'NjQ2NDgzNjM2Njk0MTU1Mjc1.XdSEjw.PYhHRZ6nfgDgwa2t9IF388qw_jI'
client.run('NjQ2NDgzNjM2Njk0MTU1Mjc1.XdSEjw.PYhHRZ6nfgDgwa2t9IF388qw_jI')