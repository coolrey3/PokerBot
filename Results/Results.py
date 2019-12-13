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

        ri = getattr(PositionRange, f'''{position}RaiseIn''')
        raiseIn = ri

        if cards in raiseIn:
            return 'Card in Raise in'
        else:
            return 'not in list'


    async def run(ctx,cards,position,stack):

            await ctx.send(f'''Position: **{str.upper(position)}**   \nStack: **{stack}**  \nGTO: **__{Results.GTO(cards,position)}__**\n\n **__Raise First-In__**\n{Results.RaiseFirst(cards,position)}\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')

