import discord, random
from discord.ext import commands
import filemanagement

client = commands.Bot(command_prefix = '.')

@client.event
async def on_ready():
    print("Bot is ready!")

@client.command()
async def ping(ctx):
    await ctx.send('Pong!')

@client.command(aliases=['8ball', 'test'])
async def _8ball(ctx, *, question):
    response = ['Jaa',
                'Nein',
                'Vielleicht']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')

@client.command()
async def file(ctx):
    await ctx.send(f'{filemanagement.readFile()}')

client.run('NjQyODc3MzQ2OTQ0Mzg1MDM2.XcdUbQ.6YDddivbSOwEaRIhRqQHFGzfL6Q')