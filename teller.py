#!/usr/bin/python
# coding=utf-8

import sys
import time
import sqlite3
import telepot
from pprint import pprint
from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
from datetime import date, datetime, timedelta
import traceback

import noti

def playerInfoData(data1,data2,data3,data4, user):
    print(user, data1)
    res_list = noti.getPlayerInfoData( data1,data2,data3,data4)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )
    else:
        noti.sendMessage( user, '아이디가 없거나 정보가 없습니다.'%data1 )

def onlinePlayersData(date_param, user ):
    print(user, date_param)
    res_list = noti.getOnlinePlayersData( date_param )
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>noti.MAX_MSG_LENGTH:
            noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        noti.sendMessage( user, msg )



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if text.startswith('?'):
        noti.sendMessage(chat_id,
                         '명령어 도움말\n현재 접속자 수-[onlinePlayers], 플레이어 정보 검색-[playerInfo] [playerName] [platform], 플레이어 랭킹 검색-[playerRankings] [playerName] [platform] 중 하나의 명령을 입력하세요.')
    elif text.startswith('onlinePlayers') and len(args) > 0:
        print('try to onlinePlayers')
        onlinePlayersData(args[0], chat_id)
    elif text.startswith('playerInfo') and len(args) > 3:
        print('try to playerInfo')
        playerInfoData(args[0],args[1],args[2],args[3], chat_id)
    else:
        noti.sendMessage(chat_id, '모르는 명령어입니다.\n현재 접속자 수 - [onlinePlayers]\n'
                                  '플레이어 정보 검색 - [playerInfo] [playerName] [platform] [key값]\n'
                                  '(key 값-player, stats, dogtags, weapons, weaponCategory, kititems, vehicles, vehicleCategory'
                                  ' 플레이어 랭킹 검색-[playerRankings] [playerName] [platform] \n'
                                  '중 하나의 명령을 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', noti.TOKEN )

bot = telepot.Bot(noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)