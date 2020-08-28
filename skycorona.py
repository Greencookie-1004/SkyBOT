import discord
import asyncio
import json
import urllib
from urllib.request import Request
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen 
from urllib.request import Request, urlopen
from urllib.request import quote
from urllib import parse

client = discord.Client()

@client.event
async def on_message(message):
    co = False
    if message.content == "/코로나:순":
        with urllib.request.urlopen("http://api.corona-19.kr/korea/?serviceKey=5533c7d6fa9cff4aaf98ba8cfa641860d") as url:
            data = json.loads(url.read().decode())
            print(data["resultMessage"])
            embed = discord.Embed(title="코로나-19 감염 지역 순위", description="🇰🇷코로나는 코리아를 이길 수 없습니다!",
                                  colour=discord.Colour.teal())
            for i in range(1, 5):
                embed.add_field(name=f"{i}번째로 많음", value=data[f"city{i}n"] + "(" + data[f"city{i}p"] + "퍼센트)")
            await message.channel.send(embed=embed)
            co = True
    if message.content.startswith("/코로나") and co == False:
        with urllib.request.urlopen("http://api.corona-19.kr/korea/country/new/?serviceKey=5533c7d6fa9cff4aaf98ba8cfa641860d") as url:
            data = json.loads(url.read().decode())
            print(data["resultMessage"])
            try:
                split = message.content.split(" ")
                if split[1] == "test": print("A")
            except IndexError:
                c = "korea"
                embed = discord.Embed(title="대한민국의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",
                                      colour=discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",
                                inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "전체":
                c = "korea"
                embed = discord.Embed(title="대한민국의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")", inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "서울":
                c = "seoul"
                embed = discord.Embed(title="서울의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")", inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "부산":
                c = "busan"
                embed = discord.Embed(title="부산의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "대구":
                c = "daegu"
                embed = discord.Embed(title="대구의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "인천":
                c = "incheon"
                embed = discord.Embed(title="인천의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "광주":
                c = "gwangju"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "대전":
                c = "daejeon"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "울산":
                c = "ulsan"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "세종":
                c = "sejong"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "경기" or split[1] == "경기도":
                c = "gyeonggi"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "강원" or split[1] == "강원도":
                c = "gangwon"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "충북" or split[1] == "충청북도":
                c = "chungbuk"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "충남" or split[1] == "충청남도":
                c = "chungnam"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "전북" or split[1] == "전라북도":
                c = "jeonbuk"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "전남" or split[1] == "전라남도":
                c = "jeonnam"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "경북" or split[1] == "경상북도":
                c = "gyeongbuk"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "경남" or split[1] == "경상남도":
                c = "gyeongnam"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "제주" or split[1] == "제주도":
                c = "jeju"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)
            if split[1] == "검역":
                c = "quarantine"
                embed = discord.Embed(title=split[1] + "의 COVID-19 통계", description="코로나는 우리를 이길수 없어요!",colour = discord.Colour.teal())
                embed.add_field(name="누적 확진자", value=data[c]["totalCase"] + "(+" + data[c]["newCase"] + ")",inline=False)
                embed.add_field(name="회복", value=data[c]["recovered"], inline=False)
                embed.add_field(name="사망", value=data[c]["death"], inline=False)
                await message.channel.send(embed=embed)


client.run('')
