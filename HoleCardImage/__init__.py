import os.path
from PIL import Image
import discord
from poker import *
from discord.ext import commands

fp = './HoleCards/'


class CardImages:

    def Formatted(cards):
        cardsFormatted = str.upper(cards[:2]) + str.lower(cards[2:])
        return cardsFormatted

    async def cardImage(cards):

        print(cards + ' in class')

        if len(cards) > 3:
            card1 = cards[:2]
            card2 = cards[2:4]

            # checks to see if hole cards already exist in folder
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
    async def sendImage(ctx,cards):
        # Send Images
        if len(cards) > 3:
            await CardImages.cardImage(cards)
            file = discord.File(f'''./HoleCards/{cards}.png''', filename=f'''./HoleCards/{cards}.png''')
            await ctx.send(file=file)
        else:
            await ctx.send(f'''Hand: ** {CardImages.Formatted(cards)}**\n''')


# Sends text results
class Results:
    async def run(ctx,cards,position,stack):
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


