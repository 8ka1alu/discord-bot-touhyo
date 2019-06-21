from discord.ext import commands
import os
import traceback

bot = commands.Bot(command_prefix='/')
token = os.environ['DISCORD_BOT_TOKEN']


@bot.event
async def on_command_error(ctx, error):
    await ctx.send(str(error))


@bot.command()
async def ping(ctx):
    await ctx.send('pong')
    
@bot.command(name="こんにちは")
async def hello(ctx):
    await ctx.send(f"どうも、{ctx.message.author.name}さん！")


@bot.command(name="さようなら")
async def goodbye(ctx):
    await ctx.send(f"じゃあね、{ctx.message.author.name}さん！")


bot.run(token)