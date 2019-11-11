import discord, random
from discord.ext import commands
import filemanagement, usermanagement


client = commands.Bot(command_prefix = '.')


@client.event
async def on_ready():
    print("Bot is ready!")


@client.command()
async def ping(ctx):
    await ctx.send('Pong!')


@client.command(aliases=['8ball'])
async def _8ball(ctx, *, question):
    response = ['Jaa',
                'Nein',
                'Vielleicht']

    await ctx.send(f'Question: {question}\nAnswer: {random.choice(response)}')


@client.command()
async def newuser(ctx):
    if usermanagement.addNewUser(ctx.message.author.name):
        await ctx.send(f'Dein Account wurde erstellt, ' + ctx.message.author.name)
    elif usermanagement.addNewUser(ctx.message.author.name) == False:
        await ctx.send(f'Du hast bereits einen Account!')
    else:
        await ctx.send(f'Discord ist gay')

@client.command()
async def username(ctx):
    await ctx.send(ctx.message.author.name)


@client.command()
async def levelup(ctx):
    usermanagement.levelUp(ctx.message.author.name)
    await ctx.send(f'Level Up!')

@client.command()
async def test(ctx):
    await ctx.send(filemanagement.readFile())

@client.command()
async def file(ctx):
    for i in range(len(filemanagement.readFile())):
        if filemanagement.readFile()[i][0] == ctx.message.author.name:
            output = filemanagement.readFile()[i][1]
    await ctx.send(f'Du bist Level: {output}')



client.run('NjQyODc3MzQ2OTQ0Mzg1MDM2.XciKiw.BMyMDCCQGNaSi6FGoB_dEEvUf-M')
