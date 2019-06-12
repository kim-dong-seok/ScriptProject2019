from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk


class Vehicle_page:
    def __init__(self,player_data):
        self.mx=0
        self.my=0
        self.s=0
        self.m=0
        self.h=0
        self.sort_count=1
        self.mcount=0
        self.mouse_count = 0
        self.count=0
        self.sort_vehicle= player_data.vehicles
        self.sort_kill= player_data.rank_vehicles
        self.menu_kans=[0,81,452,633,814]
        self.menu_cantents=["# ▼","탑승장비","사살","분당 사살","차량 파괴"]
        self.origin_contents_opacity = Image.open("ui_image/내용배경.png")
        self.contents_opacity1 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((80, 80)))
        self.contents_opacity2 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((370, 80)))
        self.contents_opacity3 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((180, 80)))
        self.orlgin_menu_bg = Image.open("ui_image/메뉴배경.png")
        self.menu_bg1 = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((80, 20)))
        self.menu_bg2= ImageTk.PhotoImage(self.orlgin_menu_bg.resize((370, 20)))
        self.menu_bg3= ImageTk.PhotoImage(self.orlgin_menu_bg.resize((180, 20)))
        self.orlgin_star = Image.open("bf4/stars/star.png")
        self.star_image = ImageTk.PhotoImage(self.orlgin_star.resize((20, 20)))
        self.origin_vehicle_image=[0]*7
        self.vehicle_image=[0]*7
        for i in range(7):
            self.origin_vehicle_image[i]=Image.open("bf4/vehicles_lineart/"+self.sort_kill[i+self.count]["name"]+".png").resize((192, 48))
            self.vehicle_image[i]= ImageTk.PhotoImage(self.origin_vehicle_image[i])
    def mouse_check(self):
        if 300  < self.mx and 300  + 80 > self.mx and \
                214 < self.my and 234 > self.my:
            self.mouse_count = 1
            self.mcount += 1
        if 300 + self.menu_kans[1] < self.mx and 300 + self.menu_kans[1] + 370 > self.mx and \
                214 < self.my and 234 > self.my:
            self.mouse_count = 2
            self.mcount += 1
        for i in range(2,5):
            if 300 + self.menu_kans[i] < self.mx and  300 + self.menu_kans[i]+180 > self.mx and \
                    214 <self.my and 234>self.my:
                self.mouse_count=i+1
                self.mcount+=1
        if self.mcount==0:
            self.mouse_count=0
        self.mcount=0
    def sort(self,event):
            if self.mouse_count==1:
                if self.sort_count==self.mouse_count:
                    self.sort_kill= sorted(self.sort_vehicle, key=lambda t: t["stat"]["kills"], reverse=False)
                    self.sort_count = 0
                else:
                    self.sort_kill = sorted(self.sort_vehicle, key=lambda t: t["stat"]["kills"], reverse=True)
                    self.sort_count = 1
            elif self.mouse_count==2:
                if self.sort_count==self.mouse_count:
                    self.sort_kill= sorted(self.sort_vehicle, key=lambda t: t["name"], reverse=False)
                    self.sort_count = 0
                else:
                    self.sort_kill = sorted(self.sort_vehicle, key=lambda t: t["name"], reverse=True)
                    self.sort_count = 2
            elif self.mouse_count==3:
                if self.sort_count==self.mouse_count:
                    self.sort_kill= sorted(self.sort_vehicle, key=lambda t: t["stat"]["kills"], reverse=False)
                    self.sort_count = 0
                else:
                    self.sort_kill = sorted(self.sort_vehicle, key=lambda t: t["stat"]["kills"], reverse=True)
                    self.sort_count = 3
            elif self.mouse_count==4:
                if self.sort_count==self.mouse_count:
                    self.sort_kill= sorted(self.sort_vehicle, key=lambda t: t["extra"]["kpm"], reverse=False)
                    self.sort_count = 0
                else:
                    self.sort_kill = sorted(self.sort_vehicle, key=lambda t: t["extra"]["kpm"], reverse=True)
                    self.sort_count = 4
            elif self.mouse_count==5:
                if self.sort_count==self.mouse_count:
                    self.sort_kill= sorted(self.sort_vehicle, key=lambda t: t["stat"]["destroys"], reverse=False)
                    self.sort_count = 0
                else:
                    self.sort_kill = sorted(self.sort_vehicle, key=lambda t: t["stat"]["destroys"], reverse=True)
                    self.sort_count = 5

    def update(self, mx, my):
        self.mx = mx
        self.my = my
        self.mouse_check()
        for i in range(7):
            self.origin_vehicle_image[i]=Image.open("bf4/vehicles_lineart/"+self.sort_kill[i+self.count]["name"]+".png").resize((192, 48))
            self.vehicle_image[i]= ImageTk.PhotoImage(self.origin_vehicle_image[i])
    def draw(self,canvas):
        canvas.create_image(300, 214, image=self.menu_bg1, anchor="nw", tag="grim")
        canvas.create_text(340, 224, text= self.menu_cantents[0], font=("", 9, "bold"), fill="white smoke", tag="grim")
        canvas.create_image(300+ self.menu_kans[1], 214, image=self.menu_bg2, anchor="nw", tag="grim")
        canvas.create_text(320+self.menu_kans[1], 217, text=self.menu_cantents[1], font=("", 9, "bold"), anchor="nw", fill="white smoke",
                           tag="grim")
        for i in range(2,5):
            canvas.create_image(300 + self.menu_kans[i], 214, image=self.menu_bg3, anchor="nw", tag="grim")
            canvas.create_text(390 + self.menu_kans[i], 224, text=self.menu_cantents[i], font=("", 9, "bold"),
                           fill="white smoke", tag="grim")
        for i in range(self.count,7+self.count):

            canvas.create_image(300, 235+((i-self.count)*81), image=self.contents_opacity1, anchor="nw", tag="grim")
            canvas.create_text(340 , 275+((i-self.count)*81), text=str(i+1), font=("", 14, "bold"),
                               fill="white smoke", tag="grim")
            canvas.create_image(300 + self.menu_kans[1], 235+((i-self.count)*81), image=self.contents_opacity2, anchor="nw", tag="grim")
            canvas.create_image(485 + self.menu_kans[1], 270+((i-self.count)*81), image=self.vehicle_image[i-self.count], tag="grim")
            canvas.create_text(485 + self.menu_kans[1], 305+((i-self.count)*81), text=self.sort_kill[i]["name"], font=("", 10, "bold"),
                                fill="white smoke", tag="grim")
            for j in range(2+self.count,5+self.count):
                canvas.create_image(300 + self.menu_kans[j-self.count], 235+((i-self.count)*81), image=self.contents_opacity3, anchor="nw", tag="grim")
            canvas.create_text(390 + self.menu_kans[2],275+((i-self.count)*81), text=format(self.sort_kill[i]["stat"]["kills"],","),
                               font=("", 14, "bold"), fill="white smoke", tag="grim")
            self.m, self.s = divmod(self.sort_kill[i]["stat"]["time"], 60)
            self.h, self.m = divmod(self.m, 60)
            canvas.create_text(390 + self.menu_kans[2], 300 + ((i-self.count)* 81),text="{0}시간 {1}분".format(self.h,self.m),
                               font=("", 10, "bold"), fill="gray", tag="grim")
            canvas.create_text(390 + self.menu_kans[3], 275+((i-self.count)*81),text='{0:.2f}'.format(self.sort_kill[i]["extra"]["kpm"]),
                               font=("", 14, "bold"), fill="white smoke", tag="grim")
            canvas.create_text(390 + self.menu_kans[4], 275 + ((i-self.count) * 81),
                               text='{0:,}'.format(self.sort_kill[i]["stat"]["destroys"]),
                               font=("", 14, "bold"), fill="white smoke", tag="grim")