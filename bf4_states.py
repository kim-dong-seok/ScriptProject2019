import requests
from tkinter import *
from PIL import Image, ImageTk
import os

data=requests.get("https://api.bf4stats.com/api/playerInfo?plat=pc&name=sharqia&output=json").json() #서버에 GET 요청
print(data)
print(data.keys())
state=data['stats']
player=data['player']
print(player.keys())
print(state.keys())
rank=state['rank']
print(rank)

window = Tk()
window.title("전장4")
originimage1=Image.open("image/ranks/r140.png").resize((100,100))
rankImage=ImageTk.PhotoImage(originimage1)
width = 500
height = 300
canvas = Canvas(window, width=width, height=height)
canvas.pack()
Label(canvas,text="name="+player['name']).pack()
Label(window, image=rankImage).pack()
Label(canvas,text="level="+str(rank)).pack()
Label(canvas,text="skill="+str(state['skill'])).pack()
Label(canvas,text="kills="+str(state['kills'])).pack()
Label(canvas,text="deaths="+str(state['deaths'])).pack()
os.system("D:/GitHub/ScriptProject2019/bg-video.webm")

window.mainloop()