
from tkinter import *
from PIL import Image, ImageTk
import tkinter.ttk




class rank_page:
    def __init__(self,player_data):
        self.ranking1=player_data.ranking1
        self.ranking2 = player_data.ranking2
        self.ranking3 = player_data.ranking3
        self.ranking4 = player_data.ranking4
        self.ranking1_image=[]
        self.ranking2_image = []
        self.ranking3_image = []
        self.ranking4_image = []
        for i in range(len(self.ranking1)-1):
            if self.ranking1[i]["ident"]=="streak":
                del self.ranking1[i]
        for i in self.ranking1:
            self.orlgin_menu_bg = Image.open(("bf4/lbicons/{0}.png").format(i["ident"]))
            self.ranking1_image.append(ImageTk.PhotoImage(self.orlgin_menu_bg.resize((30, 30))))
        for i in self.ranking2:
            self.orlgin_menu_bg = Image.open(("bf4/lbicons/{0}.png").format(i["ident"]))
            self.ranking2_image.append(ImageTk.PhotoImage(self.orlgin_menu_bg.resize((30, 30))))
        for i in self.ranking3:
            self.orlgin_menu_bg = Image.open(("bf4/lbicons/{0}.png").format(i["ident"]))
            self.ranking3_image.append(ImageTk.PhotoImage(self.orlgin_menu_bg.resize((30, 30))))
        for i in self.ranking4:
            self.orlgin_menu_bg = Image.open(("bf4/kititems_lineart/{0}.png").format(i["ident"]))
            self.ranking4_image.append(ImageTk.PhotoImage(self.orlgin_menu_bg.resize((30, 30))))

        self.cantents1 = ["점수", "스킬", "사살/사망 비율", "승리/패배 비율",
                              "분당 점수", "분당 사살", "분당 기본 점수", "헤드샷/처치 비율", "처치/명중 비율",
                          "분당 발사한 탄", "인식표", "헤드샷", "사살 도움", "제압 도움",
                          "참여한 전투", "최장거리 헤드샷", "방어한 깃발", "점령한 깃발", "장비 파괴",
                          "장비 데미지","전투당 리본"]
        self.cantents2=["돌격병 점수","공병 점수","보급병 점수","정찰병 점수","지휘관 점수"]
        self.cantents3 = ["컨퀘스트", "러시", "데스매치", "도미네이션","깃발 잡기" ,"오블리터레이션",
                          "제공권", "디퓨즈","캐리어 어설트(대형)", "캐리어 어설트", "체인 링크"]
        self.cantents4 = ["수리 도구", "제세동기", "구급상자", "무선 신호기", "T-UGS", "SOFLAM",
                          "MAV", "탄약상자", "MP_APS"]

        self.orlgin_menu_bg = Image.open("ui_image/메뉴배경.png")
        self.menu_bg1 = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((1000, 25)))

        self.origin_contents_opacity = Image.open("ui_image/내용배경.png")
        self.contents_opacity1 = ImageTk.PhotoImage(self.origin_contents_opacity.resize((199, 48)))


    def draw(self,canvas):
        canvas.create_image(300, 214, image=self.menu_bg1, anchor="nw", tag="grim")
        canvas.create_text(320, 217, text="플레이어 순위", font=("", 12, "bold"),anchor="nw", fill="white smoke", tag="grim")
        for j in range(4):
            for i in range(5):
                canvas.create_image(300+(i*200), 240+(j*49), image=self.contents_opacity1, anchor="nw", tag="grim")
                canvas.create_image(305+(i*200), 249+(j*49), image=self.ranking1_image[i+(j*5)], anchor="nw", tag="grim")
                canvas.create_text(340+(i*200), 244+(j*49), text=self.cantents1[i+(j*5)],
                                   font=("", 10, "bold"), anchor="nw", fill="white smoke",
                                   tag="grim")
                if self.ranking1[i + (j * 5)]["value"] >= 1000:
                    canvas.create_text(494 + (i * 200), 244 + (j * 49), text="{0:,}".format(self.ranking1[i + (j * 5)]["value"]),
                                       font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                       tag="grim")
                else:
                    canvas.create_text(494 + (i * 200), 244 + (j * 49), text="{0:.2f}".format(self.ranking1[i + (j * 5)]["value"]),
                                    font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                    tag="grim")
                canvas.create_text(340 + (i * 200), 269 + (j * 49), text="{0}명 중 {1}위".format(self.ranking1[i + (j * 5)]["count"],self.ranking1[i + (j * 5)]["rank"]),
                                   font=("", 10, "bold"), anchor="nw", fill="gray",
                                   tag="grim")
        canvas.create_image(300 , 240 + (4 * 49), image=self.contents_opacity1, anchor="nw", tag="grim")
        canvas.create_image(305 , 249 + (4 * 49), image=self.ranking1_image[20], anchor="nw",
                            tag="grim")
        canvas.create_text(340 , 244 + (4 * 49), text=self.cantents1[20],
                           font=("", 10, "bold"), anchor="nw", fill="white smoke",
                           tag="grim")

        canvas.create_text(494 , 244 + (4 * 49), text="{0:.2f}".format(self.ranking1[20]["value"]),
                                font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                tag="grim")
        canvas.create_text(340 , 269 + (4 * 49),
                           text="{0}명 중 {1}위".format(self.ranking1[20]["count"],
                                                     self.ranking1[20]["rank"]),
                           font=("", 10, "bold"), anchor="nw", fill="gray",
                           tag="grim")


        canvas.create_image(300, 485, image=self.menu_bg1, anchor="nw", tag="grim")
        canvas.create_text(320, 488, text="병과 순위", font=("", 12, "bold"), anchor="nw", fill="white smoke", tag="grim")
        for i in range(5):
            canvas.create_image(300 + (i * 200), 511 , image=self.contents_opacity1, anchor="nw", tag="grim")
            canvas.create_image(305 + (i * 200), 520 , image=self.ranking2_image[i ], anchor="nw",
                                tag="grim")
            canvas.create_text(340 + (i * 200), 515 , text=self.cantents2[i ],
                               font=("", 10, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
            canvas.create_text(494 + (i * 200), 515 ,
                               text="{0:,}".format(self.ranking2[i]["value"]),
                               font=("", 10, "bold"), anchor="ne", fill="white smoke",
                               tag="grim")
            canvas.create_text(340 + (i * 200), 540 ,
                               text="{0}명 중 {1}위".format(self.ranking2[i]["count"],
                                                         self.ranking2[i ]["rank"]),
                               font=("", 10, "bold"), anchor="nw", fill="gray",
                               tag="grim")

        canvas.create_image(300, 560, image=self.menu_bg1, anchor="nw", tag="grim")
        canvas.create_text(320, 563, text="게임 모드 순위", font=("", 12, "bold"), anchor="nw", fill="white smoke", tag="grim")
        for j in range(2):
            for i in range(5):
                canvas.create_image(300+(i*200), 586+(j*49), image=self.contents_opacity1, anchor="nw", tag="grim")
                canvas.create_image(305 + (i * 200), 595 + (j * 49), image=self.ranking3_image[i + (j * 5)], anchor="nw",
                                    tag="grim")
                canvas.create_text(340 + (i * 200), 590 + (j * 49), text=self.cantents3[i + (j * 5)],
                                   font=("", 10, "bold"), anchor="nw", fill="white smoke",
                                   tag="grim")
                if self.ranking3[i + (j * 5)]["value"]==None:
                    canvas.create_text(494 + (i * 200), 590 + (j * 49),
                                       text="None",
                                       font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                       tag="grim")
                else:
                    canvas.create_text(494 + (i * 200), 590 + (j * 49),
                                       text="{0:,}".format(self.ranking3[i + (j * 5)]["value"]),
                                       font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                       tag="grim")
                canvas.create_text(340 + (i * 200), 615 + (j * 49),
                                text="{0}명 중 {1}위".format(self.ranking3[i + (j * 5)]["count"],
                                                             self.ranking3[i + (j * 5)]["rank"]),
                                font=("", 10, "bold"), anchor="nw", fill="gray",
                                tag="grim")

        canvas.create_image(300 , 586 + (2 * 49), image=self.contents_opacity1, anchor="nw", tag="grim")
        canvas.create_image(305 , 595 + (2 * 49), image=self.ranking3_image[10], anchor="nw",
                            tag="grim")
        canvas.create_text(340 , 590 + (2 * 49), text=self.cantents3[10],
                           font=("", 10, "bold") , anchor="nw", fill="white smoke",
                           tag="grim")
        canvas.create_text(494 , 590 + (2 * 49),
                           text="{0:,}".format(self.ranking3[10]["value"]),
                           font=("", 10, "bold"), anchor="ne", fill="white smoke",
                           tag="grim")
        canvas.create_text(340 , 615 + (2 * 49),
                           text="{0}명 중 {1}위".format(self.ranking3[10]["count"],
                                                     self.ranking3[10]["rank"]),
                           font=("", 10, "bold"), anchor="nw", fill="gray",
                           tag="grim")


        canvas.create_image(300, 733, image=self.menu_bg1, anchor="nw", tag="grim")
        canvas.create_text(320, 736, text="병과 키트 순위", font=("", 12, "bold"), anchor="nw", fill="white smoke", tag="grim")
        for i in range(5):
            canvas.create_image(300 + (i * 200), 759 , image=self.contents_opacity1, anchor="nw",
                                    tag="grim")
            canvas.create_image(305 + (i * 200), 768 , image=self.ranking4_image[i ], anchor="nw",
                                tag="grim")
            canvas.create_text(340 + (i * 200), 763 , text=self.cantents4[i ],
                               font=("", 10, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
            if self.ranking4[i ]["value"] == None:
                canvas.create_text(494 + (i * 200), 763 ,
                                   text="None",
                                   font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                   tag="grim")
            else:
                canvas.create_text(494 + (i * 200), 763 ,
                                   text="{0:,}".format(self.ranking4[i ]["value"]),
                                   font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                   tag="grim")
            canvas.create_text(340 + (i * 200), 788 ,
                               text="{0}명 중 {1}위".format(self.ranking4[i ]["count"],
                                                         self.ranking4[i]["rank"]),
                               font=("", 10, "bold"), anchor="nw", fill="gray",
                               tag="grim")
        for i in range(4):
            canvas.create_image(300 + (i * 200), 808, image=self.contents_opacity1, anchor="nw",
                                    tag="grim")
            canvas.create_image(305 + (i * 200), 768 + ( 49), image=self.ranking4_image[i + ( 5)], anchor="nw",
                                tag="grim")
            canvas.create_text(340 + (i * 200), 763 + ( 49), text=self.cantents4[i + ( 5)],
                               font=("", 10, "bold"), anchor="nw", fill="white smoke",
                               tag="grim")
            if self.ranking4[i + ( 5)]["value"] == None:
                canvas.create_text(494 + (i * 200), 763 + ( 49),
                                   text="None",
                                   font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                   tag="grim")
            else:
                canvas.create_text(494 + (i * 200), 763 + ( 49),
                                   text="{0:,}".format(self.ranking4[i + ( 5)]["value"]),
                                   font=("", 10, "bold"), anchor="ne", fill="white smoke",
                                   tag="grim")
            canvas.create_text(340 + (i * 200), 788 + ( 49),
                               text="{0}명 중 {1}위".format(self.ranking4[i + ( 5)]["count"],
                                                         self.ranking4[i + ( 5)]["rank"]),
                               font=("", 10, "bold"), anchor="nw", fill="gray",
                               tag="grim")
