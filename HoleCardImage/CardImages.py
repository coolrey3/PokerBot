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
            formattedcards = str.upper(cards[:1])+cards[1:2]+str.upper(cards[2:3])+cards[3:]
            print(formattedcards)

            # checks to see if hole cards already exist in folder
            if os.path.isfile(f'''{fp}{formattedcards}.png'''):
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


