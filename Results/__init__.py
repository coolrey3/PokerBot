# Sends text results
class Results:
    async def run(ctx,cards,position,stack):
        if cards in f'''PositionRange.{position}Open''':

            if len(cards) > 3:
                await ctx.send(
                    f'''Position: **{str.upper(position)}**   \nStack: **{stack}**  \nGTO: **__Open__**''')
            else:
                await ctx.send(f'''Position: **{position}**  \nStack: **{stack}**  \nGTO: **__Open__**''')
        else:
            if len(cards) > 3:
                await ctx.send(
                    f'''\nPosition: **{str.upper(position)}**  \nStack: **{stack}**  \nGTO: **__Fold__**''')
            else:
                await ctx.send(
                    f'''Position: **{position}**  \nStack: **{stack}**  \nGTO: **__Fold__** ''')

        #     if len(cards) > 3:
        #         await ctx.send(f'''Position: **{str.upper(position)}**   \nStack: **{stack}**  \nGTO: **__Open__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')
        #     else: **__Open__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')
        # else:
        #     if len(cards) > 3:
        #         await ctx.send(f'''\nPosition: **{str.upper(position)}**  \nStack: **{stack}**  \nGTO: **__Fold__**\n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')
        #     else:
        #         await ctx.send(f'''Position: **{position}**  \nStack: **{stack}**  \nGTO: **__Fold__** \n\n **__Raise First-In__**\n\n **__Call VS__**\n\n **__3-Bet VS__**\n\n **__Squeeze VS__**''')

