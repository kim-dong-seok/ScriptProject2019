import requests
from tkinter import *

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
width = 500
height = 300
canvas = Canvas(window, width=width, height=height)
canvas.pack()
Label(canvas,text="name="+player['name']).pack()
Label(canvas,text="level="+str(rank)).pack()
Label(canvas,text="skill="+str(state['skill'])).pack()
Label(canvas,text="kills="+str(state['kills'])).pack()
Label(canvas,text="deaths="+str(state['deaths'])).pack()

window.mainloop()