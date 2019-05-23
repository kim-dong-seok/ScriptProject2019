import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter.ttk
from bs4 import  BeautifulSoup
import urllib.request


class player_data:
    def __init__(self,player_name,player_plat):
        self.data = requests.get("https://api.bf4stats.com/api/playerInfo?plat=" + player_plat + "&name=" + player_name + "&output=json").json()
        self.player = self.data["player"]
        self.stats =self.data["stats"]
        self.dogtags =self.data["dogtags"]
        self.weapons = self.data["weapons"]
        self.weaponCategory = self.data["weaponCategory"]
        self.kititems = self.data["kititems"]
        self.vehicles = self.data["vehicles"]
        self.modes = self.stats["modes"]
        self.kits = self.stats["kits"]
        self.vehicleCategory =self.data["vehicleCategory"]
        self.awards = self.data["awards"]
        self.assignments = self.data["assignments"]
        self.upcomingUnlocks = self.data["upcomingUnlocks"]
        self.rank_weapons = sorted(self.weapons, key=lambda t: t["stat"]["kills"], reverse=True)
        self.rank_vehicles = sorted(self.vehicles, key=lambda t: t["stat"]["kills"], reverse=True)
        self.rank_modes = sorted(self.modes, key=lambda t: t["score"], reverse=True)


