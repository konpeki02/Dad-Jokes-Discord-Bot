import json
import sys
import discord
from discord.ext import commands
from datetime import datetime

bot = commands.Bot(command_prefix='!')





def getKey(filename, target):
    with open(filename) as f:
        data = json.load(f)
        token = data[target]
        return token


def nextWord(target, source):
    msg = source.split()
    for i, h in enumerate(msg):
        if h == target:
            return msg[i + 1]


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    await bot.process_commands(message)
    if message.author == bot.user:
        return
    words = ['Im', 'I\'m', 'im']
    for word in words:
        if message.content.startswith(word):
            reply = nextWord(word, message.content)
            await message.channel.send('Hello %s, I\'m Dad!' % reply)
    if message.content.startswith('!exit'):
        await message.channel.send('Sayonara...\n')
        sys.exit()


@bot.command(pass_context=True)
async def quote(ctx, arg, name):
    current_time = datetime.now()
    timestamp = 'Timestamp: %s' % current_time.strftime("%b-%d-%Y %H:%M:%S")
    user_quote = '\" %s \" - %s' % (arg, name)
    embed = discord.Embed(title=user_quote, description=timestamp, color=0x00ff00)

    await ctx.channel.send(embed=embed)


bot.run(getKey('key.json', 'key'))
