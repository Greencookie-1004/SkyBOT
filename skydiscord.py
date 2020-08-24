 # To make a discord app you need to download discord.py with pip
#-*- coding: utf-8 -*-
import discord
from discord.ext import commands
from discord.utils import get
import asyncio
from Dtime import Uptime
from captcha.image import ImageCaptcha
import random
import datetime
import urllib
from urllib.request import Request
import bs4
from urllib.request import URLError
from urllib.request import HTTPError
from urllib.request import urlopen 
from urllib.request import Request, urlopen
from urllib.request import quote
from bs4 import BeautifulSoup
from urllib import parse
import warnings
import requests
import json
import re
import openpyxl
import koreanbots
import os, random, time
from discord import Member
import youtube_dl
import sys
from selenium import webdriver
import time

client = discord.Client()

Bot = koreanbots.Client(client, 'eyJhbGciOiJSUzI1NiIsInR5cCI6IkpXVCJ9.eyJpZCI6IjczNjEzNTY3Mjg0MjQyMDMyNiIsImlhdCI6MTU5NjUzOTk1NSwiZXhwIjoxNjI4MDk3NTU1fQ.LhkMBnjpdo1K9EAacYXEf_VCbGmY64hrJVPN0f8P79WXB64VotPfMI5TWtQTksnqdY2DetOx1eqQnlRfDolu5yQg_DwFmAJzLGiRuUx9bPdqBYZfuePTXTFhbcPCHXjEr-fiGHZfdcQTVzVgPbgiZJEKICBsEXuTI-rcscBFTnI')

owner = [653075791814590487 , 724769557759393837]

Uptime.uptimeset()

@client.event
async def on_ready():
    print('봇이 로그인 하였습니다.')
    print(' ')
    print('닉네임 : {}'.format(client.user.name))
    print('아이디 : {}'.format(client.user.id))
    while True:
        user = len(client.users)
        server = len(client.guilds)
        messages = ["제 접두사는 / 입니다!", "건의는 ∑」Greencookie#3907 또는 ∑」바나나#1234 에게 해주세요!" , "저는 SKY BOT TEAM 에서 개발, 관리되고 있어요!" , str(user) + "분의 디스코드를 함께하고 있어요!", str(server) + "개의 서버에 있다구요!"]
        for (m) in range(5):
            await client.change_presence(status=discord.Status.dnd, activity=discord.Activity(name=messages[(m)], type=discord.ActivityType.watching))
            await asyncio.sleep(4)

