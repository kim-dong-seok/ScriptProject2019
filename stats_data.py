from tkinter import *
from PIL import Image, ImageTk


class stats_data:
    def __init__(self,player_data):
        self.player_data = player_data
        self.origin_contents_opacity = Image.open("내용배경.png")
        self.contents_opacity = ImageTk.PhotoImage(self.origin_contents_opacity.resize((315, 35)))
        self.orlgin_menu_bg = Image.open("메뉴배경.png")
        self.menu_bg = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((315, 25)))
        self.menus=["일반 통계","전투 통계","팀 점수","점수","추가","게임 모드" ]
        self.scores1 = ["플레이한 전투", "완료한 전투", "승리", "패배", "승리/패배 비율"]
        self.score_list1=[0]*5
        self.score_list1[0]= self.player_data.stats['numRounds']
        self.score_list1[1] = self.player_data.stats['numWins']+ self.player_data.stats['numLosses']
        self.score_list1[2] = self.player_data.stats['numWins']
        self.score_list1[3] = self.player_data.stats['numLosses']
        self.score_list1[4] = self.player_data.stats["extra"]["wlr"]

        self.scores2 = ["돌격병 점수", "공병 점수", "보급병 점수", "정찰병 점수", "지휘관 점수",
                        "분대 점수", "탑승장비 점수", "포상 점수", "잠김 해제 점수", "총 점수","분당 점수"]
        self.score_list2_keys=["squad","vehicle","award","unlock","totalScore"]
        self.score_list2 = [0] * 11
        self.kits_keys = list(self.player_data.kits.keys())
        for i in range(5):
            self.score_list2[i]=self.player_data.kits[ self.kits_keys[i]]["score"]
            self.score_list2[5+i] = self.player_data.stats["scores"][ self.score_list2_keys[i]]
        self.score_list2[10]=self.player_data.stats["extra"]["spm"]

        self.scores3 = ["사살", "사망", "사살 도움", "K/D 비율", "분당 사살","발사한 탄", "몇중한 탄", "명중률"]
        self.score_list3 = [0] * 8
        self.score_list3_keys = ["kills", "deaths", "killAssists","shotsFired","shotsHit"]
        for i in range(3):
            self.score_list3[i]=self.player_data.stats[ self.score_list3_keys[i]]
        self.score_list3[3] = self.player_data.stats["extra"]["kdr"]
        self.score_list3[4] = self.player_data.stats["extra"]["kpm"]
        self.score_list3[5] = self.player_data.stats[self.score_list3_keys[3]]
        self.score_list3[6] = self.player_data.stats[self.score_list3_keys[4]]
        self.score_list3[7] = self.player_data.stats["extra"]["accuracy"]

        self.scores4 = ["수리", "소생", "치료", "재보급", "보복 사살","구원","제압 도움"]
        self.score_list4 = [0] * 7
        self.score_list4_keys = ["repairs", "revives", "heals", "resupplies", "avengerKills","saviorKills","suppressionAssists"]
        for i in range(7):
            self.score_list4[i] = self.player_data.stats[self.score_list4_keys[i]]

        self.scores5 = ["컨퀘스트", "러시", "데스매치", "도미네이션", "깃발 잡기", "오블리터레이션","제공권", "디퓨즈",
                         "대형 캐리어 어설트", "캐리어 어설트", "체인 링크"]
        self.score_list5=[]
        for i in self.player_data.modes:
            self.score_list5.append(i["score"])
        del self.score_list5[8]

        self.scores6 = ["획득한 인식표", "장비 파괴", "장비 대미지", "헤드샷", "최장거리 헤드샷", "최고 연속 사살", "숙적 사살","최고 연속 희생양 사살"]
        self.score_list6 = [0] * 8
        self.score_list6_keys = ["dogtagsTaken", "vehiclesDestroyed", "vehicleDamage", "headshots", "longestHeadshot", "killStreakBonus", "nemesisKills","nemesisStreak"]
        for i in range(8):
            self.score_list6[i] = self.player_data.stats[self.score_list6_keys[i]]
    def draw(self,canvas):
        for j in range(3):
            canvas.create_image(300+(j*340), 214, image=self.menu_bg, anchor="nw", tag="grim")
            canvas.create_text(310 + (j * 340), 217, text=self.menus[j], font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        for i in range(5):
            canvas.create_image(300 , 240+(i*36), image=self.contents_opacity, anchor="nw", tag="grim")
            canvas.create_text(310 , 247+(i*36), text=self.scores1[i], font=("", 12, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
        for i in range(4):
            canvas.create_text(605, 247 + (i * 36), text=format(self.score_list1[i], ","), font=("", 12, "bold"),
                               anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(605, 391, text=format(self.score_list1[4], ".3f"), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")

        canvas.create_image(300 , 430, image=self.menu_bg, anchor="nw", tag="grim")
        canvas.create_text(310 , 433, text=self.menus[3], font=("", 12, "bold"), anchor="nw",
                           fill="white smoke", tag="grim")
        for i in range(11):
            canvas.create_image(300 , 456+(i*36), image=self.contents_opacity, anchor="nw", tag="grim")
            canvas.create_text(310 , 463+(i*36), text=self.scores2[i], font=("", 12, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
        for i in range(9):
            canvas.create_text(605, 463 + (i * 36), text=format(self.score_list2[i], ","), font=("", 12, "bold"),
                               anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(605, 463 + (9 * 36), text="= "+format(self.score_list2[9], ","), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(605, 463 + (10 * 36), text=format(self.score_list2[10], ".0f"), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")

        for i in range(8):
            canvas.create_image(640 , 240+(i*36), image=self.contents_opacity, anchor="nw", tag="grim")
            canvas.create_text(650 , 247+(i*36), text=self.scores3[i], font=("", 12, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
        for i in range(3):
            canvas.create_text(945, 247 + (i * 36), text=format(self.score_list3[i], ","), font=("", 12, "bold"),
                               anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(945, 247 + (3 * 36), text=format(self.score_list3[3], ".2f"), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(945, 247 + (4 * 36), text=format(self.score_list3[4], ".2f"), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(945, 247 + (5 * 36), text=format(self.score_list3[5], ","), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(945, 247 + (6 * 36), text=format(self.score_list3[6], ","), font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")
        canvas.create_text(945, 247 + (7 * 36), text=format(self.score_list3[7], ".2f")+" %", font=("", 12, "bold"),
                           anchor="ne", fill="white smoke", tag="grim")

        for i in range(7):
            canvas.create_image(980 , 240+(i*36), image=self.contents_opacity, anchor="nw", tag="grim")
            canvas.create_text(990 , 247+(i*36), text=self.scores4[i], font=("", 12, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
            canvas.create_text(1285, 247 + (i * 36), text=format(self.score_list4[i],","), font=("", 12, "bold"), anchor="ne",
                               fill="white smoke",tag="grim")

        canvas.create_image(980, 502, image=self.menu_bg, anchor="nw", tag="grim")
        canvas.create_text(990, 505, text=self.menus[5], font=("", 12, "bold"), anchor="nw",
                           fill="white smoke", tag="grim")
        for i in range(10):
            canvas.create_image(980 , 528+(i*36), image=self.contents_opacity, anchor="nw", tag="grim")
            canvas.create_text(990 , 535+(i*36), text=self.scores5[i], font=("", 12, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
            canvas.create_text(1285, 535 + (i * 36), text=format(self.score_list5[i],","), font=("", 12, "bold"), anchor="ne",
                               fill="white smoke",tag="grim")

        canvas.create_image(640, 545, image=self.menu_bg, anchor="nw", tag="grim")
        canvas.create_text(650, 548, text=self.menus[4], font=("", 12, "bold"), anchor="nw",
                           fill="white smoke", tag="grim")

        for i in range(8):
            canvas.create_image(640 , 571+(i*36), image=self.contents_opacity, anchor="nw", tag="grim")
            canvas.create_text(650 , 578+(i*36), text=self.scores6[i], font=("", 12, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
            canvas.create_text(940, 578 + (i * 36), text=format(self.score_list6[i],","), font=("", 12, "bold"), anchor="ne",
                               fill="white smoke",tag="grim")