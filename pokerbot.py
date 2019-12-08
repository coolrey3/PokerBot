import discord
from poker import *
from discord.ext import commands

description = '''An example bot to showcase the discord.ext.commands extension
module. There are a number of utility commands being showcased here.'''

bot = commands.Bot(command_prefix='!', case_insensitive=True, description=description, pass_context=True)


# Discord
def read_token():
    with open("token.txt", "r") as f:
        lines = f.readlines()
        return lines[0].strip()


token = read_token()
client = discord.Client()
guildId = client.get_guild(635691275663704091)

# GTO Opening Ranges
utgOpen = Range('AA-33 AKo-AJo KQo AKs-ATs KQs-KTs QJs-QTs JTs-J9s T9s 98s 87s 76s 65s')
mpOpen = Range('AA-22 AKs-A7s A5s KQs-KTs QJs-QTs JTs-J9s T9s-T8s 98s-97s 87s-86s 76s-75s 65s 54s AKo-ATo KQo')
coOpen = Range('AA-22 AKs-A2s KQs-K6s QJs-Q7s JTs-J8s T9s-T8s 98s-97s 87s-86s 76s-75s 65s-64s 54s AKo-ATo KQo-KJo QJo')
buttonOpen = Range(
    'AA-22 AKs-A2s KQs-K2s QJs-Q2s JTs-J5s T9s-T6s 98s-96s 87s-85s 76s-74s 65s-64s 54s-53s 43s AKo-A2o KQo-K7o QJo-Q9o JTo-J9o T9o-T8o 98o 87o')
sbOpen = Range(
    'AA-22 AKs-A2s KQs-K2s QJs-Q4s JTs-J7s T9s-T7s 98s-97s 87s-86s 76s-75s 65s-64s 54s AKo-A7o KQo-K9o QJo-Q9o JTo-J9o T9o 98o')


@bot.event
async def on_ready():
    print(f'''Logged in as {bot.user.name}''')
    print(bot.user.id)
    print('------')


@bot.command()
async def users(ctx):
    await ctx.send(f"""# of users on this server: {guildId.member_count}""")


@bot.command()
async def pb(ctx):
    await ctx.send("Hi i'm pokerbot! I am in early beta so what I am able to do is limited at this time. Refer"
                   " to the list below for my available commands. \n\n"
                   "'!open range' : lists NLHE opening ranges \n"
                   "'!equity' : type command followed by hole cards to return equity;(i.e: !equity A9o) \n")


@bot.command()
async def openrange(ctx):
    await ctx.send("https://cdn.discordapp.com/attachments/635691657219538945/652081217679917088/opening_ranges.jpg")


@bot.command()
async def sb(ctx, arg):
    print(arg)
    if arg in sbOpen:
        await ctx.send(arg + ' in the SB, GTO says open')
    else:
        await ctx.send(arg + " in the SB, GTO says Fold it")


@bot.command()
async def utg(ctx, arg):
    print(arg)
    if arg in utgOpen:
        await ctx.send(arg + ' Under the Gun, GTO says open')
    else:
        await ctx.send(arg + " Under the Gun, GTO says Fold it")


@bot.command()
async def mp(ctx, arg):
    print(arg)
    if arg in mpOpen:
        await ctx.send(arg + ' in MP, GTO says open')
    else:
        await ctx.send(arg + " in MP, GTO says Fold it")


@bot.command()
async def co(ctx, arg):
    print(arg)
    if arg in coOpen:
        await ctx.send(arg + ' in the CO, GTO says open')
    else:
        await ctx.send(arg + " in the CO, GTO says Fold it")


@bot.command()
async def btn(ctx, arg):
    print(arg)
    if arg in buttonOpen:
        await ctx.send(arg + ' on the Button, GTO says open')

    else:
        await ctx.send(arg + " on the Button, GTO says Fold it")


bot.run(token)