@client.event
async def on_message(message):
    if message.content == '/공지채널':
        embed = discord.Embed(title="SkyBOT 공지채널", description="SkyBOT의 공지는 기본적으로 랜덤한 채널에 올라옵니다. \n 하지만, 특정 키워드가 들어간 채널이 있을경우 해당 채널로 공지가 발송됩니다. \n 발송 우선순위 채널 - **[ SkyBOT-공지 ] , [ 봇-공지 ] , [ 봇_공지 ] , [ 봇공지 ] , [ bot_announcement ]**")
        embed.set_footer(text="원하는 특정 키워드가 있으면 /피드백 으로 알려주세요!")
        await message.channel.send(embed=embed)

    if message.content.startswith("/제작도움"):
        embed = discord.Embed(title="제작을 도와주신분!", description="총개발자 - ∑」Cookie#3907 \n \n 일부 코드 도움 - ∑」 Apple#9999, djs226587#1243", timestamp=message.created_at,
        colour=discord.Colour.teal()
        )
        embed.set_footer(text=message.author.name + " | Sky BOT#2208", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith("/초대"):
        embed = discord.Embed(title="SkyBOT 초대하기!", description="[봇 초대하기](https://discord.com/api/oauth2/authorize?client_id=736135672842420326&permissions=8&scope=bot)", timestamp=message.created_at,
        colour=discord.Colour.teal()
        )
        embed.set_footer(text=message.author.name + " | Sky BOT#2208", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == "/내아이디":
        embed = discord.Embed(title="아이디 정보", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.add_field(name=f"아이디 확인 결과", value=f"`{message.author.id}`가 {message.author.mention}님의 아이디에요!")
        embed.set_footer(text=message.author.name + " | Sky BOT#2208  스카이봇은 2명이 개발하고 있어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content.startswith('/아이디'):
        memb = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
        embed = discord.Embed(title="아이디 확인 결과", description=f"`{memb.id}` 가 {memb.mention}님의 아이디에요!", timestamp=message.created_at,
        colour = discord.Colour.purple()    
    )
        embed.set_footer(text=message.author.name)
        await message.channel.send(embed=embed)
        

    if message.content.startswith("/핑"):
        la = client.latency
        embed = discord.Embed(title="퐁!")
        embed.add_field(name="반응 속도", value=str(round(la * 1000)) + "ms")
        embed.set_footer(text=message.author.name + " | Sky BOT#2208  스카이봇은 2명이 개발하고 있어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)

    if message.content == '/내정보':
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        roles=[role for role in message.author.roles]
        embed=discord.Embed(colour=message.author.color, timestamp=message.created_at)
        embed.set_author(name=f"{message.author}님의 정보!")
        embed.set_thumbnail(url=message.author.avatar_url)
        embed.set_footer(text=f"{message.author}님에 의해 제공되었어요!", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=message.author.id, inline = False)
        embed.add_field(name="닉네임", value=message.author.display_name,  inline = False)
        embed.add_field(name="계정 생성 시간", value=message.author.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=message.author.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=message.author.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =message.author.status, inline = False)
        await message.channel.send(embed=embed)

    if message.content.startswith('/정보'):
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
        roles=[role for role in user.roles]
        embed=discord.Embed(colour=user.color, timestamp=message.created_at)
        embed.set_author(name=f"{user}님의 정보!")
        embed.set_thumbnail(url=user.avatar_url)
        embed.set_footer(text=f"{message.author}님에 의해 제공되었어요!", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=user.id, inline = False)
        embed.add_field(name="닉네임", value=user.display_name, inline = False)
        embed.add_field(name="계정 생성 시간", value=user.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=user.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=user.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =user.status, inline = False)
        await message.channel.send(embed=embed)

    if message.content.startswith('/정보'):
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        user2 = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
        roles=[role for role in user2.roles]
        embed=discord.Embed(colour=user2.color, timestamp=message.created_at)
        embed.set_author(name=f"{user2}님의 정보!")
        embed.set_thumbnail(url=user2.avatar_url)
        embed.set_footer(text=f"{message.author}님에 의해 제공되었어요!", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=user2.id, inline = False)
        embed.add_field(name="닉네임", value=user2.display_name, inline = False)
        embed.add_field(name="계정 생성 시간", value=user2.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=user2.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=user2.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =user2.status, inline = False)
        await message.channel.send(embed=embed)

    if message.content.startswith('/정보'):
        print(f'{message.guild.name}/{message.author} ('+ f'{message.author.id}) : {message.content}')
        use = message.guild.get_member(int(message.content.split(' ')[1][4:22]))
        roles=[role for role in use.roles]
        embed=discord.Embed(colour=message.author.color, timestamp=message.created_at)
        embed.set_author(name=f"{use}님의 정보!")
        embed.set_thumbnail(url=use.avatar_url)
        embed.set_footer(text=f"{message.author}님에 의해 제공되었어요!", icon_url=message.author.avatar_url)
        embed.add_field(name="ID", value=use.id, inline = False)
        embed.add_field(name="닉네임", value=use.display_name, inline = False)
        embed.add_field(name="계정 생성 시간", value=use.created_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name="가입 시간", value=use.joined_at.strftime("%a, %#d %B %Y, %I:%M %p UTC"), inline = False)
        embed.add_field(name=f"소유한 역할 ({len(roles)})", value=" ".join([role.mention for role in roles]), inline = False)
        embed.add_field(name="가장 높은등급인 역할", value=use.top_role.mention,  inline = False)
        embed.add_field(name ="상태", value =use.status, inline = False)
        await message.channel.send(embed=embed)

    if message.content == '/서버정보':
        rnrrk = message.guild.region
        print(message.guild.region)
        embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at, title=f"{message.guild.name}")
        embed.set_thumbnail(url=message.guild.icon_url)
        embed.add_field(name="서버 이름", value=message.guild.name, inline=False)
        embed.add_field(name="서버 ID", value=message.guild.id, inline=False)
        embed.add_field(name="서버 국가", value=rnrrk, inline=False)
        embed.add_field(name="서버 Owner", value=f'<@{message.guild.owner.id}>', inline=False)
        embed.add_field(name="서버 Owner ID", value=message.guild.owner.id, inline=False)
        embed.add_field(name="서버 멤버 수", value=f'{len(message.guild.members)}명 (봇 : {len(list(filter(lambda x: x.bot, message.guild.members)))}명 | 유저 : {len(list(filter(lambda x: not x.bot, message.guild.members)))}명)', inline=False)
        embed.add_field(name="서버 채널 수", value=f'전체 채널: {len(message.guild.channels)}개 (채팅채널 : {len(message.guild.text_channels)}개 | 음성채널 : {len(message.guild.voice_channels)}개 | 카테고리 : {len(message.guild.categories)}개)', inline=False)
        embed.add_field(name="서버 부스트 레벨", value=f'{message.guild.premium_tier}레벨', inline=False)
        embed.add_field(name="서버 부스트 횟수", value=f'{message.guild.premium_subscription_count}번', inline=False)
        if message.guild.afk_channel != None:
            embed.add_field(name = f'잠수 채널', value = f'<#{message.guild.afk_channel.id}> \n ( 시간 제한 : {message.guild.afk_timeout} 초 )', inline = False)
        else:
            embed.add_field(name="잠수 채널", value="잠수 채널이 없습니다.")
        if message.guild.system_channel != None:
            embed.add_field(name = f'시스템 채널', value = f'<#{message.guild.system_channel.id}>', inline = False)
        else:
            embed.add_field(name="잠수 채널", value="시스템 채널이 없습니다.")
        embed.set_footer(text=f"{message.author}, 인증됨 | 준홍봇의 코드를 참고했어요!", icon_url=message.author.avatar_url)
        await message.channel.send(embed=embed)


    if message.content.startswith("/계산"):
        global calcResult
        param = message.content.split()
        try:
            if param[1].startswith("더하기"):
                calcResult = int(param[2])+int(param[3])
                if calcResult < 1000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 더하기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 1000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 더하기 결과 ", description="계산 결과가 [ 1, 000, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
            if param[1].startswith("빼기"):
                calcResult = int(param[2])-int(param[3])
                if calcResult < 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 빼기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 빼기 결과 ", description="계산 결과가 [ 100, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
            if param[1].startswith("곱하기"):
                calcResult = int(param[2])*int(param[3])
                if calcResult < 10000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 곱하기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 10000000000:
                    embed = discord.Embed(title="SkyBOT : 계산 곱하기 결과 ", description="계산 결과가 [ 10, 000, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
            if param[1].startswith("나누기"):
                calcResult = int(param[2])/int(param[3])
                if calcResult < 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 나누기 결과 ", description="계산 결과는 [ "+str(calcResult)+" ] 인것 같아요!")
                    await message.channel.send(embed=embed)
                elif calcResult >= 100000000:
                    embed = discord.Embed(title="SkyBOT : 계산 나누기 결과 ", description="계산 결과가 [ 100, 000, 000 ] 을 넘었어요!", timestamp=message.created_at,
                    colour = discord.Colour.red()
            )
                    await message.channel.send(embed=embed)
        except IndexError:
            embed = discord.Embed(title="SkyBOT : 계산 오류", description="2개의 숫자가 포함되지 않았어요!", timestamp=message.created_at,
            colour = discord.Colour.dark_red()        
        )
            await message.channel.send(embed=embed)
        except ValueError:
            await message.channel.send("숫자로 넣어주세요.")
        except ZeroDivisionError:
            await message.channel.send("You can't divide with 0.")

    if message.content == "/도움말" or message.content == "/명령어":
        embed = discord.Embed(title="🔨ㅣSky BOT 도움말", timestamp=message.created_at,
        colour=discord.Colour.gold()
    )
        embed.add_field(name="/도움말 기본, /명령어 기본", value="봇의 기본 명령어들입니다.", inline=False)
        embed.add_field(name="/도움말 관리, /명령어 관리", value="봇의 관리 명령어들입니다.", inline=False)
        embed.add_field(name="/도움말 도박, /명령어 도박", value="봇의 도박 명령어들입니다.", inline=False)
        embed.add_field(name="/도움말 지식, /명령어 지식", value="봇의 지식 명령어들입니다.", inline=False)
        embed.add_field(name="/도움말 검색, /명령어 검색", value="봇의 검색 명령어들입니다.", inline=False)
        embed.add_field(name="/도움말 정보, /명령어 정보", value="봇의 정보 명령어들입니다.", inline=False)
        embed.add_field(name="/도움말 기타, /명령어 기타", value="봇의 기타 명령어들입니다.", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content == "/도움말 기본" or message.content == '/명령어 기본':
        embed = discord.Embed(title="📗ㅣSKYBOT 기본 명령어", timestamp=message.created_at, 
        colour=discord.Colour.dark_blue()    
    )
        embed.add_field(name="/도움말, /명령어", value="SkyBOT의 도움말을 보여드려요!", inline=False)
        embed.add_field(name="/핑", value="SkyBOT의 핑 ( 반응 속도 ) 를 알려드려요!", inline=False)
        embed.add_field(name="/업타임", value="SkyBOT의 업타임을 알려드려요!", inline=False)
        embed.add_field(name="/초대", value="SkyBOT의 초대링크가 포함된 메시지를 보내요!", inline=False)
        embed.add_field(name="/피드백 [ 내용 ]", value="SkyBOT의 개발자에게 [ 내용 ] 을 보내요!", inline=False)
        embed.add_field(name="/하트", value="하트를 눌러주세요!", inline=False)
        embed.add_field(name="/봇정보", value="봇의 기본 정보들이 담겼습니다!", inline=False)
        embed.add_field(name="/공지채널", value="공지채널에 대해서 알려드려요!", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content == "/도움말 관리" or message.content == '/명령어 관리':
        embed = discord.Embed(title="🔨ㅣSKYBOT 관리 명령어", timestamp=message.created_at,
        colour = discord.Colour.dark_teal()    
    )
        embed.add_field(name="/청소 [ 메시지 수 ]", value="[ 메시지 수 ] 에 해당하는 숫자 - 1 만큼의 메시지가 지워집니다! \n /청소 11 을 적으면 10개를 지우는것과 같습니다!", inline=False)
        embed.add_field(name="/킥 [ 멘션 ] [ 사유 ]", value="[ 멘션 ] 된 유저를 [ 사유 ] 로 인해 서버에서 추방합니다! \n 사유를 적지않으면 사유가 None으로 표시됩니다.", inline=False)
        embed.add_field(name="/밴 [ 멘션 ] [ 사유 ]", value="[ 멘션 ] 된 유저를 [ 사유 ] 로 인해 서버에서 차단합니다! \n 사유를 적지않으면 사유가 None으로 표시됩니다.", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!ㅣ해당 명령어들은 서버 관리자 권한이 있는 사람만 가능해요!")
        await message.channel.send(embed=embed)

    if message.content == '/도움말 기타' or message.content == '/명령어 기타':
        embed = discord.Embed(title="🎸ㅣSKYBOT 기타 명령어", timestamp=message.created_at,
        colour = discord.Colour.dark_gold()    
    )
        embed.add_field(name="/캡챠, /캡차", value="랜덤한 숫자가 담긴 캡챠 인증코드를 발송합니다!", inline=False)
        embed.add_field(name="/낚시", value="랜덤한 확률로 물고기 또는 무언가를 낚습니다! [ 틀만 잡힌 기능입니다. ]", inline=False)
        embed.add_field(name="/주사위", value="1부터 6까지의 숫자중 랜덤한 숫자가 나옵니다!", inline=False)
        embed.add_field(name="/복권", value="랜덤하게 번호를 출력합니다.", inline=False)
        embed.add_field(name="/시간", value="현재 시간을 출력합니다.", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content == '/도움말 도박' or message.content == '/명령어 도박':
        embed = discord.Embed(title="🎰ㅣSKYBOT 도박 명령어", timestamp=message.created_at,
        colour = discord.Colour.dark_magenta()    
    )
        embed.add_field(name="/코인받기", value="1000코인 ~ 100000코인 중 랜덤하게 받아요! ( 쿨타임 3분 )", inline=False)
        embed.add_field(name="/코인", value="본인의 코인 수를 확인해요!", inline=False)
        embed.add_field(name="/도박 [ 수 ]", value="[ 수 ] 만큼의 돈으로 도박을 해요! ( 확률 50 : 50 )", inline=False)
        embed.add_field(name="/올인", value="소지하고 있는 모든 돈으로 도박을 해요! ( 확률 50 : 50 )", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content == '/도움말 지식' or message.content == '/명령어 지식':
        embed = discord.Embed(title="📘ㅣSKYBOT 지식 명령어", timestamp=message.created_at,
        colour = discord.Colour.dark_teal()    
    )
        embed.add_field(name="/배워 [ A ] [ B ]", value="[ A ] 를 말하면 [ B ] 로 대답하게 가르칩니다! \n ex ) /배워 안녕 반가워요!", inline=False)
        embed.add_field(name="카이야 [ A ]", value="/배워 로 가르쳤던 내용의 [ A ] 를 적으면 [ B ] 가 나옵니다! \n ex ) /말해 안녕", inline=False)
        embed.add_field(name="/잊어 [ A ]", value="/배워 로 가르쳤던 내용의 [ A ] 를 적으면 해당 기억을 잊어버립니다. \n ※ 해당 명령어를 사용하면 다시 추가하기 전까지 삭제됩니다.", inline=False)
        embed.add_field(name="/기억초기화, /기억 초기화", value="[ Owner 전용 ] 모든 기억을 초기화합니다.", inline=False)
        embed.set_footer(name="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content == '/도움말 검색' or message.content == '/명령어 검색':
        embed = discord.Embed(title="🔎ㅣSKYBOT 검색 명령어", timestamp=message.created_at,
        colour = discord.Colour.teal()    
    )
        embed.add_field(name='/날씨 [ 지역 ]', value="[ 지역 ] 의 정보를 출력합니다. \n 국내 지역만 지원합니다.", inline=False)
        embed.add_field(name="/이미지 [ 검색어 ]", value="[ 검색어 ] 에 알맞는 이미지를 랜덤하게 출력합니다. \n 정확도가 다소 떨어질 수 있습니다.", inline=False)
        embed.add_field(name="/실검", value="네이버 실시간 검색어 순위를 출력합니다.", inline=False)
        embed.add_field(name="/계산 [ 더하기/빼기/곱하기/나누기 ] [ 수 ] [ 수 ] ...", value="[ 더하기/뺴기/곱하기/나누기 ] 로 [ 수 ] 들을 계산합니다. \n 사용 예시 ) /계산 더하기 1 2 3 5", inline=False)
        embed.add_field(name="/코로나", value="국내 코로나 정보를 출력합니다. \n Made by J-hoplin", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content == '/도움말 정보' or message.content == '/명령어 정보':
        embed = discord.Embed(title="📃ㅣSKYBOT 정보 명령어", timestamp=message.created_at,
        colour = discord.Colour.dark_teal()    
    )
        embed.add_field(name="/내정보", value="본인의 정보를 출력합니다.", inline=False)
        embed.add_field(name="/정보 [ 멘션 ]", value="멘션된 유저의 정보를 출력합니다.", inline=False)
        embed.add_field(name="/내아이디", value="본인의 아이디를 출력합니다.", inline=False)
        embed.add_field(name="/아이디 [ 멘션 ]", value="멘션된 유저의 아이디를 출력합니다.", inline=False)
        embed.set_footer(text="스카이봇 개발자는 ∑」Cookie**#3907, ∑」wave**#1234 이에요!")
        await message.channel.send(embed=embed)

    if message.content.startswith("/캡챠") or message.content.startswith("/캡차"):
        Image_captcha = ImageCaptcha()
        msg = ""
        a = ""
        for i in range(6):
            a += str(random.randint(0, 9))

        name = "Captcha.png"
        Image_captcha.write(a, name)

        await message.channel.send(file=discord.File(name))
        embed = discord.Embed(title="인증코드", description = message.author.mention + ", 위에 있는 인증코드를 10초내에 입력해주세요.", timestamp=message.created_at,
        colour=discord.Colour.blurple()
    )
        embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
        await message.channel.send(embed=embed)

        def check(msg):
            return msg.author == message.author and msg.channel == message.channel

        try:
            msg = await client.wait_for("message", timeout=10, check=check)
        except:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증시간 ( 10초 ) 를 초과했습니다.", timestamp=message.created_at,
            colour=discord.Colour.orange()
    )
            embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await message.channel.send(embed=embed)

        if msg.content == a:
            embed = discord.Embed(title="성공!", description = message.author.mention + ", __**Captcha**__ 인증시간 내에 올바른 인증코드를 작성했습니다.", timestamp=message.created_at,
            colour=discord.Colour.green()
    )
            embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await message.channel.send(embed=embed)
        
        else:
            embed = discord.Embed(title="실패!", description = message.author.mention + ", __**Captcha**__ 인증코드가 올바르지 않습니다.", timestamp=message.created_at,
            colour=discord.Colour.red()
    )
            embed.set_footer(text="Sky BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await message.channel.send(embed=embed)
        
       

    if (message.content.split(" ")[0] == "/밴"):
        if (message.author.guild_permissions.ban_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][3:21]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="💥 서버 추방", description=f'당신은 **{message.guild.name}** 서버에서 차단되었습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.ban(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Ban Success", description=f"{message.author.mention} 님, 성공적으로 차단시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 차단할 수 있는 권한이 없습니다.", color=0xff0000))
            return

    if (message.content.split(" ")[0] == "/킥"):
        if (message.author.guild_permissions.kick_members):
            try:
                user = message.guild.get_member(int(message.content.split(' ')[1][2:20]))
                reason = message.content[22:]
                if (len(message.content.split(" ")) == 2):
                    reason = "None"
                await user.send(embed=discord.Embed(title="💥 서버 추방", description=f'당신은 **{message.guild.name}** 서버에서 추방되었습니다. 사유는 다음과 같습니다. ```{reason}```', color=0xff0000))
                await user.kick(reason=reason)
                await message.channel.send(embed=discord.Embed(title="Kick Success", description=f"{message.author.mention} 님, 성공적으로 추방시켰습니다. 사유:```{reason}```", color=0x00ff00))
            except Exception as e:
                await message.channel.send(embed=discord.Embed(title="❌ 에러 발생", description=str(e), color=0xff0000))
                return
        else:
            await message.channel.send(embed=discord.Embed(title="⚠ 권한 부족", description=message.author.mention + "님은 유저를 추방할 수 있는 권한이 없습니다.", color=0xff0000))
            return
 
    if message.content.startswith("/피드백"):
        Dansdml1 = message.content[5:]
        Dansdml = discord.Embed(title="**< Space BOT >**", color=0x6777ff)
        Dansdml.add_field(name="• 문의하는 내용", value=f"{Dansdml1}\n\n• 문의하는 서버 : {message.guild.name}\n• 문의한 이용자 : {message.author.mention}", inline=False)
        Dansdml.set_thumbnail(url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
        Dansdml.set_footer(text=message.author.name + " | 피드백 코드의 원본은 djs226587#1243 님의 코드에요 !", icon_url=message.author.avatar_url)
        m = await message.channel.send("문의발송 여부를 선택하여주세요.", embed=Dansdml)
        await m.add_reaction('✅')
        await m.add_reaction('❎')
        try:
            reaction, user = await client.wait_for('reaction_add', timeout = 5, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
        except asyncio.TimeoutError:
            Drhdwltlrks = discord.Embed(title="**< Space BOT >**", color=0xff0000)
            Drhdwltlrks.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송 선택 시간초과입니다.**", inline=False)
            Drhdwltlrks.set_thumbnail(url=message.author.avatar_url)
            Drhdwltlrks.set_footer(text="Sky BOT#2204 | 피드백 코드의 원본은 djs226587#1243 님의 코드에요 !" , icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
            await m.edit(content="문의발송이 취소되었습니다.", embed=Drhdwltlrks)
        else:
            if str(reaction.emoji) == "❎":
                Drhdwlcnlth = discord.Embed(title="**< Space BOT >**", color=0xff0000)
                Drhdwlcnlth.add_field(name="**문의**", value=f"{message.author.mention} **님 문의발송이 취소되었습니다.**", inline=False)
                Drhdwlcnlth.set_thumbnail(url=message.author.avatar_url)
                Drhdwlcnlth.set_footer(text="Sky BOT#2204 | 피드백 코드의 원본은 djs226587#1243 님의 코드에요 !" , icon_url="https://cdn.discordapp.com/attachments/736382917072257107/736383011125461072/skybot.png")
                await m.edit(embed=Drhdwlcnlth)
            elif str(reaction.emoji) == "✅":
                await m.edit(content="서포트 서버에 피드백이 발송되었어요!", embed=Dansdml)
                await client.get_channel(int(737624237925466154)).send(embed=Dansdml)

    if message.content == "/실검":
        url = "https://m.search.naver.com/search.naver?query=%EC%8B%A4%EA%B2%80"
        html = urlopen(url)
        parse = BeautifulSoup(html, "html.parser")
        result = ""
        tags = parse.find_all("span", {"class" : "tit _keyword"})
        for i, e in enumerate(tags):
            result = result + (str(i+1))+"위 | "+e.text+"\n"
        await message.channel.send(result)


    if message.content.startswith("/공지"):
            if message.author.id in owner:
                if str(message.content[7:]) == '' or str(message.content[7:]) == ' ':
                    await message.channel.send("메세지를 쓰세요.")
                try:
                    msg = message.content[4:]
                    oksv = 0
                    embed = discord.Embed(
                        title = msg.split('&&')[0],
                        description = msg.split('&&')[1] + f"\n \n[서포트 서버](https://discord.gg/g5cEJzk)",
                        colour = discord.Colour.gold(),
                        timestamp = message.created_at
                    ).set_footer(icon_url=message.author.avatar_url, text=f'{message.author} - Developer | 봇 공지는 기본적으로 랜덤 채널에 발송돼요! 자세한 설명은 /공지채널!') .set_thumbnail(url=client.user.avatar_url_as(format=None, static_format="png", size=1024))
                except IndexError:
                    await message.channel.send("형식이 틀렸습니다. ``*공지 <제목>&&<내용>``으로 다시 시도해보세요.")
                m = await message.channel.send("아래와 같이 공지가 발신됩니다.", embed=embed)
                await m.add_reaction('✅')
                await m.add_reaction('❎')
                try:
                    reaction, user = await client.wait_for('reaction_add', timeout = 20, check = lambda reaction, user: user == message.author and str(reaction.emoji) in ['✅', '❎'])
                except asyncio.TimeoutError:
                    await message.channel.send('시간이 초과되었습니다.')
                else:
                    if str(reaction.emoji) == "❎":
                        await message.channel.send("공지발신을 취소하였어요")
                    elif str(reaction.emoji) == "✅":
                        await m.edit(content="발신중입니다...", embed=embed)
                        for i in client.guilds:
                            arr = [0]
                            alla = False
                            flag = True
                            z = 0
                            for j in i.channels:
                                arr.append(j.id)
                                z+=1
                                if "SkyBOT-공지" in j.name or"봇-공지" in j.name or "봇_공지" in j.name or "봇공지" in j.name or "bot_announcement" in j.name or "테스트1" in j.name:
                                    if str(j.type)=='text':
                                        try:
                                            oksv += 1
                                            await j.send(embed=embed)
                                            alla = True
                                        except:
                                            pass
                                        break
                            if alla==False:
                                try:
                                    chan=i.channels[1]
                                except:
                                    pass
                                if str(chan.type)=='text':
                                    try:
                                        oksv += 1
                                        await chan.send(embed=embed)
                                    except:
                                        pass
                        await message.channel.send(f"**📢 공지 가 성공적으로 발신되었습니다. 📢**\n\n{len(client.guilds)}개의 서버 중에서  {oksv}개의 서버에 발신 완료했습니다., {len(client.guilds) - oksv}개의 서버에 발신 실패했습니다.")
                        await m.edit(content="발신이 완료되었습니다!", embed=embed)
            else:
                await message.channel.send('이 명령어를 쓰려면 최소 Bot Developer 권한이 필요합니다.')

    if message.content.startswith("/청소"):
        if message.author.guild_permissions.manage_messages:
            try:
                amount = message.content[4:]
                await message.channel.purge(limit=int(amount))
                embed = discord.Embed(title="청소 완료!", description=f"{message.author.mention}, **{amount}** 개의 메시지를 청소했어요!", timestamp=message.created_at,
                colour = discord.Colour.green()
    )
                embed.set_footer(text="Space BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736130989109280812/736134727639105577/skybot.png")
                await message.channel.send(embed=embed)
            except ValueError:
                embed = discord.Embed(title="청소 실패!", description=f"{message.author.mention}, 청소할 메시지가 정해져 있지 않아요!", timestamp=message.created_at, 
                colour=discord.Colour.orange()
    )
                embed.set_footer(text="Space BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736130989109280812/736134727639105577/skybot.png")
                await message.channel.send(embed=embed)
        else:
                embed = discord.Embed(title="청소 실패!", description=f"{message.author.mention}, 청소를 실행할 권한이 부족해요!", timestamp=message.created_at, 
                colour=discord.Colour.red()
    )
                embed.set_footer(text="Space BOT#2204", icon_url="https://cdn.discordapp.com/attachments/736130989109280812/736134727639105577/skybot.png")
                await message.channel.send(embed=embed)

    if message.content == '/업타임':
        uptime = str(Uptime.uptime()).split(":")
        hours = uptime[0]
        minitues = uptime[1]
        seconds = uptime[2].split(".")[0]
        embed = discord.Embed(title="SpaceBOT Uptime", description=f"{hours}시간 {minitues}분 {seconds}초 동안 봇이 구동중입니다!", timestamp=message.created_at, 
        colour = discord.Colour.teal()
    )
        await message.channel.send(embed=embed)

    if message.content == '/하트':
        embed = discord.Embed(title="하트를 눌러주세요!", description="[❤ 하트 누르기](https://koreanbots.dev/bots/736135672842420326)\n \n 하트는 개발자에게 큰 힘이 돼요!")
        embed.set_footer(text="하트 누르기를 누르면 [ 한국 디스코드 봇 리스트 ] 창으로 이동합니다!")
        await message.channel.send(embed=embed)

    if message.content.startswith('/이미지'):

        Text = ""
        learn = message.content.split(" ")
        vrsize = len(learn)  # 배열크기
        vrsize = int(vrsize)
        for i in range(1, vrsize):  # 띄어쓰기 한 텍스트들 인식함
            Text = Text + " " + learn[i]
        print(Text.strip())  # 입력한 명령어

        randomNum = random.randrange(0, 3) # 랜덤 이미지 숫자

        location = Text
        enc_location = urllib.parse.quote(location) # 한글을 url에 사용하게끔 형식을 바꿔줍니다. 그냥 한글로 쓰면 실행이 안됩니다.
        hdr = {'User-Agent': 'Mozilla/5.0'}
        # 크롤링 하는데 있어서 가끔씩 안되는 사이트가 있습니다.
        # 그 이유는 사이트가 접속하는 상대를 봇으로 인식하였기 때문인데
        # 이 코드는 자신이 봇이 아닌것을 증명하여 사이트에 접속이 가능해집니다!
        url = 'https://search.naver.com/search.naver?where=image&sm=tab_jum&query=' + enc_location # 이미지 검색링크+검색할 키워드
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser") # 전체 html 코드를 가져옵니다.
        # print(bsObj)
        imgfind1 = bsObj.find('div', {'class': 'photo_grid _box'}) # bsjObj에서 div class : photo_grid_box 의 코드를 가져옵니다.
        # print(imgfind1)
        imgfind2 = imgfind1.findAll('a', {'class': 'thumb _thumb'}) # imgfind1 에서 모든 a태그 코드를 가져옵니다.
        imgfind3 = imgfind2[randomNum]  # 0이면 1번째사진 1이면 2번째사진 형식으로 하나의 사진 코드만 가져옵니다.
        imgfind4 = imgfind3.find('img') # imgfind3 에서 img코드만 가져옵니다.
        imgsrc = imgfind4.get('data-source') # imgfind4 에서 data-source(사진링크) 의 값만 가져옵니다.
        print(imgsrc)
        embed = discord.Embed(title="이미지 검색 결과입니다!", timestamp=message.created_at, 
            colour=discord.Colour.green()
        )
        embed.set_image(url=imgsrc) # 이미지의 링크를 지정해 이미지를 설정합니다.
        await message.channel.send(embed=embed) # 메시지를 보냅니다.

    if message.content == '/봇정보':
        user = len(client.users)
        server = len(client.guilds)
        embed = discord.Embed(title="📘ㅣSkyBOT 정보", timestamp=message.created_at,
        colour = discord.Colour.green()
    )
        embed.add_field(name="개발 언어", value="Python", inline=False)
        embed.add_field(name="개발 시작 일자", value="2020. 07. 19", inline=False)
        embed.add_field(name="서버 수", value=str(server), inline=False)
        embed.add_field(name="유저 수", value=str(user),inline=False)
        await message.channel.send(embed=embed)

    if message.content == '/낚시':
        randomlist = ['연어', '대구', '레인보우피시', '그린쿠키피시', '비튜', ' 복어', '코리', '사과', '수학익힘책', '스카이봇 코드', '테이프', '호리병', '참치', '황새치', '상어', '흰동가리', '아구']
        ran = random.randint(0, len(randomlist)-1)
        embed = discord.Embed(title=f"'{randomlist[ran]}' 를 낚았습니다!")
        embed.add_field(name="결과", value=f"{randomlist[ran]}를 낚았다!")
        await message.channel.send(embed=embed)

    if message.content == '/주사위':
        randomlist = ['1', '2', '3', '4', '5', '6']
        ran = random.randint(0, len(randomlist)-1)
        embed = discord.Embed(title=f"'{randomlist[ran]}' 가 나왔습니다!")
        embed.add_field(name="결과", value=f"{randomlist[ran]}가 나왔습니다!")
        await message.channel.send(embed=embed)


    if message.content.startswith("/날씨"):
        learn = message.content.split(" ")
        location = learn[1]
        enc_location = urllib.parse.quote(location+'날씨')
        hdr = {'User-Agent': 'Mozilla/5.0'}
        url = 'https://search.naver.com/search.naver?where=nexearch&sm=top_hty&fbm=1&ie=utf8&query=' + enc_location
        print(url)
        req = Request(url, headers=hdr)
        html = urllib.request.urlopen(req)
        bsObj = bs4.BeautifulSoup(html, "html.parser")
        todayBase = bsObj.find('div', {'class': 'main_info'})

        todayTemp1 = todayBase.find('span', {'class': 'todaytemp'})
        todayTemp = todayTemp1.text.strip()  # 온도
        print(todayTemp)

        todayValueBase = todayBase.find('ul', {'class': 'info_list'})
        todayValue2 = todayValueBase.find('p', {'class': 'cast_txt'})
        todayValue = todayValue2.text.strip()  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        print(todayValue)

        todayFeelingTemp1 = todayValueBase.find('span', {'class': 'sensible'})
        todayFeelingTemp = todayFeelingTemp1.text.strip()  # 체감온도
        print(todayFeelingTemp)

        todayMiseaMongi1 = bsObj.find('div', {'class': 'sub_info'})
        todayMiseaMongi2 = todayMiseaMongi1.find('div', {'class': 'detail_box'})
        todayMiseaMongi3 = todayMiseaMongi2.find('dd')
        todayMiseaMongi = todayMiseaMongi3.text  # 미세먼지
        print(todayMiseaMongi)

        tomorrowBase = bsObj.find('div', {'class': 'table_info weekly _weeklyWeather'})
        tomorrowTemp1 = tomorrowBase.find('li', {'class': 'date_info'})
        tomorrowTemp2 = tomorrowTemp1.find('dl')
        tomorrowTemp3 = tomorrowTemp2.find('dd')
        tomorrowTemp = tomorrowTemp3.text.strip()  # 오늘 오전,오후온도
        print(tomorrowTemp)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowMoring1 = tomorrowAreaBase.find('div', {'class': 'main_info morning_box'})
        tomorrowMoring2 = tomorrowMoring1.find('span', {'class': 'todaytemp'})
        tomorrowMoring = tomorrowMoring2.text.strip()  # 내일 오전 온도
        print(tomorrowMoring)

        tomorrowValue1 = tomorrowMoring1.find('div', {'class': 'info_data'})
        tomorrowValue = tomorrowValue1.text.strip()  # 내일 오전 날씨상태, 미세먼지 상태
        print(tomorrowValue)

        tomorrowAreaBase = bsObj.find('div', {'class': 'tomorrow_area'})
        tomorrowAllFind = tomorrowAreaBase.find_all('div', {'class': 'main_info morning_box'})
        tomorrowAfter1 = tomorrowAllFind[1]
        tomorrowAfter2 = tomorrowAfter1.find('p', {'class': 'info_temperature'})
        tomorrowAfter3 = tomorrowAfter2.find('span', {'class': 'todaytemp'})
        tomorrowAfterTemp = tomorrowAfter3.text.strip()  # 내일 오후 온도
        print(tomorrowAfterTemp)

        tomorrowAfterValue1 = tomorrowAfter1.find('div', {'class': 'info_data'})
        tomorrowAfterValue = tomorrowAfterValue1.text.strip()

        print(tomorrowAfterValue)  # 내일 오후 날씨상태,미세먼지

        embed = discord.Embed(
            title=learn[1]+ ' 날씨 정보',
            description=learn[1]+ '날씨 정보입니다.',
            colour=discord.Colour.gold()
        )
        embed.add_field(name='현재온도', value=todayTemp+'˚', inline=False)  # 현재온도
        embed.add_field(name='체감온도', value=todayFeelingTemp, inline=False)  # 체감온도
        embed.add_field(name='현재상태', value=todayValue, inline=False)  # 밝음,어제보다 ?도 높거나 낮음을 나타내줌
        embed.add_field(name='현재 미세먼지 상태', value=todayMiseaMongi, inline=False)  # 오늘 미세먼지
        embed.add_field(name='오늘 오전/오후 날씨', value=tomorrowTemp, inline=False)  # 오늘날씨 # color=discord.Color.blue()
        embed.add_field(name='**----------------------------------**',value='**----------------------------------**', inline=False)  # 구분선
        embed.add_field(name='내일 오전온도', value=tomorrowMoring+'˚', inline=False)  # 내일오전날씨
        embed.add_field(name='내일 오전날씨상태, 미세먼지 상태', value=tomorrowValue, inline=False)  # 내일오전 날씨상태
        embed.add_field(name='내일 오후온도', value=tomorrowAfterTemp + '˚', inline=False)  # 내일오후날씨
        embed.add_field(name='내일 오후날씨상태, 미세먼지 상태', value=tomorrowAfterValue, inline=False)  # 내일오후 날씨상태


        await message.channel.send(embed=embed)

    if message.content.startswith("/복권"):
        Text = ""
        number = [1, 2, 3, 4, 5, 6, 7]
        count = 0
        for i in range(0, 7):
            num = random.randrange(1, 46)
            number[i] = num
            if count >= 1:
                for i2 in range(0, i):
                    if number[i] == number[i2]:  # 만약 현재랜덤값이 이전숫자들과 값이 같다면
                        numberText = number[i]
                        print("작동 이전값 : " + str(numberText))
                        number[i] = random.randrange(1, 46)
                        numberText = number[i]
                        print("작동 현재값 : " + str(numberText))
                        if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                            numberText = number[i]
                            print("작동 이전값 : " + str(numberText))
                            number[i] = random.randrange(1, 46)
                            numberText = number[i]
                            print("작동 현재값 : " + str(numberText))
                            if number[i] == number[i2]:  # 만약 다시 생성한 랜덤값이 이전숫자들과 또 같다면
                                numberText = number[i]
                                print("작동 이전값 : " + str(numberText))
                                number[i] = random.randrange(1, 46)
                                numberText = number[i]
                                print("작동 현재값 : " + str(numberText))

            count = count + 1
            Text = Text + "  " + str(number[i])

        print(Text.strip())
        embed = discord.Embed(
            title="복권 숫자!",
            description=Text.strip(),
            colour=discord.Color.red()
        )
        await message.channel.send(embed=embed)

    if message.content.startswith(f'/봇현황'):
        if message.author.id in owner:
            embed = discord.Embed(title="SkyBOT", description=f"{len(client.guilds)}개의 서버에 있습니다. {len(client.users)}명의 이용자와 함께합니다.", color=0xe38f4e)
            value = ""
            for guild in client.guilds:
                value += f"{guild.name}\n"
            embed.add_field(name="저는 어느 서버에 있을까요?", value=value)
            await message.channel.send(f"{message.author.mention} DM으로 전송해 드렸어요!")
            await message.author.send(embed=embed)
        else:
            await message.channel.send("해당 명령어는 Owner 등급 이상만 사용 가능합니다.")

# 관리 명령어

    if message.content == '/시간':
        a = datetime.datetime.today().year
        b = datetime.datetime.today().month
        c = datetime.datetime.today().day
        d = datetime.datetime.today().hour
        e = datetime.datetime.today().minute
        f = datetime.datetime.today().second
        await message.channel.send(str(a) + "년 " + str(b) + "월 " + str(c) + "일 " + str(d) + "시 " + str(e) + "분 " + str(f) + "초에요!")

    if message.content.startswith("/eval"):
        if message.author.id in owner:
            a=message.content[6:]
            
            if message.content in ['output','token', 'file=', 'os', 'logout', 'login', 'quit', 'exit', 'sys', 'shell', 'dir']:
                embed=discord.Embed(colour=0x85CFFF, timestamp=message.created_at)
                embed.add_field(name="Error!", value=f'{message.content} 그 명령어는 금지된 단어가 포함되어있습니다.', inline=True)
                embed.set_footer(text=f"{message.author}, 인증됨", icon_url=message.author.avatar_url)
                await message.channel.send(embed=embed)
                return None

            try:
                msg=await message.channel.send(embed=discord.Embed(color=0x85CFFF, title="evaling...",description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    evaling...
    ```"""))
                aa=await eval(a)
            except Exception as e:
                await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
                        
    ```py
    {a}          
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
                try:
                    aa = eval(a)
                except Exception as e:
                    await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
                        
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {e}
    ```"""))
                else:
                    await msg.edit(embed=discord.Embed(color=0x85CFFF, title=f"eval",description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```""")) 
            else:
                await msg.edit(embed=discord.Embed(color=0x85CFFF, title="eval",description=f"""📥INPUT📥
    ```py
    {a}
    ```
    📤OUTPUT📤
    ```py
    {aa}
    ```"""))
        else:
            await message.channel.send("권한없음")

client.run('NzM2MTM1NjcyODQyNDIwMzI2.XxqZxQ.NRqfu427toGKALzJxTnlw8NqcJU')