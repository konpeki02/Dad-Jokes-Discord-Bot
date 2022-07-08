import json
import discord
import sys
from discord.ext import commands



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


key = getKey('key.json', 'key')

bot = commands.Bot(command_prefix='!')


@bot.event
async def on_ready():
    print('We have logged in as {0.user}'.format(bot))


@bot.event
async def on_message(message):
    if message.author == bot.user:
        return
    words = ['Im', 'I\'m', 'im']
    for word in words:
        if message.content.startswith(word):
            reply = nextWord(word, message.content)
            await message.channel.send('Hello %s, I\'m Dad!' % reply)
    if message.content.startswith('!exit'):
        exit()


bot.run(key)

