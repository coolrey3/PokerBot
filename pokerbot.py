import discord
from poker import *
from discord.ext import commands
# from HoleCardImage import CardImages
import os.path
from PIL import Image



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


@bot.command(aliases=("pokerbot",'pb'))
async def poker_bot(ctx):
    embed = discord.Embed(title="PokerBot Help", description='''Hi i'm pokerbot! I am in early alpha so what I am able to do is limited at this time.\n\nRefer to the list below for my available commands and keep in mind commands are case insensitive for your convenience! \n''')
    embed.add_field(name="!PokerBot", value="Displays the Poker Bot instructions")
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
    cardsFormatted = str.upper(cards[:2])+cards[2:]
    position = 'SB'

    class CardImages:

         async def cardimage(self):

            print(cards + ' in class')
            if len(cards) > 3:
                card1 = cards[:2]
                card2 = cards[2:4]

                # checks to see if hole cards already exist in folder
                fp = './HoleCards/'
                if os.path.isfile(f'''{fp}{cards}.png'''):
                    print('Hole Cards already exist')
                else:
                    images = [Image.open(x) for x in [f'''./4colordeck/{card1}.png''', f'''./4colordeck/{card2}.png''']]
                    widths, heights = zip(*(i.size for i in images))

                    total_width = sum(widths)
                    max_height = max(heights)

                    new_im = Image.new('RGB', (total_width, max_height))

                    x_offset = 0

                    for im in images:
                        new_im.paste(im, (x_offset, 0))
                        x_offset += im.size[0]

                    new_im.save(f'''./HoleCards/{cards}.png''')
                    print('new image saved in holecards')

                # sends images of cards
                file = discord.File(f'''./HoleCards/{cards}.png''', filename=f'''./HoleCards/{cards}.png''')
                await ctx.send(file=file)

                ############################

    await CardImages.cardimage(cards)

    # sends text results
    if cards in sbOpen:
        if len(cards) > 3:
            await ctx.send(f'''Position: **{position}**   \nStack: **{stack}**  \nGTO: **__Open__**''')
        else:
            await ctx.send(f'''Hand: ** {cardsFormatted} **  \nPosition: **{position}**  \nStack: **{stack}**  \nGTO: **__Open__**''')
    else:
        if len(cards) > 3:
            await ctx.send(f'''\nPosition: **{position}**  \nStack: **{stack}**  \nGTO: **__Fold__**''')
        else:
            await ctx.send(f'''Hand: ** {cardsFormatted} **  \nPosition: **{position}**  \nStack: **{stack}**  \nGTO: **__Fold__**''')

@bot.command()
async def utg(ctx, arg, stack="100bb"):
    print(arg)
    if arg in utgOpen:
        await ctx.send(arg + ' Under the Gun, GTO says open')
    else:
        await ctx.send(arg + " Under the Gun, GTO says Fold it")


@bot.command()
async def mp(ctx, arg, stack="100bb"):
    print(arg)
    if arg in mpOpen:
        await ctx.send(arg + ' in MP, GTO says open')
    else:
        await ctx.send(arg + " in MP, GTO says Fold it")


@bot.command()
async def co(ctx, arg, stack="100bb"):
    print(arg)
    if arg in coOpen:
        await ctx.send(arg + ' in the CO, GTO says open')
    else:
        await ctx.send(arg + " in the CO, GTO says Fold it")

@bot.command()
async def combo(ctx,arg):
    print(arg)
    ctx.send(arg)
@bot.command()
async def btn(ctx, arg, stack="100bb"):
    print(arg)
    if arg in buttonOpen:
        await ctx.send(arg + ' on the Button, GTO says open')

    else:
        await ctx.send(arg + " on the Button, GTO says Fold it")


@bot.command()
async def range(ctx, cards):
    print(cards)
    await ctx.send(Range(cards).to_ascii())


bot.run(token)
