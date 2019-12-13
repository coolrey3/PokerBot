# Sends text results
from PositionRanges import PositionRange
class Results:

    def GTO(cards,position):
        gt = getattr(PositionRange, f'''{position}Open''')
        gtoOutput = gt

        # print(gtoOutput)
        if cards in gtoOutput:
            GTOplay = 'Open'
            return GTOplay
        else:
            GTOplay = 'Fold'
            return GTOplay

    def RaiseFirst(cards,position):

        if cards in

        print('first')


    async def run(ctx,cards,position,stack):

            await ctx.send(f'''Position: **{str.upper(position)}**   \nStack: **{stack}**  \nGTO: **__{Results.GTO(cards,position)}__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')

