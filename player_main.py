from tkinter import *
from PIL import Image, ImageTk




class player_main:
    def __init__(self,player_data):
        self.mx=0
        self.my=0
        self.mouse_count=10
        self.mouse_count2 = 0
        self.mcount = 0
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
        self.origin_contents_opacity = Image.open("ui_image/내용배경.png")
        self.origin_rank1_weapon= Image.open("bf4/weapons_fancy/" + self.player_data.rank_weapons[0]["name"] + ".png").resize((147, 88))
        self.rank1_weapon= ImageTk.PhotoImage(self.origin_rank1_weapon)
        self.origin_rank2_weapon = Image.open("bf4/weapons_fancy/" + self.player_data.rank_weapons[1]["name"] + ".png").resize((73, 44))
        self.rank2_weapon = ImageTk.PhotoImage(self.origin_rank2_weapon)
        self.origin_rank3_weapon = Image.open("bf4/weapons_fancy/" + self.player_data.rank_weapons[2]["name"] + ".png").resize((73, 44))
        self.rank3_weapon = ImageTk.PhotoImage(self.origin_rank3_weapon)
        self.origin_rank1_vehicle = Image.open("bf4/vehicles_fancy/" + self.player_data.rank_vehicles[0]["name"] + ".png").resize((147, 88))
        self.rank1_vehicle = ImageTk.PhotoImage(self.origin_rank1_vehicle)
        self.origin_rank2_vehicle = Image.open("bf4/vehicles_fancy/" + self.player_data.rank_vehicles[1]["name"] + ".png").resize((73, 44))
        self.rank2_vehicle = ImageTk.PhotoImage(self.origin_rank2_vehicle)
        self.origin_rank3_vehicle = Image.open("bf4/vehicles_fancy/" + self.player_data.rank_vehicles[2]["name"] + ".png").resize((73, 44))
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
        self.orlgin_menu_bg = Image.open("ui_image/메뉴배경.png")
        self.menu_bg = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((331, 25)))
        self.orlgin_gauge_bg = Image.open("ui_image/게이지배경.png")
        self.gauge_bg = ImageTk.PhotoImage(self.orlgin_gauge_bg.resize((160, 28)))
        self.orlgin_gauge = Image.open("ui_image/게이지.png")
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

        self.orlgin_dogtags[0] = Image.open(self.dogtags[0]["img"]).resize((192, 192)).rotate(-20)
        self.dogtags_image[0] = ImageTk.PhotoImage(self.orlgin_dogtags[0])
        self.orlgin_dogtags[1] = Image.open(self.dogtags[1]["img"]).resize((192, 192))
        self.dogtags_image[1] = ImageTk.PhotoImage(self.orlgin_dogtags[1])
        self.orlgin_circle = Image.open("ui_image/원채우기.png")
        self.circle_image = ImageTk.PhotoImage(self.orlgin_circle.resize((28, 28)))
        self.win_percent=100-int(100/(1 + self.player_data.stats["extra"]["wlr"]))
        self.win_rotation=-360+int(360 / (1 + self.player_data.stats["extra"]["wlr"]))
        self.lose_rotation = - int(360 / (1 + self.player_data.stats["extra"]["wlr"]))+10
        self.win=0
        self.lose=0
        self.win_rotation_finish=0
        self.lose_rotation_finish = 0

        self.origin_player_ranking1 = self.ranking_image_find(self.player_data.sort_ranking1)
        self.player_ranking1 = ImageTk.PhotoImage(self.origin_player_ranking1)
        self.origin_player_ranking2 = self.ranking_image_find(self.player_data.sort_ranking2)
        if self.player_data.sort_ranking2["group"]=="kititem" or self.player_data.sort_ranking2["group"]=="vehicle" or self.player_data.sort_ranking2["group"]=="weapon":
            self.player_ranking2 = ImageTk.PhotoImage(self.origin_player_ranking2.resize((92,55)))
        else:
            self.player_ranking2 = ImageTk.PhotoImage(self.origin_player_ranking2.resize((55, 55)))
        self.origin_player_ranking3 = self.ranking_image_find(self.player_data.sort_ranking3)
        if self.player_data.sort_ranking3["group"] == "kititem" or self.player_data.sort_ranking3[
            "group"] == "vehicle" or self.player_data.sort_ranking3["group"] == "weapon":
            self.player_ranking3 = ImageTk.PhotoImage(self.origin_player_ranking3.resize((92, 55)))
        else:
            self.player_ranking3 = ImageTk.PhotoImage(self.origin_player_ranking3.resize((55, 55)))
        self.mouse_check_point=[[300,240],[632,240],[964,240],[300,482],[632,482],[964,482],[300,703],[632,703],[964,703]]
    def ranking_image_find(self,player_ranking):
        if player_ranking["group"]=="player":
            return Image.open("bf4/lbicons/" + player_ranking["label"] + ".png").resize((110, 110))
        elif player_ranking["group"]=="kit":
            return Image.open("bf4/lbicons/Kit" + player_ranking["label"] + ".png").resize((110, 110))
        elif player_ranking["group"]=="mode":
            return Image.open("bf4/lbicons/" + player_ranking["label"] + ".png").resize((110, 110))
        elif player_ranking["group"]=="weapon":
            return Image.open("bf4/weapons_fancy/"+player_ranking["ident"]+".png").resize((184, 110))
        elif player_ranking["group"]=="vehicle":
            return Image.open("bf4/vehicles_fancy/" + player_ranking["ident"] + ".png").resize((184, 110))
        elif player_ranking["group"]=="ribbon":
            return Image.open("bf4/ribbons/" + player_ranking["ident"] + ".png").resize((110, 110))
        elif player_ranking["group"]=="kititem":
            return Image.open( "bf4/kititems_fancy/" + player_ranking["ident"] + ".png").resize((184, 110))
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
    def mouse_check(self):

        if self.mouse_check_point[0][0] < self.mx and self.mouse_check_point[0][0] + 331 > self.mx and\
            self.mouse_check_point[0][1]<self.my and self.mouse_check_point[0][1]+215>self.my:
            self.mouse_count=1
            self.mouse_count2 = 1
            self.mcount+=1
        if self.mouse_check_point[1][0] < self.mx and self.mouse_check_point[1][0] + 331 > self.mx and\
            self.mouse_check_point[1][1]<self.my and self.mouse_check_point[1][1]+215>self.my:
            self.mouse_count=1
            self.mouse_count2 = 2
            self.mcount+=1
        if self.mouse_check_point[2][0] < self.mx and self.mouse_check_point[2][0] + 331 > self.mx and\
            self.mouse_check_point[2][1]<self.my and self.mouse_check_point[2][1]+215>self.my:
            self.mouse_count=1
            self.mouse_count2 = 3
            self.mcount+=1

        if self.mouse_check_point[3][0] < self.mx and self.mouse_check_point[3][0] + 331 > self.mx and\
            self.mouse_check_point[3][1]<self.my and self.mouse_check_point[3][1]+170>self.my:
            self.mouse_count=1
            self.mouse_count2 = 4
            self.mcount += 1
        if self.mouse_check_point[4][0] < self.mx and self.mouse_check_point[4][0] + 331 > self.mx and \
            self.mouse_check_point[4][1] < self.my and self.mouse_check_point[4][1] + 170 > self.my:
            self.mouse_count =1
            self.mouse_count2 = 5
            self.mcount += 1
        if self.mouse_check_point[5][0] < self.mx and self.mouse_check_point[5][0] + 331 > self.mx and\
            self.mouse_check_point[5][1]<self.my and self.mouse_check_point[5][1]+170>self.my:
            self.mouse_count=4
            self.mouse_count2 = 6
            self.mcount += 1

        if self.mouse_check_point[6][0] < self.mx and self.mouse_check_point[6][0] + 331 > self.mx and\
            self.mouse_check_point[6][1]<self.my and self.mouse_check_point[6][1]+170>self.my:
            self.mouse_count=2
            self.mouse_count2 = 7
            self.mcount += 1
        if self.mouse_check_point[7][0] < self.mx and self.mouse_check_point[7][0] + 331 > self.mx and\
            self.mouse_check_point[7][1]<self.my and self.mouse_check_point[7][1]+170>self.my:
            self.mouse_count=3
            self.mouse_count2 = 8
            self.mcount += 1
        if self.mouse_check_point[8][0] < self.mx and self.mouse_check_point[8][0] + 331 > self.mx and\
            self.mouse_check_point[8][1]<self.my and self.mouse_check_point[8][1]+170>self.my:
            self.mouse_count=1
            self.mouse_count2 = 9
            self.mcount += 1

        if self.mcount==0:
            self.mouse_count=10
            self.mouse_count2 = 0
        self.mcount=0
    def update(self,mx,my):
        self.mx=mx
        self.my = my
        self.mouse_check()
        if self.win_rotation_finish<10:
            self.win+=self.win_rotation/10
            self.win_rotation_finish+=1
        elif self.win_rotation_finish==9:
            self.win = self.win_rotation
            self.win_rotation_finish+=1
        if self.win_rotation_finish==10:
            if self.lose_rotation_finish < 10:
                self.lose += self.lose_rotation / 10
                self.lose_rotation_finish+=1
            elif self.lose_rotation_finish==9:
                self.lose = self.lose_rotation
                self.win_rotation_finish +=1

        if self.skill<self.player_data.stats["skill"]:
            self.skill+=self.player_data.stats["skill"]/20
        elif self.skill>self.player_data.stats["skill"]:
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
            elif self.mode_stars<0:
                self.gauge[i] = ImageTk.PhotoImage(self.orlgin_gauge.resize((1, 20)))
        for i in range(5):
            if self.service_star[i]>0:
                if self.service_star_gauge[i]<(self.service_star[i]*100)%100:
                    self.service_star_gauge[i] += ((self.service_star[i]*100)%100)/10
                    self.service_gauge[i]=ImageTk.PhotoImage(self.orlgin_gauge.resize((int(2* self.service_star_gauge[i]), 20)))
            elif self.service_star[i]<0:
                self.service_gauge[i] = ImageTk.PhotoImage(self.orlgin_gauge.resize((1, 20)))
        if self.player_data.player["score"] < 32160000:
            self.rank_gauge = ImageTk.PhotoImage(self.orlgin_gauge.resize((int(280*(self.score/self.player_data.player["rank"]["next"]["needed"])), 20)))
    def draw(self,canvas):
        for i in range(3):
            if self.mouse_count2==i+1:
                canvas.create_image(self.mouse_check_point[i][0], 240, image=self.contents_opacity, anchor="nw", tag="grim")
        for i in range(3,6):
            if self.mouse_count2==i+1:
                canvas.create_image(self.mouse_check_point[i][0], 482, image=self.contents_opacity2, anchor="nw", tag="grim")
        for i in range(6,9):
            if self.mouse_count2==i+1:
                canvas.create_image(self.mouse_check_point[i][0], 703, image=self.contents_opacity3, anchor="nw", tag="grim")
        for j in range(3):
            canvas.create_image(300+(j*332), 214, image=self.menu_bg, anchor="nw", tag="grim")
        for j in range(3):
            canvas.create_image(300+(j*332), 456, image=self.menu_bg, anchor="nw", tag="grim")
        for j in range(3):
            canvas.create_image(300 + (j * 332), 677, image=self.menu_bg, anchor="nw", tag="grim")

        canvas.create_text(310, 218, text="계급", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(300, 240, image=self.contents_opacity, anchor="nw", tag="grim")
        canvas.create_image(465, 320, image=self.level_image, tag="grim")
        canvas.create_image(320, 380, image=self.rank_gauge_bg, anchor="nw", tag="grim")
        canvas.create_image(323, 384, image=self.rank_gauge, anchor="nw", tag="grim")
        canvas.create_text(320, 415, text=self.rank_list[self.player_data.player["rank"]["nr"]], font=("", 10, "bold"), anchor="nw", fill="gray", tag="grim")
        if self.player_data.player["score"]<32160000:
            canvas.create_text(611, 415, text=str( self.player_data.player["score"])+"/"+str(self.player_data.player["rank"]["next"]["needed"]), font=("", 10, "bold"), anchor="ne",
                           fill="white smoke", tag="grim")
        else:
            canvas.create_text(611, 415, text=str(self.player_data.player["score"]) + "/" + str(
                self.player_data.player["rank"]["needed"]), font=("", 10, "bold"), anchor="ne",
                               fill="white smoke", tag="grim")
        canvas.create_text(642, 218, text="스킬", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(632, 240, image=self.contents_opacity_1, anchor="nw", tag="grim")
        canvas.create_text(797, 275, text=str(format(self.skill,".0f")), font=("", 40, "bold"), fill="white smoke", tag="grim")
        canvas.create_rectangle(712,310,883,320,outline="white smoke",tag="grim")
        canvas.create_rectangle(712+(self.skill/1000*170), 310, 722+(self.skill/1000*170), 320, fill="white smoke",outline="white smoke",tag="grim")
        canvas.create_image(632, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(687, 350, text="K/D", font=("", 10, "bold"),fill="gray", tag="grim")
        canvas.create_text(687, 375, text=str(round(self.player_data.stats["extra"]["kdr"],2)), font=("", 18, "bold"), fill="white smoke", tag="grim")
        canvas.create_image(743, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(798, 350, text="분당 점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 375, text=str(int(self.player_data.stats["extra"]["spm"])), font=("", 18, "bold"),fill="white smoke", tag="grim")
        canvas.create_image(854, 334, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(909, 350, text="분당 사살", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(909, 375, text=str(round(self.player_data.stats["extra"]["kpm"],2)), font=("", 18, "bold"),fill="white smoke", tag="grim")
        canvas.create_image(632, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(687, 410, text="사살", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(687, 435, text=str(self.player_data.stats['kills']), font=("", 12, "bold"),fill="white smoke", tag="grim")
        canvas.create_image(743, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(798, 410, text="점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 435, text=format(self.player_data.player['score'],','), font=("", 12, "bold"),fill="white smoke", tag="grim")
        canvas.create_image(854, 395, image=self.contents_opacity_2, anchor="nw", tag="grim")
        canvas.create_text(909, 410, text="시간", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(909, 435, text=str(int((self.player_data.player['timePlayed']/60)/60))+"시간 "+str(int((self.player_data.player['timePlayed']/60)%60))+"분", font=("", 12, "bold"),fill="white smoke", tag="grim")
        canvas.create_text(974, 218, text="인식표", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(964, 240, image=self.contents_opacity, anchor="nw", tag="grim")
        canvas.create_image(1094, 250, image=self.dogtags_image[1], anchor="nw", tag="grim")
        canvas.create_image(974, 250, image=self.dogtags_image[0], anchor="nw", tag="grim")
        canvas.create_text(1031, 303, text="["+self.player_data.player["tag"]+"]", font=("", 10,"bold"),
                           anchor="nw", fill="gray40", tag="grim",angle=-20)
        canvas.create_text(1027, 318, text= self.player_data.player["name"] , font=("", 10 ,"bold"),
                           anchor="nw", fill="gray40", tag="grim", angle=-20)

        canvas.create_text(310, 460, text="공로 스타", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(300, 482, image=self.contents_opacity2, anchor="nw", tag="grim")
        for i in range(5):
            canvas.create_image(320, 487 + (32 * i), image=self.icons_image[i], anchor="nw", tag="grim")
            canvas.create_image(373, 487 + (32 * i), image=self.service_gauge_bg, anchor="nw", tag="grim")
            canvas.create_image(376, 491+(32*i), image=self.service_gauge[i], anchor="nw", tag="grim")
            canvas.create_text(466, 492+(32*i), text="★ " + str(self.player_data.kits[self.kits_keys[i]]["stars"]), font=("", 11, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_text(642, 460, text="팀플레이", font=("", 12, "bold"), anchor="nw",fill="white smoke", tag="grim")
        canvas.create_image(632, 482, image=self.contents_opacity2_1, anchor="nw", tag="grim")
        canvas.create_arc(727, 509, 787, 569, start =90, extent = self.win,fill="DodgerBlue4",width=1,tag="grim")
        canvas.create_arc(727, 509, 787, 569, start=90+self.win, extent=-10+self.lose, fill="firebrick4",width=1,tag="grim")
        canvas.create_oval(742, 524, 772, 554, fill="black",tag="grim")
        canvas.create_image(757, 539, image=self.circle_image, tag="grim")
        canvas.create_text(803, 511, text="승리", font=("", 10, "bold"),anchor="nw", fill="gray", tag="grim")
        canvas.create_text(803, 526, text=str(self.win_percent)+"%",anchor="nw", font=("", 18, "bold"),fill="white smoke", tag="grim")
        canvas.create_image(632, 597, image=self.contents_opacity2_2, anchor="nw", tag="grim")
        canvas.create_text(798, 612, text="분대 점수", font=("", 10, "bold"), fill="gray", tag="grim")
        canvas.create_text(798, 634, text=format(self.player_data.stats['scores']["squad"], ','), font=("", 12, "bold"), fill="white smoke", tag="grim")

        canvas.create_text(974, 460, text="최고 순위표", font=("", 12, "bold"), anchor="nw",fill="white smoke", tag="grim")
        canvas.create_image(964, 482, image=self.contents_opacity2_3, anchor="nw", tag="grim")
        canvas.create_image(1089, 532, image=self.player_ranking1, tag="grim")
        canvas.create_text(984, 587, text=self.player_data.sort_ranking1["label"], font=("", 11, "bold"), anchor="nw",
                           fill="gray", tag="grim")
        canvas.create_text(984, 612, text=str(self.player_data.sort_ranking1["rank"])+"위 전 세계",
                           font=("", 16, "bold"), anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(1205, 482, image=self.contents_opacity2_4, anchor="nw", tag="grim")
        canvas.create_image(1250, 512, image=self.player_ranking2, tag="grim")
        canvas.create_text(1250, 551, text=str(self.player_data.sort_ranking2["rank"]) + " 위",
                           font=("", 11, "bold"),  fill="white smoke", tag="grim")
        canvas.create_image(1205, 568, image=self.contents_opacity2_4, anchor="nw", tag="grim")
        canvas.create_image(1250, 598, image=self.player_ranking3, tag="grim")
        canvas.create_text(1250, 637, text=str(self.player_data.sort_ranking3["rank"]) + " 위",
                           font=("", 11, "bold"), fill="white smoke", tag="grim")

        canvas.create_text(310, 681, text="최고 무기", font=("", 12, "bold"), anchor="nw",fill="white smoke", tag="grim")
        canvas.create_image(300, 703, image=self.contents_opacity3_1, anchor="nw", tag="grim")
        canvas.create_image(425, 743, image=self.rank1_weapon,  tag="grim")
        canvas.create_text(320, 785, text=self.player_data.rank_weapons[0]["name"], font=("", 10, "bold"), anchor="nw", fill="gray", tag="grim")
        canvas.create_text(320, 805, text=str(self.player_data.rank_weapons[0]["stat"]["kills"])+" 사살", font=("", 13, "bold"), anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(551, 703, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(591, 728, image=self.rank2_weapon, tag="grim")
        canvas.create_text(591, 758, text=str(self.player_data.rank_weapons[1]["stat"]["kills"]) + " 사살", font=("", 10, "bold"), fill="white smoke", tag="grim")
        canvas.create_image(551, 774, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(591, 799, image=self.rank3_weapon, tag="grim")
        canvas.create_text(591, 829, text=str(self.player_data.rank_weapons[2]["stat"]["kills"]) + " 사살",  font=("", 10, "bold"), fill="white smoke", tag="grim")

        canvas.create_text(642, 681, text="최고 탑승장비", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(632, 703, image=self.contents_opacity3_1, anchor="nw", tag="grim")
        canvas.create_image(757, 743, image=self.rank1_vehicle, tag="grim")
        canvas.create_text(652, 785, text=self.player_data.rank_vehicles[0]["name"], font=("", 10, "bold"), anchor="nw", fill="gray",tag="grim")
        canvas.create_text(652, 805, text=str(self.player_data.rank_vehicles[0]["stat"]["kills"]) + " 사살", font=("", 13, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(883, 703, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(923, 728, image=self.rank2_vehicle, tag="grim")
        canvas.create_text(923, 758, text=str(self.player_data.rank_vehicles[1]["stat"]["kills"]) + " 사살", font=("", 10, "bold"), fill="white smoke", tag="grim")
        canvas.create_image(883, 774, image=self.contents_opacity3_2, anchor="nw", tag="grim")
        canvas.create_image(923, 799, image=self.rank3_vehicle, tag="grim")
        canvas.create_text(923, 829, text=str(self.player_data.rank_vehicles[2]["stat"]["kills"]) + " 사살", font=("", 10, "bold"),fill="white smoke", tag="grim")

        canvas.create_text(974, 681, text="최고 게임 모드", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        canvas.create_image(964, 703, image=self.contents_opacity3, anchor="nw", tag="grim")
        for i in range(4):
            canvas.create_text(984, 713+(33*i), text=self.hangul_mode(self.player_data.rank_modes[i]) , font=("", 10, "bold"),anchor="nw",fill="gray", tag="grim")
            canvas.create_image(1119, 708+(32*i), image=self.gauge_bg, anchor="nw", tag="grim")
            canvas.create_image(1121, 712+(32*i), image=self.gauge[i], anchor="nw", tag="grim")
            canvas.create_text(1184, 713+(32*i), text="★ " + str(int(self.mode_star(self.player_data.rank_modes[i]))), font=("", 11, "bold"),anchor="nw", fill="white smoke",tag="grim")


