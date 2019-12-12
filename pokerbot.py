import discord
from poker import *
from discord.ext import commands
from HoleCardImage import CardImages
from PositionRanges import *

cards = ''
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


@bot.event
async def on_ready():
    print(f'''Logged in as {bot.user.name}''')
    print(bot.user.id)
    print('------')


@bot.command()
async def users(ctx):
    await ctx.send(f"""# of users on this server: {guildId.member_count}""")


@bot.command(aliases=("pokerbot", 'pb'))
async def poker_bot(ctx):
    embed = discord.Embed(title="PokerBot Help", description='''Hi i'm pokerbot! I am in early alpha so what I am able to do is limited at this time.\n\nRefer to the list below for my available commands and keep in mind commands are case insensitive for your convenience! \n''')
    embed.add_field(name="!PokerBot", value="Displays the Poker Bot instructions")
    embed.add_field(name="!Range", value="type comman followed by range to see range chart;(i.e: !Range 33+,A5s+")
    embed.add_field(name="!OpenRange", value="Sends image of GTO recommended open range for 6 max NLHE")
    embed.add_field(name="!BTN", value="type command followed by hole cards for an open or fold recommendation from the Button;(i.e: !BTN A9o)")
    embed.add_field(name="!SB", value="type command followed by hole cards for an open or fold recommendation from the Small Blind;(i.e: !SB JJ)")
    embed.add_field(name="!CO", value="type command followed by hole cards for an open or fold recommendation from the Cut Off;(i.e: !CO 8h6d)")
    embed.add_field(name="!MP", value="type command followed by hole cards for an open or fold recommendation from Middle Position;(i.e: !MP T9s)")
    embed.add_field(name="!UTG", value="type command followed by hole cards for an open or fold recommendation from Under the Gun;(i.e: !UTG AA)")
    await ctx.send(content=None, embed=embed)


@bot.command()
async def openrange(ctx):
    file = discord.File('openrange.jpg', filename='openrange.jpg')
    await ctx.send(file=file)


@bot.command()
async def sb(ctx, cards, stack="100bb"):
    position = 'sb'

# Send Images
    if len(cards) > 3:
        await CardImages.cardImage(cards)
        await ctx.send(file=CardImages.sendImage(cards))
    else:
        await ctx.send(f'''Hand: ** {CardImages.Formatted(cards)}**\n''')

# Sends text results
    if cards in f'''PositionRange.{position}Open''':
        if len(cards) > 3:
            await ctx.send(f'''Position: **{str.upper(position)}**   \nStack: **{stack}**  \nGTO: **__Open__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')
        else:
            await ctx.send(f'''Position: **{position}**  \nStack: **{stack}**  \nGTO: **__Open__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')
    else:
        if len(cards) > 3:
            await ctx.send(f'''\nPosition: **{str.upper(position)}**  \nStack: **{stack}**  \nGTO: **__Fold__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')
        else:
            await ctx.send(f'''Position: **{position}**  \nStack: **{stack}**  \nGTO: **__Fold__** \n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')


@bot.command()
async def utg(ctx, cards, stack="100bb"):

    cardsFormatted = str.upper(cards[:2]) + cards[2:]
    position = 'utg'

    # Send Images
    if len(cards) > 3:
        await CardImages.cardImage(cards)
        await ctx.send(file=CardImages.sendImage(cards))
    else:
        await ctx.send(f'''Hand: ** {cardsFormatted}**\n''')

    if cards in f'''PositionRange.{position}Open''':
        await ctx.send(cards + ' Under the Gun, GTO says open')
    else:
        await ctx.send(cardsFormatted + " Under the Gun, GTO says Fold it")


@bot.command()
async def mp(ctx, cards, stack="100bb"):
    print(cards)
    cardsFormatted = str.upper(cards[:2]) + cards[2:]

    # Send Images
    if len(cards) > 3:
        await CardImages.cardImage(cards)
        await ctx.send(file=CardImages.sendImage(cards))
    else:
        await ctx.send(f'''Hand: ** {cardsFormatted}**\n''')


    if cards in PositionRange.mpOpen:
        await ctx.send(cards + ' in MP, GTO says open')
    else:
        await ctx.send(cards + " in MP, GTO says Fold it")


@bot.command()
async def co(ctx, cards, stack="100bb"):
    print(cards)
    cardsFormatted = str.upper(cards[:2]) + cards[2:]

    # Send Images
    if len(cards) > 3:
        await CardImages.cardImage(cards)
        await ctx.send(file=CardImages.sendImage(cards))
    else:
        await ctx.send(f'''Hand: ** {cardsFormatted}**\n''')

    if cards in PositionRange.coOpen:
        await ctx.send(cards + ' in the CO, GTO says open')
    else:
        await ctx.send(cards + " in the CO, GTO says Fold it")

@bot.command()
async def combo(ctx,arg):
    print(arg)
    ctx.send(arg)
@bot.command()
async def btn(ctx, cards, stack="100bb"):
    print(cards)
    if cards in PositionRange.buttonOpen:
        await ctx.send(cards + ' on the Button, GTO says open')

    else:
        await ctx.send(cards + " on the Button, GTO says Fold it")

        cardsFormatted = str.upper(cards[:2]) + cards[2:]

        # Send Images
        if len(cards) > 3:
            await CardImages.cardImage(cards)
            await ctx.send(file=CardImages.sendImage(cards))
        else:
            await ctx.send(f'''Hand: ** {cardsFormatted}**\n''')


@bot.command()
async def range(ctx, cards):
    print(cards)
    await ctx.send(Range(cards).to_ascii())

@bot.command()
async def setrange(ctx, position, userrange):
    print(position)
    if str.lower(position) == 'sb':
        sbOpen = Range(userrange)
    await ctx.send(Range(userrange).to_ascii())


bot.run(token)
