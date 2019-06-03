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
import requests

TOKEN = '861927235:AAFOOzJm5q0p15mdFQ3w649xZn5hcIDyMjU'
MAX_MSG_LENGTH = 300
baseurl = 'https://api.bf4stats.com/api/'
bot = telepot.Bot(TOKEN)
def getOnlinePlayersData( date_param):
    res_list = []
    url = baseurl+date_param+"?output=json"
    data=requests.get(url).json()
    for i in data:
        row = "플랫폼["+data[i]["label"]+"]  현재 접속자 수 "+str(data[i]["count"])+"명\n최근 하루 최고 접속자 수 "+str(data[i]["peak24"])+"명"

        if row:
            res_list.append(row)
    return res_list
def getPlayerInfoData( data1,data2,data3,data4):
    res_list = []
    url = baseurl+data1+"?plat="+data3+"&name="+data2+"&opt="+data4+"&output=json"
    originData=requests.get(url).json()
    data=originData[data4]
    if data4=="player":
        row = "이름: {0}\n태그: {1}\n레벨: {2}\n점수: {3:,}\n플레이타임: ".format(data["name"],data["tag"],data["rank"]["nr"],data["score"])+str(int((data['timePlayed'] / 60) / 60)) + "시간 " + str(int((data['timePlayed'] / 60) % 60)) + "분"
    elif data4=="stats":
        row = "스킬: {0:,}\n사살: {1:,}\n사망: {2:,}\n사살 도움: {3:,}\n발사: {4:,}\n명중: {5:,}\n제압 도움: {6:,}" \
              "\n보복 사살: {7:,}\n구원: {8:,}\n치료: {9:,}\n소생: {10:,}\n보급: {11:,}\n수리: {12:,}\n장비 파괴: {13:,}" \
              "\n장비 피해: {14:,}\n헤드샷: {15:,}\n최장거리 헤드샷: {16:,}\n최고 연속 사살: {17:,}\n전투: {18:,}" \
              "\n승리: {19:,}\n패배: {20:,}".format(data["skill"], data["kills"], data["deaths"],data["killAssists"],
                                                data["shotsFired"],data["shotsHit"],data["suppressionAssists"],
                                                data["avengerKills"],data["saviorKills"],data["heals"], data["revives"],
                                                data["resupplies"],data["repairs"],data["vehiclesDestroyed"],
                                                data["vehicleDamage"], data["headshots"],data["longestHeadshot"],
                                                data["killStreakBonus"],data["numRounds"],data["numWins"],data["numLosses"])

    if row:
        res_list.append(row)
    return res_list

def sendMessage(user, msg):
    try:
        bot.sendMessage(user, msg)
    except:
        traceback.print_exc(file=sys.stdout)



if __name__=='__main__':
    today = date.today()
    current_month = today.strftime('%Y%m')

    print( '[',today,']received token :', TOKEN )

    pprint( bot.getMe() )

    run(current_month)
