#!/usr/bin/python
# coding=utf-8


import time
import telepot
from pprint import pprint
from datetime import date, datetime
import bf4_noti

def playerInfoData(data1,data2,data3,data4, user):
    print(user, data1)
    res_list = bf4_noti.getPlayerInfoData( data2,data3,data4)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>bf4_noti.MAX_MSG_LENGTH:
            bf4_noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        bf4_noti.sendMessage( user, msg )
def playerRankingsData(data1,data2,data3,data4, user):
    print(user, data1)
    res_list = bf4_noti.getPlayerRankingsData( data2,data3,data4)
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>bf4_noti.MAX_MSG_LENGTH:
            bf4_noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        bf4_noti.sendMessage( user, msg )
def onlinePlayersData(date_param, user ):
    print(user, date_param)
    res_list = bf4_noti.getOnlinePlayersData( )
    msg = ''
    for r in res_list:
        print( str(datetime.now()).split('.')[0], r )
        if len(r+msg)+1>bf4_noti.MAX_MSG_LENGTH:
            bf4_noti.sendMessage( user, msg )
            msg = r+'\n'
        else:
            msg += r+'\n'
    if msg:
        bf4_noti.sendMessage( user, msg )



def handle(msg):
    content_type, chat_type, chat_id = telepot.glance(msg)
    if content_type != 'text':
        bf4_noti.sendMessage(chat_id, '난 텍스트 이외의 메시지는 처리하지 못해요.')
        return

    text = msg['text']
    args = text.split(' ')
    if text.startswith('?'):
        bf4_noti.sendMessage(chat_id, '명령어 도움말\n현재 접속자 수 - [onlinePlayers]\n'
                                  '플레이어 정보 검색 - [playerInfo] [platform] [playerName] [key값]\n'
                                  '(key 값-player, stats, weapons,  weaponCategory, vehicles ,vehicleCategory)\n'
                                  ' 플레이어 랭킹 검색-[playerRankings] [platform] [playerName] [key값]\n'
                                  '(key 값-player, stats, weapons,  weaponCategory, vehicles ,vehicleCategory)\n'
                                  '중 하나의 명령을 입력하세요.')
    elif text.startswith('onlinePlayers') and len(args) > 0:
        print('try to onlinePlayers')
        onlinePlayersData( chat_id)
    elif text.startswith('playerInfo') and len(args) > 3:
        print('try to playerInfo')
        playerInfoData(args[0],args[1],args[2],args[3], chat_id)
    elif text.startswith('playerRankings') and len(args) > 3:
        print('try to playerRankings')
        playerRankingsData(args[0],args[1],args[2],args[3], chat_id)
    else:
        bf4_noti.sendMessage(chat_id, '모르는 명령어입니다.\n현재 접속자 수 - [onlinePlayers]\n'
                                  '플레이어 정보 검색 - [playerInfo] [platform] [playerName] [key값]\n'
                                  '(key 값-player, stats, weapons,  weaponCategory, vehicles ,vehicleCategory)\n'
                                  ' 플레이어 랭킹 검색-[playerRankings] [platform] [playerName] [key값]\n'
                                  '(key 값-player, kit,mode,  weapon, vehicles ,ribbon,kititem)\n'
                                  '중 하나의 명령을 입력하세요.')


today = date.today()
current_month = today.strftime('%Y%m')

print( '[',today,']received token :', bf4_noti.TOKEN )

bot = telepot.Bot(bf4_noti.TOKEN)
pprint( bot.getMe() )

bot.message_loop(handle)

print('Listening...')

while 1:
  time.sleep(10)