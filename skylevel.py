import discord
import asyncio
import openpyxl

client = discord.Client()

@client.event
async def on_message(message):
    if message.content.startswith(''):
        file = openpyxl.load_workbook('레벨.xlsx')
        sheet = file.active
        exp = [100, 500, 1000, 5000, 10000, 50000, 100000, 500000]
        i = 1
        while True:
            if sheet["A" + str(i)].value == str(message.author.id):
                sheet["B" + str(i)].value = sheet["B" + str(i)].value + 2
                if sheet["B" + str(i)].value >= exp[sheet["C" + str(i)].value - 1]:
                    sheet["C" + str(i)].value = sheet["C" + str(i)].value + 1
                    embed = discord.Embed(title="레벨업!", description="현재 레벨 : " + str(sheet["C" + str(i)].value) + "레벨 \n 현재 경험치 : " + str(sheet["B" + str(i)].value) + "XP")
                    embed.set_footer(text="레벨은 강제로 삭제할 수 없어요!")
                    await message.channel.send(embed=embed)
                file.save('레벨.xlsx')
                break

            if sheet["A" + str(i)].value == None:
                sheet["A" + str(i)].value = str(message.author.id)      
                sheet["B" + str(i)].value = 0
                sheet["C" + str(i)].value = 1
                file.save('레벨.xlsx')
                break
                
            i += 1

client.run('')
