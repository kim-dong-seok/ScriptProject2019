import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter.ttk
from operator import  itemgetter

online=requests.get("https://api.bf4stats.com/api/onlinePlayers?output=json").json()
player_name="sharqia"
player_plat="pc"
player_data=requests.get("https://api.bf4stats.com/api/playerInfo?plat="+player_plat+"&name="+player_name+"&output=json").json()

print(player_data.keys())
player=player_data["player"]
stats=player_data["stats"]
dogtags=player_data["dogtags"]
weapons=player_data["weapons"]
weaponCategory=player_data["weaponCategory"]
kititems=player_data["kititems"]
vehicles=player_data["vehicles"]
vehicleCategory=player_data["vehicleCategory"]
awards=player_data["awards"]
assignments=player_data["assignments"]
upcomingUnlocks=player_data["upcomingUnlocks"]
kits=stats["kits"]
print("플레이어")
print(player.keys())
print("통계")
print(stats.keys())
print("인식표")
print(dogtags.keys())
#Assault = 155.000
#Engineer = 131.000
#Support = 134.000
#Recon = 104.000
#Commander = 20.000

#정복21.000
#러쉬15.000
#데스매치6.000
#지배19.500
#Obliteration ???    (폭탄 배달은 러쉬 서비스 스타에 추가됨)
#해체6.000(폭탄배달이러쉬서비스스타에추가됨)
#깃발7.500
#공기우위12.000
#CarrierAssault22.000
#체인링크10.000

print("upcomingUnlocks")

print(kits.keys())

