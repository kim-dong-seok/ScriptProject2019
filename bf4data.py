import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter.ttk

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
print("플레이어")
print(player.keys())
print("통계")
print(stats.keys())
print("인식표")
print(dogtags.keys())


print("upcomingUnlocks")
print(upcomingUnlocks[0])