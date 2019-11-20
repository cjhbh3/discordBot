import discord

client = discord.Client()

@client.event
async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')

# Bot token: 'NjQ2NDgzNjM2Njk0MTU1Mjc1.XdRy3w.chmFA1d9ueEAQwDCcFkkcCtXdVU'
client.run('NjQ2NDgzNjM2Njk0MTU1Mjc1.XdRy3w.chmFA1d9ueEAQwDCcFkkcCtXdVU')