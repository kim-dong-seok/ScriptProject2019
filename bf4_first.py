import requests
from tkinter import *
from PIL import Image, ImageTk


class start_page():
    def __init__(self):
        self.originimage2 = Image.open("ui_image/bf4.gg.png")
        self.Big_logoImage = ImageTk.PhotoImage(self.originimage2.resize((600, 120)))
        self.orlginOpacity = Image.open("ui_image/opacity.png")
        self.opacityImage = ImageTk.PhotoImage(self.orlginOpacity.resize((600, 300)))
        online = requests.get("https://api.bf4stats.com/api/onlinePlayers?output=json").json()
        self.online_players = [online["pc"], online["ps4"], online["xone"], online["ps3"], online["xbox"]]
        self.total_players = 0
        for i in range(5):
            self.total_players += self.online_players[i]["count"]

    def draw(self,canvas):
        canvas.create_image(800, 600, image=self.opacityImage, tag="grim")
        canvas.create_image(800, 280, image=self.Big_logoImage, tag="grim")
        canvas.create_text(800, 510, text="현재 온라인 플레이어(총" + str(self.total_players) + "명)", font=("", 16),
                                fill="white smoke", tag="grim")
        for i in range(5):
            canvas.create_text(600 + (100 * i), 555, text=self.online_players[i]["label"], font=("", 16),
                                    fill="white smoke", tag="grim")
            canvas.create_text(600 + (100 * i), 600, text=self.online_players[i]["count"], font=("", 19, "bold"),
                                    fill="white smoke", tag="grim")
            canvas.create_text(600 + (100 * i), 645, text="최다 접속", font=("", 14), fill="white smoke", tag="grim")
            canvas.create_text(600 + (100 * i), 675, text=self.online_players[i]["peak24"], font=("", 16),
                                    fill="white smoke", tag="grim")

