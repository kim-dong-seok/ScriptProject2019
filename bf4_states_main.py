import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter.ttk
from bs4 import  BeautifulSoup
import urllib.request








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
print(stats["kits"])
print("인식표")
print(dogtags.keys())
print(player_data["assignments"])


class player_main:
    def __init__(self):
        self.skill=0
        self.origin_level_image = Image.open("image/ranks/r140.png").resize((120, 120))
        self.level_image = ImageTk.PhotoImage(self.origin_level_image)
        self.origin_contents_opacity = Image.open("내용배경.png")
        self.contents_opacity = ImageTk.PhotoImage(self.origin_contents_opacity .resize((331, 215)))
        self.contents_opacity_1 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((331, 93)))
        self.contents_opacity_2 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((109, 60)))

        self.contents_opacity2 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((331, 170)))
        self.contents_opacity2_1 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((331, 114)))
        self.contents_opacity2_2 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((331, 55)))

        self.contents_opacity2_3 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((240, 170)))
        self.contents_opacity2_4 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((90, 84)))

        self.contents_opacity3 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((331, 140)))
        self.contents_opacity3_1 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((250, 140)))
        self.contents_opacity3_2 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((80, 69)))
        self.orlgin_menu_bg = Image.open("메뉴배경.png")
        self.menu_bg = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((331, 25)))

    def update(self):
        if self.skill<stats["skill"]:
            self.skill+=10
        else:
            self.skill=stats["skill"]
    def draw(self,canvas):

        for j in range(3):
            canvas.create_image(300+(j*332), 214, image=self.menu_bg, anchor="nw", tag="grim")
        for j in range(3):
            canvas.create_image(300+(j*332), 456, image=self.menu_bg, anchor="nw", tag="grim")
        for j in range(3):
            canvas.create_image(300 + (j * 332), 677, image=self.menu_bg, anchor="nw", tag="grim")

        canvas.create_text(310, 218, text="계급", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(300, 240, image=self.contents_opacity, anchor="nw", tag="grim")
        canvas.create_image(465, 320, image=self.level_image, tag="grim")
        canvas.create_text(642, 218, text="스킬", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(632, 240, image=self.contents_opacity_1, anchor="nw", tag="grim")
        canvas.create_text(797, 275, text=str(self.skill), font=("", 40, "bold"), fill="ghost white", tag="grim")
        canvas.create_image(632, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(687, 350, text="K/D", font=("", 10, "bold"),fill="gray", tag="grim")
        canvas.create_text(687, 375, text=str(round(stats['kills']/stats['deaths'],2)), font=("", 18, "bold"), fill="ghost white", tag="grim")
        canvas.create_image(743, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(798, 350, text="분당 점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 375, text=str(int(player['score'] / (player['timePlayed']/60))), font=("", 18, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(854, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(909, 350, text="분당 사살", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(909, 375, text=str(round(stats['kills'] / (player['timePlayed'] / 60),2)), font=("", 18, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(632, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(687, 410, text="사살", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(687, 435, text=str(stats['kills']), font=("", 12, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(743, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(798, 410, text="점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 435, text=format(player['score'],','), font=("", 12, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(854, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(909, 410, text="시간", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(909, 435, text=str(int((player['timePlayed']/60)/60))+"시간 "+str(int((player['timePlayed']/60)%60))+"분", font=("", 12, "bold"),fill="ghost white", tag="grim")
        canvas.create_text(974, 218, text="인식표", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(964, 240, image=self.contents_opacity, anchor="nw", tag="grim")

        canvas.create_text(310, 460, text="공로 스타", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(300, 482, image=self.contents_opacity2, anchor="nw", tag="grim")
        canvas.create_text(642, 460, text="팀플레이", font=("", 12, "bold"), anchor="nw",fill="ghost white", tag="grim")
        canvas.create_image(632, 482, image=self.contents_opacity2_1, anchor="nw", tag="grim")
        canvas.create_image(632, 597, image=self.contents_opacity2_2, anchor="nw", tag="grim")
        canvas.create_text(974, 460, text="최고 순위표", font=("", 12, "bold"), anchor="nw",fill="ghost white", tag="grim")
        canvas.create_image(964, 482, image=self.contents_opacity2_3, anchor="nw", tag="grim")
        canvas.create_image(1205, 482, image=self.contents_opacity2_4, anchor="nw", tag="grim")
        canvas.create_image(1205, 568, image=self.contents_opacity2_4, anchor="nw", tag="grim")

        canvas.create_text(310, 681, text="최고 무기", font=("", 12, "bold"), anchor="nw",fill="ghost white", tag="grim")
        canvas.create_image(300, 703, image=self.contents_opacity3_1, anchor="nw", tag="grim")
        canvas.create_image(551, 703, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(551, 774, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_text(642, 681, text="최고 탑승장비", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(632, 703, image=self.contents_opacity3_1, anchor="nw", tag="grim")
        canvas.create_image(883, 703, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(883, 774, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_text(974, 681, text="최고 게임 모드", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(964, 703, image=self.contents_opacity3, anchor="nw", tag="grim")

class bf4_main:
    def __init__(self):
        self.window = Tk()
        self.window.title("bf4.gg")
        self.video_source = "bg-video.mp4"
        self.vid = MyVideoCapture(self.video_source)
        self.width=1600
        self.height=900
        self.x=0
        self.y=0
        self.b1ck=0
        self.bcheck=-1
        self.canvas = Canvas(self.window,  width=self.width, height=self.height)
        self.canvas.pack()
        self.orlgin_bgimage = Image.open("bg.jpg")
        self.bgimage= ImageTk.PhotoImage(self.orlgin_bgimage.resize(( self.width, self.height)))
        self.originimage2 = Image.open("bf4.gg.png").resize((160, 32))
        self.logoImage = ImageTk.PhotoImage(self.originimage2)
        #self.orlginOpacity = Image.open("opacity.png")
        #self.opacityImage = ImageTk.PhotoImage(self.orlginOpacity.resize((1000, 700)))
        self.orlgin_logo_bg=Image.open("로고배경.png")
        self.logo_bg = ImageTk.PhotoImage(self.orlgin_logo_bg.resize((1600, 45)))
        self.orlgin_search_bg = Image.open("검색배경.png")
        self.search_bg = ImageTk.PhotoImage(self.orlgin_search_bg.resize((1600, 45)))
        self.orlgin_name_bg = Image.open("내용배경.png")
        self.name_bg = ImageTk.PhotoImage(self.orlgin_name_bg.resize((350, 45)))

        self.menu_buttons = [menu_button(300+(i*166),165) for i in range(6)]
        self.menu_buttons[0].btext="개요"
        self.menu_buttons[1].btext ="통계"
        self.menu_buttons[2].btext = "잠김 해제"
        self.menu_buttons[3].btext = "로드아웃"
        self.menu_buttons[4].btext = "과제"
        self.menu_buttons[5].btext = "포상"
        self.player_main=player_main()

        self.e1 = Entry(self.canvas, font=("", 13,) , width=25)
        self.e1.insert(0, "Player name")
        self.e1.place(x=self.width / 17*5, y=self.height / 16)
        self.values = ["PC", "PS4", "XONE", "PS3", "XBOX"]
        self.c1 = tkinter.ttk.Combobox(self.canvas, values=self.values, width=9, font=("", 12))
        self.c1.set("플랫폼")
        self.c1.place(x=self.width / 31*7, y=self.height / 16)
        self.b1 = Button(self.canvas, text="검색", font=("", 10), command=self.search, bg="black",
                         width=6, height=1)
        self.b1.place(x=self.width / 2, y=self.height / 16)

        self.window.bind('<Motion>', self.motion)
        self.delay = 15
        self.update()
        self.window.mainloop()
    def search(self):
        pass
    def click(self,event):
        if self.menu_buttons[self.bcheck].ckeck==1:
            for i in range(6):
                if self.menu_buttons[i].ckeck == 2:
                    self.menu_buttons[i].ckeck = 0
            self.menu_buttons[self.bcheck].ckeck = 2


    def motion(self,event):
        self.x,self.y=event.x,event.y
        self.mause_update()
    def mause_update(self):
        for i in range(6):
            if self.menu_buttons[i].ckeck == 1:
                self.bcheck = i
                self.window.bind('<Button-1>', self.click)
            self.menu_buttons[i].update(self.x, self.y)
    def update(self):
        ret, frame = self.vid.get_frame()

        if ret:
            self.canvas.delete("grim")
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame).resize((1920, 1080)))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW,tag="grim")

            self.player_main.update()
            self.draw()
        self.window.after(self.delay, self.update)
    def draw(self):
        #self.canvas.create_image( self.width/2, self.height/2, image=self.bgimage,tag="grim")
        #self.canvas.create_image( 300, 265, image=self.opacityImage,anchor="nw",tag="grim")
        self.canvas.create_image(self.width / 2,self.height/40 , image=self.logo_bg,tag="grim")
        self.canvas.create_image(self.width / 2, self.height / 13, image=self.search_bg,tag="grim")
        self.canvas.create_image(300, 10, image=self.logoImage,anchor="nw",tag="grim")
        self.canvas.create_image(300, 108, image=self.name_bg,anchor="nw",tag="grim")
        self.canvas.create_text(320,115, text=player["plat"].upper(),
                                font=("", 20,"bold"), fill="ghost white", tag="grim",anchor="nw")
        self.canvas.create_text(420,115, text="["+player["tag"]+"]",
                                font=("", 20, "bold"), fill="ghost white", tag="grim",anchor="nw")
        self.canvas.create_text(510,115, text=player["name"],
                                font=("", 20, "bold"), fill="ghost white", tag="grim",anchor="nw")
        for menu_button in self.menu_buttons:
            menu_button.draw(self.canvas)
        self.player_main.draw(self.canvas)


class menu_button:
    orlgin_menu_bg=None
    orlgin_gradient_bg = None
    orlgin_click__bg = None
    def __init__(self,bx=0,by=0,btext=" "):
        self.ckeck = 0
        self.bx = bx
        self.by = by
        self.btext=btext

        if menu_button.orlgin_menu_bg==None:
            self.orlgin_menu_bg = Image.open("메뉴배경.png")
        self.menu_bg = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((165, 35)))
        if menu_button.orlgin_gradient_bg == None:
            self.orlgin_gradient_bg = Image.open("그라데이션.png")
        self.gradient_bg = ImageTk.PhotoImage(self.orlgin_gradient_bg.resize((165, 35)))
        if menu_button.orlgin_click__bg == None:
            self.orlgin_click_bg = Image.open("클릭시.png")
        self.click_bg = ImageTk.PhotoImage(self.orlgin_click_bg.resize((165, 35)))

    def update(self,x,y):

        if x > self.bx and x < self.bx+165 and y > self.by and y < self.by+35:
            if self.ckeck != 2:
                self.ckeck = 1
        else:
            if self.ckeck != 2:
                self.ckeck=0

    def draw(self,canvas):
        if self.ckeck==0:
            canvas.create_image(self.bx, self.by, image=self.menu_bg, anchor="nw",tag="grim")
            canvas.create_text(self.bx+82,self.by+18, text=self.btext, font=("", 14, "bold"), fill="ghost white", tag="grim")
        if self.ckeck==1:
            canvas.create_image(self.bx, self.by, image=self.gradient_bg, anchor="nw",tag="grim")
            canvas.create_text(self.bx+82,self.by+18, text=self.btext, font=("", 14, "bold"), fill="ghost white", tag="grim")
        if self.ckeck==2:
            canvas.create_image(self.bx, self.by, image=self.click_bg, anchor="nw",tag="grim")
            canvas.create_text(self.bx+82,self.by+18, text=self.btext, font=("", 14, "bold"), fill="black", tag="grim")

class MyVideoCapture:
    def __init__(self, video_source=0):
        # Open the video source
        self.vid = cv2.VideoCapture(video_source)
        self.frame_counter = 0
        if not self.vid.isOpened():
            raise ValueError("Unable to open video source", video_source)

        # Get video source width and height
        self.width = self.vid.get(cv2.CAP_PROP_FRAME_WIDTH)
        self.height = self.vid.get(cv2.CAP_PROP_FRAME_HEIGHT)

    def get_frame(self):
        if self.vid.isOpened():
            self.ret, frame = self.vid.read()
            self.frame_counter += 1
            # If the last frame is reached, reset the capture and the frame_counter
            if self.frame_counter == self.vid.get(cv2.CAP_PROP_FRAME_COUNT):
                self.frame_counter = 0  # Or whatever as long as it is the same as next line
                self.vid.set(cv2.CAP_PROP_POS_FRAMES, 0)
            if self.ret:
                # Return a boolean success flag and the current frame converted to BGR
                return (self.ret, cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
            else:
                return (self.ret, None)
        else:
            return (self.ret, None)

    # Release the video source when the object is destroyed
    def __del__(self):
        if self.vid.isOpened():
            self.vid.release()
bf4=bf4_main()

