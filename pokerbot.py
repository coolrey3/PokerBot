import discord
from poker import *


#Discord
def read_token():
    with open("token.txt", "r") as f:
        lines=f.readlines()
        return lines[0].strip()

token = read_token()
client=discord.Client()

#Open Ranges
utgOpen = Range('AA-33 AKo-AJo KQo AKs-ATs KQs-KTs QJs-QTs JTs-J9s T9s 98s 87s 76s 65s')
mpOpen = Range('AA-22 AKs-A7s A5s KQs-KTs QJs-QTs JTs-J9s T9s-T8s 98s-97s 87s-86s 76s-75s 65s 54s AKo-ATo KQo')
coOpen = Range('AA-22 AKs-A2s KQs-K6s QJs-Q7s JTs-J8s T9s-T8s 98s-97s 87s-86s 76s-75s 65s-64s 54s AKo-ATo KQo-KJo QJo')
buttonOpen = Range('AA-22 AKs-A2s KQs-K2s QJs-Q2s JTs-J5s T9s-T6s 98s-96s 87s-85s 76s-74s 65s-64s 54s-53s 43s AKo-A2o KQo-K7o QJo-Q9o JTo-J9o T9o-T8o 98o 87o')
sbOpen = Range('AA-22 AKs-A2s KQs-K2s QJs-Q4s JTs-J7s T9s-T7s 98s-97s 87s-86s 76s-75s 65s-64s 54s AKo-A7o KQo-K9o QJo-Q9o JTo-J9o T9o 98o')

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
        await message.channel.send("Hi i'm pokerbot! I am in early beta so what I am able to do is limited at this time. Refer"
                                   " to the list below for my available commands. \n\n"
                                   "'!open range' : lists NLHE opening ranges \n"
                                   "'!equity' : type command followed by hole cards to return equity;(i.e: !equity A9o) \n")

    if message.content.find("!open range") !=-1:
        await message.channel.send("https://cdn.discordapp.com/attachments/635691657219538945/652081217679917088/opening_ranges.jpg",)


    #if message.content.find("!equity") !=-1:
    #
    #     holecards = message.content[8:]
    #     print(holecards)
    #     print(cards[0])

    #best method using ranges and poker library
        if Hand("33") in Range('AA-22'):
            print('its here')
        else:
            print("not here")


    #1 method of finding cards via count
        if cards.count(holecards) > 0:
            print("found em")
        else:
            print(type(cards))
            print(type(holecards))
            print(type(cards[0]))

    #checks cards in array, will likely use holes variable and search respective array per position
        if holecards in cards:
            await message.channel.send(holecards + ' , All in Boss')
        else:
            await message.channel.send(holecards + " ,Fold it")

#UTG Open Check
    if message.content.find("!UTG") !=-1:
        holecards = message.content[5:]
        print(holecards)
        if holecards in utgOpen:
            await message.channel.send(holecards + ' UTG, GTO says open')
        else:
            await message.channel.send(holecards + " UTG,Fold it")

#MP Open Check
    if message.content.find("!MP") !=-1:
        holecards = message.content[4:]
        print(holecards)
        if holecards in mpOpen:
            await message.channel.send(holecards + ' MP, GTO says open')
        else:
            await message.channel.send(holecards + " MP,Fold it")

#CO Open Check
    if message.content.find("!CO") !=-1:
        holecards = message.content[4:]
        print(holecards)
        if holecards in coOpen:
            await message.channel.send(holecards + ' CO, GTO says open')
        else:
            await message.channel.send(holecards + " CO,Fold it")

#SB Open Check
    if message.content.find("!SB") !=-1:
        holecards = message.content[4:]
        print(holecards)
        if holecards in sbOpen:
            await message.channel.send(holecards + ' SB, GTO says open')
        else:
            await message.channel.send(holecards + " SB,Fold it")

#Button Open Check
    if message.content.find("!Button") !=-1:
        holecards = message.content[8:]
        print(holecards)
        if holecards in buttonOpen:
            await message.channel.send(holecards + ' Button, GTO says open')
        else:
            await message.channel.send(holecards + " Button,Fold it")






client.run(token)