class player_main:
    def __init__(self,player_data):
        self.player_data=player_data
        self.rank_list=[
                        "이병","이병 2","이병 3","이병 4","이병 5",
                        "일병","일병 2","일병 3","일병 4","일병 5",
                        "상병","상병 2","상병 3","상병 4","상병 5",
                        "병장",  "병장 2", "병장 3", "병장 4", "병장 5",
                        "하사",  "하사 2", "하사 3", "하사 4", "하사 5",
                        "중사",  "중사 2", "중사 3", "중사 4", "중사 5",
                        "상사",  "상사 2", "상사 3", "상사 4", "상사 5",
                        "일등상사", "일등상사 2", "일등상사 3", "일등상사 4", "일등상사 5",
                        "원사",  "원사 2", "원사 3", "원사 4", "원사 5",
                        "주임원사",  "주임원사 2", "주임원사 3", "주임원사 4", "주임원사 5",
                        "준위 1", "준위 1 2", "준위 1 3", "준위 1 4", "준위 1 5",
                        "준위 2",  "준위 2 2", "준위 2 3", "준위 2 4", "준위 2 5",
                        "준위 3",  "준위 3 2", "준위 3 3", "준위 3 4", "준위 3 5",
                        "준위 4",  "준위 4 2", "준위 4 3", "준위 4 4", "준위 4 5",
                        "준위 5",  "준위 5 2", "준위 5 3", "준위 5 4", "준위 5 5",
                        "소위", "소위 2", "소위 3", "소위 4", "소위 5",
                        "중위",  "중위 2", "중위 3", "중위 4", "중위 5",
                        "대위",  "대위 2", "대위 3", "대위 4", "대위 5",
                        "소령", "소령 2", "소령 3", "소령 4", "소령 5",
                        "중령",  "중령 2", "중령 3", "중령 4", "중령 5",
                        "대령", "대령 2", "대령 3", "대령 4", "대령 5",
                        "대령 6",  "대령 7", "대령 8", "대령 9", "대령 10",
                        "준장",  "준장 2", "준장 3", "준장 4", "준장 5",
                        "준장 6", "준장 7", "준장 8", "준장 9", "준장 10",
                        "소장", "소장 2", "소장 3", "소장 4", "소장 5",
                        "소장 6",  "소장 7", "소장 8", "소장 9", "소장 10",
                        "중장", "중장 2", "중장 3", "중장 4", "중장 5",
                        "중장 6",  "중장 7", "중장 8", "중장 9", "중장 10",
                        "대장"]

        self.kits_keys=list( self.player_data.kits.keys())
        self.kits_score=[155000,131000,134000,104000,20000]
        self.skill=0
        self.score=0
        self.star_gauge=[0]*4
        self.service_star_gauge = [0] * 5
        self.service_star = [0] * 5
        for i in range(5):
            self.service_star[i] = self.player_data.kits[self.kits_keys[i]]["score"] / self.kits_score[i]

        self.origin_level_image = Image.open(self.player_data.player["rank"]["imgLarge"]).resize((120, 120))
        self.level_image = ImageTk.PhotoImage(self.origin_level_image)
        self.origin_contents_opacity = Image.open("내용배경.png")
        self.origin_rank1_weapon= Image.open(self.player_data.rank_weapons[0]["imgFancy"]).resize((147, 88))
        self.rank1_weapon= ImageTk.PhotoImage(self.origin_rank1_weapon)
        self.origin_rank2_weapon = Image.open(self.player_data.rank_weapons[1]["imgFancy"]).resize((73, 44))
        self.rank2_weapon = ImageTk.PhotoImage(self.origin_rank2_weapon)
        self.origin_rank3_weapon = Image.open(self.player_data.rank_weapons[2]["imgFancy"]).resize((73, 44))
        self.rank3_weapon = ImageTk.PhotoImage(self.origin_rank3_weapon)
        self.origin_rank1_vehicle = Image.open(self.player_data.rank_vehicles[0]["imgFancy"]).resize((147, 88))
        self.rank1_vehicle = ImageTk.PhotoImage(self.origin_rank1_vehicle)
        self.origin_rank2_vehicle = Image.open(self.player_data.rank_vehicles[1]["imgFancy"]).resize((73, 44))
        self.rank2_vehicle = ImageTk.PhotoImage(self.origin_rank2_vehicle)
        self.origin_rank3_vehicle = Image.open(self.player_data.rank_vehicles[2]["imgFancy"]).resize((73, 44))
        self.rank3_vehicle = ImageTk.PhotoImage(self.origin_rank3_vehicle)
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
        self.orlgin_gauge_bg = Image.open("게이지배경.png")
        self.gauge_bg = ImageTk.PhotoImage(self.orlgin_gauge_bg.resize((160, 28)))
        self.orlgin_gauge = Image.open("게이지.png")
        self.gauge = [ImageTk.PhotoImage(self.orlgin_gauge.resize((150, 20))) for i in range(4)]
        self.service_gauge_bg = ImageTk.PhotoImage(self.orlgin_gauge_bg.resize((230, 28)))
        self.service_gauge = [ImageTk.PhotoImage(self.orlgin_gauge.resize((220, 20))) for i in range(5)]
        self.rank_gauge_bg = ImageTk.PhotoImage(self.orlgin_gauge_bg.resize((291, 28)))
        self.rank_gauge = ImageTk.PhotoImage(self.orlgin_gauge.resize((286, 20)))
        icons=["KitAssault","KitEngineer","KitSupport","KitRecon","KitCommander"]
        self.orlgin_icons=[0]*5
        self.icons_image = [0] * 5
        for i in range(5):
            self.orlgin_icons[i] = Image.open("bf4/lbicons/"+icons[i]+".png")
            self.icons_image[i]=ImageTk.PhotoImage(self.orlgin_icons[i].resize((28, 28)))
        self.orlgin_dogtags = [0] * 2
        self.dogtags_image = [0] * 2
        self.dogtags=[self.player_data.dogtags["basic"],self.player_data.dogtags["advanced"]]

        self.orlgin_dogtags[0] = Image.open(self.dogtags[0]["img"]).resize((128, 64)).rotate(20)
        self.dogtags_image[0] = ImageTk.PhotoImage(self.orlgin_dogtags[0])
        self.orlgin_dogtags[1] = Image.open(self.dogtags[1]["img"]).resize((128, 64))
        self.dogtags_image[1] = ImageTk.PhotoImage(self.orlgin_dogtags[1])



    def mode_star(self,star):
        if star["id"]==1: #컨퀘스트
            return star["score"]/21000
        elif star["id"]==2: #러쉬
            return star["score"]/15000
        elif star["id"]==2097152: #오블리터레이션
            return star["score"]/16500
        elif star["id"]==8388608: #제공권
            return star["score"]/12000
        elif star["id"]==8:   #데스매치
            return star["score"]/6000
        elif star["id"]==34359738368: #체인링크
            return star["score"]/10000
        elif star["id"]==67108864: #대형 캐리어어설트
            return star["score"]/22000
        elif star["id"]==134217728: #캐리어어설트
            return star["score"]/22000
        elif star["id"]==524288: #깃발뻇기
            return star["score"]/7500
    def hangul_mode(self,mode):
        if mode["id"]==1:
            return "컨퀘스트"
        elif mode["id"]==2:
            return "러쉬"
        elif mode["id"]==2097152:
            return "오블리터레이션"
        elif mode["id"]==8388608:
            return "제공권"
        elif mode["id"]==8:
            return "데스매치"
        elif mode["id"]==34359738368:
            return "체인 링크"
        elif mode["id"]==1024:
            return "도미네이션"
        elif mode["id"]==67108864:
            return "캐리어 어설트"
        elif mode["id"]==134217728:
            return "캐리어 어설트"
        elif mode["id"]==16777216:
            return "디퓨즈"
        elif mode["id"]==524288:
            return "Capture the Flag"
    def update(self):

        if self.skill<self.player_data.stats["skill"]:
            self.skill+=self.player_data.stats["skill"]/20
        else:
            self.skill=self.player_data.stats["skill"]
        if self.player_data.player["score"]>32160000:
            self.score=32160000
        else:
            if self.score<self.player_data.player["score"]:
                self.score += self.player_data.player["score"]/ 10
            if self.score>self.player_data.player["score"]:
                self.score = self.player_data.player["score"]

        for i in range(4):
            self.mode_stars =(self.mode_star(self.player_data.rank_modes[i])*100)%100
            if self.mode_stars>0:
                if self.star_gauge[i]<self.mode_stars:
                    self.star_gauge[i] += self.mode_stars/10
                    self.gauge[i]=ImageTk.PhotoImage(self.orlgin_gauge.resize((int(1.5* self.star_gauge[i]), 20)))
            else:
                self.gauge[i] = ImageTk.PhotoImage(self.orlgin_gauge.resize((1, 20)))
        for i in range(5):
            if self.service_star[i]>0:
                if self.service_star_gauge[i]<(self.service_star[i]*100)%100:
                    self.service_star_gauge[i] += ((self.service_star[i]*100)%100)/10
                    self.service_gauge[i]=ImageTk.PhotoImage(self.orlgin_gauge.resize((int(2* self.service_star_gauge[i]), 20)))
            else:
                self.service_gauge[i] = ImageTk.PhotoImage(self.orlgin_gauge.resize((1, 20)))
        if self.player_data.player["score"] < 32160000:
            self.rank_gauge = ImageTk.PhotoImage(self.orlgin_gauge.resize((int(280*(self.score/self.player_data.player["rank"]["next"]["needed"])), 20)))
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
        canvas.create_image(320, 380, image=self.rank_gauge_bg, anchor="nw", tag="grim")
        canvas.create_image(323, 384, image=self.rank_gauge, anchor="nw", tag="grim")
        canvas.create_text(320, 415, text=self.rank_list[self.player_data.player["rank"]["nr"]], font=("", 10, "bold"), anchor="nw", fill="gray", tag="grim")
        if self.player_data.player["score"]<32160000:
            canvas.create_text(611, 415, text=str( self.player_data.player["score"])+"/"+str(self.player_data.player["rank"]["next"]["needed"]), font=("", 10, "bold"), anchor="ne",
                           fill="ghost white", tag="grim")
        else:
            canvas.create_text(611, 415, text=str(self.player_data.player["score"]) + "/" + str(
                self.player_data.player["rank"]["needed"]), font=("", 10, "bold"), anchor="ne",
                               fill="ghost white", tag="grim")
        canvas.create_text(642, 218, text="스킬", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(632, 240, image=self.contents_opacity_1, anchor="nw", tag="grim")
        canvas.create_text(797, 275, text=str(format(self.skill,".0f")), font=("", 40, "bold"), fill="ghost white", tag="grim")
        canvas.create_image(632, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(687, 350, text="K/D", font=("", 10, "bold"),fill="gray", tag="grim")
        canvas.create_text(687, 375, text=str(round(self.player_data.stats['kills']/self.player_data.stats['deaths'],2)), font=("", 18, "bold"), fill="ghost white", tag="grim")
        canvas.create_image(743, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(798, 350, text="분당 점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 375, text=str(int(self.player_data.player['score'] / (self.player_data.player['timePlayed']/60))), font=("", 18, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(854, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(909, 350, text="분당 사살", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(909, 375, text=str(round(self.player_data.stats['kills'] / (self.player_data.player['timePlayed'] / 60),2)), font=("", 18, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(632, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(687, 410, text="사살", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(687, 435, text=str(self.player_data.stats['kills']), font=("", 12, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(743, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(798, 410, text="점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 435, text=format(self.player_data.player['score'],','), font=("", 12, "bold"),fill="ghost white", tag="grim")
        canvas.create_image(854, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(909, 410, text="시간", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(909, 435, text=str(int((self.player_data.player['timePlayed']/60)/60))+"시간 "+str(int((self.player_data.player['timePlayed']/60)%60))+"분", font=("", 12, "bold"),fill="ghost white", tag="grim")
        canvas.create_text(974, 218, text="인식표", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(964, 240, image=self.contents_opacity, anchor="nw", tag="grim")
        canvas.create_image(964, 240, image=self.dogtags_image[0], anchor="nw", tag="grim")
        canvas.create_image(1264, 240, image=self.dogtags_image[1], anchor="nw", tag="grim")

        canvas.create_text(310, 460, text="공로 스타", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(300, 482, image=self.contents_opacity2, anchor="nw", tag="grim")
        for i in range(5):

            canvas.create_image(320, 487 + (32 * i), image=self.icons_image[i], anchor="nw", tag="grim")
            canvas.create_image(373, 487 + (32 * i), image=self.service_gauge_bg, anchor="nw", tag="grim")
            canvas.create_image(376, 491+(32*i), image=self.service_gauge[i], anchor="nw", tag="grim")
            canvas.create_text(466, 492+(32*i), text="★ " + str(self.player_data.kits[self.kits_keys[i]]["stars"]), font=("", 11, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_text(642, 460, text="팀플레이", font=("", 12, "bold"), anchor="nw",fill="ghost white", tag="grim")
        canvas.create_image(632, 482, image=self.contents_opacity2_1, anchor="nw", tag="grim")
        canvas.create_image(632, 597, image=self.contents_opacity2_2, anchor="nw", tag="grim")
        canvas.create_text(974, 460, text="최고 순위표", font=("", 12, "bold"), anchor="nw",fill="ghost white", tag="grim")
        canvas.create_image(964, 482, image=self.contents_opacity2_3, anchor="nw", tag="grim")
        canvas.create_image(1205, 482, image=self.contents_opacity2_4, anchor="nw", tag="grim")
        canvas.create_image(1205, 568, image=self.contents_opacity2_4, anchor="nw", tag="grim")

        canvas.create_text(310, 681, text="최고 무기", font=("", 12, "bold"), anchor="nw",fill="ghost white", tag="grim")
        canvas.create_image(300, 703, image=self.contents_opacity3_1, anchor="nw", tag="grim")
        canvas.create_image(425, 743, image=self.rank1_weapon,  tag="grim")
        canvas.create_text(320, 785, text=self.player_data.rank_weapons[0]["name"], font=("", 10, "bold"), anchor="nw", fill="gray", tag="grim")
        canvas.create_text(320, 805, text=str(self.player_data.rank_weapons[0]["stat"]["kills"])+" 사살", font=("", 13, "bold"), anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(551, 703, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(591, 728, image=self.rank2_weapon, tag="grim")
        canvas.create_text(591, 758, text=str(self.player_data.rank_weapons[1]["stat"]["kills"]) + " 사살", font=("", 10, "bold"), fill="ghost white", tag="grim")
        canvas.create_image(551, 774, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(591, 799, image=self.rank3_weapon, tag="grim")
        canvas.create_text(591, 829, text=str(self.player_data.rank_weapons[2]["stat"]["kills"]) + " 사살",  font=("", 10, "bold"), fill="ghost white", tag="grim")

        canvas.create_text(642, 681, text="최고 탑승장비", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(632, 703, image=self.contents_opacity3_1, anchor="nw", tag="grim")
        canvas.create_image(757, 743, image=self.rank1_vehicle, tag="grim")
        canvas.create_text(652, 785, text=self.player_data.rank_vehicles[0]["name"], font=("", 10, "bold"), anchor="nw", fill="gray",tag="grim")
        canvas.create_text(652, 805, text=str(self.player_data.rank_vehicles[0]["stat"]["kills"]) + " 사살", font=("", 13, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(883, 703, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(923, 728, image=self.rank2_vehicle, tag="grim")
        canvas.create_text(923, 758, text=str(self.player_data.rank_vehicles[1]["stat"]["kills"]) + " 사살", font=("", 10, "bold"), fill="ghost white", tag="grim")
        canvas.create_image(883, 774, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(923, 799, image=self.rank3_vehicle, tag="grim")
        canvas.create_text(923, 829, text=str(self.player_data.rank_vehicles[2]["stat"]["kills"]) + " 사살", font=("", 10, "bold"),fill="ghost white", tag="grim")

        canvas.create_text(974, 681, text="최고 게임 모드", font=("", 12, "bold"),anchor="nw", fill="ghost white", tag="grim")
        canvas.create_image(964, 703, image=self.contents_opacity3, anchor="nw", tag="grim")
        for i in range(4):
            canvas.create_text(984, 713+(33*i), text=self.hangul_mode(self.player_data.rank_modes[i]) , font=("", 10, "bold"),anchor="nw",fill="gray", tag="grim")
            canvas.create_image(1119, 708+(32*i), image=self.gauge_bg, anchor="nw", tag="grim")
            canvas.create_image(1121, 712+(32*i), image=self.gauge[i], anchor="nw", tag="grim")
            canvas.create_text(1184, 713+(32*i), text="★ " + str(int(self.mode_star(self.player_data.rank_modes[i]))), font=("", 11, "bold"),anchor="nw", fill="ghost white",tag="grim")





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
        self.player_data=player_data("sharqia","pc")
        self.player_name = " "
        self.scene=0
        self.b1ck=0
        self.bcheck=-1
        self.canvas = Canvas(self.window,  width=self.width, height=self.height)
        self.canvas.pack()
        self.orlgin_bgimage = Image.open("bg.jpg")
        self.bgimage= ImageTk.PhotoImage(self.orlgin_bgimage.resize(( self.width, self.height)))
        self.originimage2 = Image.open("bf4.gg.png").resize((160, 32))
        self.logoImage = ImageTk.PhotoImage(self.originimage2)
        self.orlgin_logo_bg=Image.open("로고배경.png")
        self.logo_bg = ImageTk.PhotoImage(self.orlgin_logo_bg.resize((1600, 45)))
        self.orlgin_search_bg = Image.open("검색배경.png")
        self.search_bg = ImageTk.PhotoImage(self.orlgin_search_bg.resize((1600, 45)))
        self.orlgin_name_bg = Image.open("내용배경.png")
        self.name_bg = ImageTk.PhotoImage(self.orlgin_name_bg.resize((350, 45)))


        self.count = 0
        self.e1 = Entry(self.canvas, font=("", 20), width=20)
        self.e1.insert(0, "Player name")
        self.e1.place(x=500, y=400)
        self.b1 = Button(self.canvas, text="Search", font=("", 14, "bold"), command=self.search, width=9, pady=0)
        self.b1.place(x=1100, y=400, anchor="ne")
        self.str=StringVar()
        self.c1 = tkinter.ttk.Combobox(self.canvas, textvariable=self.str, width=7, font=("", 20))
        self.c1["values"]=("pc", "ps4", "xone", "ps3", "xbox")
        self.c1.set("Platform")
        self.c1.place(x=835, y=400)
        self.e2 = Entry(self.canvas, font=("", 13,), width=20)
        self.e2.insert(0, "Player name")
        self.c2 = tkinter.ttk.Combobox(self.canvas, textvariable=self.str, width=8, font=("", 12))
        self.c2["values"]=("pc", "ps4", "xone", "ps3", "xbox")
        self.c2.set("Platform")
        self.b2 = Button(self.canvas, text="Search", font=("", 10, "bold"), command=self.search,
                         width=9)

        self.menu_buttons = [menu_button(300+(i*166),165) for i in range(6)]
        self.menu_buttons[0].btext="개요"
        self.menu_buttons[1].btext ="통계"
        self.menu_buttons[2].btext = "잠김 해제"
        self.menu_buttons[3].btext = "로드아웃"
        self.menu_buttons[4].btext = "과제"
        self.menu_buttons[5].btext = "포상"
        self.menu_buttons[0].ckeck=2
        self.player_main=player_main(self.player_data)
        self.start_page=start_page()


        self.window.bind('<Motion>', self.motion)
        self.delay = 10
        self.update()
        self.window.mainloop()

    def search(self):
        if self.scene==0:
            self.player_name = self.e1.get()
            self.scene=1
            self.e1.place_forget()
            self.b1.place_forget()
            self.c1.place_forget()
            self.player_data=player_data( self.player_name, self.c1.get())
            self. player_main=player_main(self.player_data)
            self.e2.place(x=300, y=self.height / 16)
            self.c2.place(x=470, y=self.height / 16)
            self.b2.place(x=565, y=self.height / 16)
    def click(self,event):
        if self.menu_buttons[self.bcheck].ckeck==1:
            for i in range(6):
                if self.menu_buttons[i].ckeck == 2:
                    self.menu_buttons[i].ckeck = 0
            self.menu_buttons[self.bcheck].ckeck = 2


    def motion(self,event):
        if self.scene==1:
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
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame).resize((1600, 900)))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW,tag="grim")
            if self.scene == 1:
                self.player_main.update()
        self.draw()
        self.window.after(self.delay, self.update)
    def draw(self):
        if self.scene==0:
            self.start_page.draw(self.canvas)
        elif self.scene==1:
            self.canvas.create_image(self.width / 2,self.height/40 , image=self.logo_bg,tag="grim")
            self.canvas.create_image(self.width / 2, self.height / 13, image=self.search_bg,tag="grim")
            self.canvas.create_image(300, 10, image=self.logoImage,anchor="nw",tag="grim")
            self.canvas.create_image(300, 108, image=self.name_bg,anchor="nw",tag="grim")
            self.canvas.create_text(320,115, text=self.player_data.player["plat"].upper(),
                                    font=("", 20,"bold"), fill="ghost white", tag="grim",anchor="nw")
            self.canvas.create_text(420,115, text="["+self.player_data.player["tag"]+"]",
                                    font=("", 20, "bold"), fill="ghost white", tag="grim",anchor="nw")
            self.canvas.create_text(510,115, text=self.player_data.player["name"],
                                    font=("", 20, "bold"), fill="ghost white", tag="grim",anchor="nw")
            for menu_button in self.menu_buttons:
                menu_button.draw(self.canvas)
            self.player_main.draw(self.canvas)

class start_page():
    def __init__(self):
        self.originimage2 = Image.open("bf4.gg.png")
        self.Big_logoImage = ImageTk.PhotoImage(self.originimage2.resize((600, 120)))
        self.orlginOpacity = Image.open("opacity.png")
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
                                fill="ghost white", tag="grim")
        for i in range(5):
            canvas.create_text(600 + (100 * i), 555, text=self.online_players[i]["label"], font=("", 16),
                                    fill="ghost white", tag="grim")
            canvas.create_text(600 + (100 * i), 600, text=self.online_players[i]["count"], font=("", 19, "bold"),
                                    fill="ghost white", tag="grim")
            canvas.create_text(600 + (100 * i), 645, text="최다 접속", font=("", 14), fill="ghost white", tag="grim")
            canvas.create_text(600 + (100 * i), 675, text=self.online_players[i]["peak24"], font=("", 16),
                                    fill="ghost white", tag="grim")

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

bf4_main()