import discord



def read_token():
    with open("token.txt", "r") as f:
        lines=f.readlines()
        return lines[0].strip()

token = read_token()

client=discord.Client()

utgOpen = []
cards = ['A9o','AA',]

@client.event
async def on_message(message):

    guildId=client.get_guild(635691275663704091)

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return
    if message.author.bot: return

    # Bot Commands

    if message.content.find("!users") !=-1:
        await message.channel.send(f"""# of users on this server: {guildId.member_count}""")
    if message.content.find("!pb") !=-1 or message.content.find("!pokerbot") !=-1:
        #await message.channel.send("Hi i'm pokerbot! type '!pokerbot commands' to see what I can do!")
    #if message.content.find("!pokerbot commands") !=-1 or message.content.find("!pb commands") !=-1:
        await message.channel.send("Hi i'm pokerbot! I am in early beta so what I am able to do is limited at this time. Refer"
                                   " to the list below for my available commands. \n\n"
                                   "'!open range' : lists NLHE opening ranges \n"
                                   "'!equity' : type command followed by hole cards to return equity;(i.e: !equity A9o) \n")

    if message.content.find("!open range") !=-1:
        await message.channel.send("https://cdn.discordapp.com/attachments/635691657219538945/652081217679917088/opening_ranges.jpg",)


    if message.content.find("!equity") !=-1:
        #print(message.content[7:11])
        #await message.channel.send("test")

        holecards = message.content[8:]
        print(holecards)
        print(cards[0])
        if cards.count(holecards) > 0:
            print("found em")
        else:
            print(type(cards))
            print(type(holecards))
            print(type(cards[0]))

        if holecards in cards:
            await message.channel.send(holecards + ' , All in Boss')
        else:
            await message.channel.send(holecards + " ,Fold it")



client.run(token)


