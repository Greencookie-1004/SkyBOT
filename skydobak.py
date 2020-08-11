import discord
import asyncio
import re
import os, random, time

client = discord.Client()

#사용하는 변수들
idA, moneyA, preA, timeA, give, ID, TIME = [], [], [], [], 0, 0, 0


try: #만약 파일이 없으면 새로 만듦
    f = open("UserData.txt", "r")
except:
    f = open("UserData.txt", "w")
    f.close()
    f = open("UserData.txt", "r")
    w = open("member.txt", "r")
while True: #유저들 데이터를 읽음 데이터 형식 : 유저ID,가지고 있는 돈,돈받은 시간
    line = f.readline()
    if not line: break
    line = line.split(",")
    idA.append(line[0])
    moneyA.append(int(line[1]))
    timeA.append(int(line[2]))
while True:
    line = w.readline()
    if not line: break
    preA.append(line)


f.close()

@client.event
async def on_ready(): #봇이 켜지면
    print("봇 아이디: ", client.user.id)
    print("봇 준비 완료")

@client.event
async def on_message(message):
    if message.content == "/코인받기":
        ID = str(message.author.id)
        TIME = int(time.time())
        if ID in idA: #만약 등록된 ID라면
            if TIME - timeA[idA.index(ID)] < 180: #1시간이 안 지났을 때
                embed = discord.Embed(title='SkyBOT 도박 : Error', description='3분 마다 받을 수 있습니다.', color=0xFF0000)
                await message.channel.send(embed=embed)
                raise ValueError #탈출
            elif TIME - timeA[idA.index(ID)] >= 180: #1시간이 지났을 때
                timeA[idA.index(ID)] = int(time.time())
        give = random.randrange(1,10)*random.randrange(1000,10000) # 줄 돈
        if ID in idA:
            moneyA[idA.index(ID)] += give
            f = open("UserData.txt", "w") #저장
            for i in range(0,len(idA),1):
                f.write(str(idA[i])+","+str(moneyA[i])+","+str(timeA[i])+"\n")
            f.close()
        elif not ID in idA:
            idA.append(ID)
            moneyA.append(give)
            timeA.append(int(time.time()))
            f = open("UserData.txt", "w") #저장
            for i in range(0,len(idA),1):
                f.write(str(idA[i])+","+str(moneyA[i])+","+str(timeA[i])+"\n")
            f.close()
        msg = str(give)+"코인을 받았습니다. 현재 스카이코인 : "+str(moneyA[idA.index(ID)])+"코인"
        embed = discord.Embed(title='', description=msg, color=0x00FF00)
        await message.channel.send(embed=embed)
    if message.content.startswith("/도박"):
        ID = str(message.author.id)
        msg = message.content.split()
        if msg[1].isdecimal() == False: #만약 숫자가 아니라면
            embed = discord.Embed(title='SkyBOT 도박 : Error', description='숫자외에 다른 내용이 들어가 있어요!', color=0xFF0000)
            await message.channel.send(embed=embed)
            raise ValueError
        msg[1] = int(msg[1])
        if not ID in idA or moneyA[idA.index(ID)] - int(msg[1]) < 0: #등록된 ID가 아니거나 돈이 부족하면
            embed = discord.Embed(title='SkyBOT 도박 : Error', description='보유한 돈보다 높은돈을 거실수 없어요!', color=0xFF0000)
            await message.channel.send(embed=embed)
            raise ValueError #탈출
        moneyA[idA.index(ID)] -= msg[1]
        give = random.randrange(1,11)
        await asyncio.sleep(1)
        adminlist = [488670402118156298, 653075791814590487] #관리자
        if message.author.id in adminlist: #관리자라면 테슽 할것도 있고 하니 돈 많이 줌
            give = 999
        if not ID in preA:
            if give % 2 == 0 or message.author.id in adminlist: #어드민일 때는 무조건 도박 성공
                moneyA[idA.index(ID)] += give*msg[1]
                embed = discord.Embed(title="도박 성공!", description="도박을 성공하여 [ "+str(give)+"배 ] 의 돈을 얻었어요! \n \n 현재 스카이코인 • "+str(moneyA[idA.index(ID)])+" 코인", timestamp=message.created_at,
                colour = discord.Colour.dark_green()
    )
                embed.set_footer(text="도박 확률은 50 : 50이에요!")
                await message.channel.send(embed=embed)
            elif give % 2 != 0:
                embed = discord.Embed(title="도박 실패..", description="도박을 성공했으면 [ "+str(give)+"배 ] 의 돈을 얻을 수 있었는데 실패했네요.. \n \n 현재 스카이코인 • "+str(moneyA[idA.index(ID)])+" 코인", timestamp=message.created_at,
                colour = discord.Colour.dark_red()
    )
                embed.set_footer(text="도박 확률은 50 : 50이에요!")
                await message.channel.send(embed=embed)
            f = open("UserData.txt", "w") #저장
            for i in range(0,len(idA),1):
                f.write(str(idA[i])+","+str(moneyA[i])+","+str(timeA[i])+"\n")
                f.close()
        else:
            give = random.randrange(1,11)
            moneygive = random.randrange(5,21)
            if give == 1 or give == 2:
                embed = discord.Embed(title="도박 실패..", description="도박을 성공했으면 [ " + str(moneygive) + "배 ] 의 돈을 얻을 수 있었는데 실패했네요.. \n \n 현재 스카이코인 • " + str(moneyA[idA.index(ID)]) + " 코인",timestamp=message.created_at,colour=discord.Colour.dark_red())
                embed.set_footer(text="프리미엄 유저의 도박 확률은 80 : 20 이에요!")
                await message.channel.send(embed=embed)
            elif give <= 3:
                moneyA[idA.index(ID)] += give * msg[1]
                embed = discord.Embed(title="도박 성공!",description="도박을 성공하여 [ " + str(moneygive) + "배 ] 의 돈을 얻었어요! \n \n 현재 스카이코인 • " + str(
                                          moneyA[idA.index(ID)]) + " 코인", timestamp=message.created_at,
                                      colour=discord.Colour.dark_green()
                                      )
                embed.set_footer(text="도박 확률은 80 : 20 이에요!")
                await message.channel.send(embed=embed)
            f = open("UserData.txt", "w")  # 저장
            for i in range(0, len(idA), 1):
                f.write(str(idA[i]) + "," + str(moneyA[i]) + "," + str(timeA[i]) + "\n")
                f.close()






    if message.content == "/코인":
        ID = str(message.author.id)
        if ID in idA: #만약 등록된 ID라면
            embed = discord.Embed(title=f'{message.author.name}님이 보유한 코인', description=str(moneyA[idA.index(ID)])+" 코인", color=0x118811)
            await message.channel.send(embed=embed)
        elif not ID in idA: #등록된 ID가 아니라면
            embed = discord.Embed(title='보유한 돈', description="0 원", color=0x118811)
            await message.channel.send(embed=embed)
    if message.content == "/랭킹":
        embed = discord.Embed(title='', description='랭킹', color=0x118811)
        filt = moneyA.sort(reverse=True)
        embed.add_field(name=f"1위", value=f"{filt[1]}원 보유")
        embed.add_field(name=f"2위", value=f"{filt[2]}원 보유")
        embed.add_field(name=f"3위", value=f"{filt[3]}원 보유")

    if message.content == "/올인":
        ID = str(message.author.id)
        if not ID in idA or moneyA[idA.index(ID)] <= 0: #만약 돈이 부족하면
            embed = discord.Embed(title='', description='코인이 부족합니다.', color=0xFF0000)
            await message.channel.send(embed=embed)
            raise ValueError
        give = random.randrange(2,10)
        await asyncio.sleep(1)
        if give % 2 == 0:
            moneyA[idA.index(ID)]*= give
            embed = discord.Embed(title="SkyBOT 도박 올인 : 성공", description="올인을 성공하여 [ "+str(give)+"배 ] 의 코인을 얻었어요! \n \n 현재 스카이코인 • "+str(moneyA[idA.index(ID)])+" 코인", timestamp=message.created_at,
            colour = discord.Colour.dark_green()       
    )
            embed.set_footer(text="올인 확률은 50 : 50이에요!")
            await message.channel.send(embed=embed)
        elif give % 2 != 0:
            moneyA[idA.index(ID)] = 0
            embed = discord.Embed(title="SkyBOT 도박 올인 : 실패", description="올인을 성공했으면 [ "+str(give)+"배 ] 의 코인을 얻을 수 있었는데 실패했네요.. \n \n 현재 스카이코인 • "+str(moneyA[idA.index(ID)])+" 코인", timestamp=message.created_at,
            colour = discord.Colour.dark_red()       
    )
            embed.set_footer(text="올인 확률은 50 : 50이에요!")
            await message.channel.send(embed=embed)
        f = open("UserData.txt", "w") #저장
        for i in range(0,len(idA),1):
            f.write(str(idA[i])+","+str(moneyA[i])+","+str(timeA[i])+"\n")
        f.close()

client.run("Token")
