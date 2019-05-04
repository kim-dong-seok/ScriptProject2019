import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter as tk

data=requests.get("https://api.bf4stats.com/api/playerInfo?plat=pc&name=sharqia&output=json").json() #서버에 GET 요청
print(data)
print(data.keys())
data2=requests.get("https://api.bf4stats.com/api/playerRankings?plat=pc&name=sharqia&output=json").json()
print(data2)
rankings=data2["rankings"]
print(rankings)
state=data['stats']
player=data['player']
print(player.keys())
print(state.keys())
rank=state['rank']
dogtags=data['dogtags']
weapons=data['weapons']
weaponCategory=data['weaponCategory']
kititems=data['kititems']
vehicles=data['vehicles']
vehicleCategory=data['vehicleCategory']
awards=data['awards']
assignments=data['assignments']
upcomingUnlocks=data['upcomingUnlocks']
print(str(round(state['kills']/(player['timePlayed']/60),2)))
print(player['score'])



class App1:
    def __init__(self):
        self.window = Tk()
        self.window.title("전장4")
        self.originimage1=Image.open("image/ranks/r140.png").resize((100,100))
        self.rankImage=ImageTk.PhotoImage(self.originimage1)
        self.width = 500
        self.height = 300
        self.canvas = Canvas(self.window, width=self.width, height=self.height,bd=0)
        self.canvas.pack()
        #Label(canvas,text="name="+player['name']).pack()
        #Label(canvas,text="level="+str(rank)).pack()
        #Label(canvas,text="skill="+str(state['skill'])).pack()
        #Label(canvas,text="kills="+str(state['kills'])).pack()
        #Label(canvas,text="deaths="+str(state['deaths'])).pack()
        self.canvas.create_image(50,50, image=self.rankImage)
        self.window.mainloop()

class App2:
    def __init__(self, window, window_title):
        self.window = window
        self.window.title(window_title)
        self.originimage1 = Image.open("image/ranks/r140.png")
        self.orlginOpacity = Image.open("opacity.png")
        self.originBgImage = Image.open("bg.jpg")
        self.rankImage = ImageTk.PhotoImage(self.originimage1.resize((100, 100)))
        self.opacityImage = ImageTk.PhotoImage(self.orlginOpacity.resize((600, 500)))
        self.menuImage = ImageTk.PhotoImage(self.orlginOpacity.resize((200, 30)))
        self.bgImage = ImageTk.PhotoImage(self.originBgImage.resize((800, 600)))
        self.canvas = Canvas(window, width = 800, height = 600)
        self.canvas.pack()
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()

        self.window.mainloop()

    def update(self):

        self.canvas.create_image(0, 0, image = self.bgImage, anchor = NW)
        self.canvas.create_image(400, 300, image=self.opacityImage)
        self.canvas.create_image(200, 65, image=self.menuImage)
        self.canvas.create_text(120, 65, text="계급", font=("",12,"bold"), fill="ghost white")
        self.canvas.create_image(400, 65, image=self.menuImage)
        self.canvas.create_text(320, 65, text="스킬", font=("",12,"bold"), fill="ghost white")
        self.canvas.create_image(200, 150, image=self.rankImage)
        self.canvas.create_text(400, 110, text=str(state['skill']), font=("", 30,"bold"), fill="ghost white")
        self.canvas.create_text(335, 140, text="K/D", font=("", 10, "bold"), fill="grey")
        self.canvas.create_text(335, 160, text=str(round(state['kills']/state['deaths'],2)), font=("", 15, "bold"), fill="ghost white")
        self.canvas.create_text(400, 140, text="분당 점수", font=("", 10, "bold"), fill="grey")
        self.canvas.create_text(400, 160, text=str(int(player['score'] / (player['timePlayed']/60))),
                                    font=("", 15, "bold"), fill="ghost white")
        self.canvas.create_text(465, 140, text="분당 사살", font=("", 10, "bold"), fill="grey")
        self.canvas.create_text(465, 160, text=str(round(state['kills'] / (player['timePlayed'] / 60),2)),
                                    font=("", 15, "bold"), fill="ghost white")
        self.canvas.create_text(335, 190, text="사살", font=("", 10, "bold"), fill="grey")
        self.canvas.create_text(335, 210, text=str(state['kills']),
                                    font=("", 8, "bold"), fill="ghost white")
        self.canvas.create_text(400, 190, text="점수", font=("", 10, "bold"), fill="grey")
        self.canvas.create_text(400, 210, text=format(player['score'],','),
                                    font=("", 8, "bold"), fill="ghost white")
        self.canvas.create_text(465, 190, text="시간", font=("", 10, "bold"), fill="grey")
        self.canvas.create_text(465, 210, text=str(int((player['timePlayed']/60)/60))+"시간 "+str(int((player['timePlayed']/60)%60))+"분",
                                    font=("", 8, "bold"), fill="ghost white")
        self.canvas.create_text(125,205,text="대장",font=("", 8, "bold"),fill="grey")




# Create a window and pass it to the Application object
App2(Tk(), "Tkinter and OpenCV")