# Sends text results
from PositionRanges import PositionRange
class Results:

    def GTO(cards,position):
        gtoOutput =f''' PositionRange.{position}Open'''
        gt = f'{gtoOutput}'
        print(gt)
        if cards in f'''PositionRange.{position}Open''':
            GTOplay = 'Open'
            return GTOplay
        else:
            GTOplay = 'Fold'
            return GTOplay

    async def run(ctx,cards,position,stack):

            await ctx.send(f'''Position: **{str.upper(position)}**   \nStack: **{stack}**  \nGTO: **{Results.GTO(cards,position)}**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')

