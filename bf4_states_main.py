import tkinter.ttk
import cv2
from PIL import ImageGrab
from stats_data import*
from player_data import*
from player_main import*
from start_page import*
from weapons_page import*
from vehicle_page import*
from rank_page import*
from bf4_gmail import *

class bf4_main:
    def __init__(self):
        self.window = Tk()
        self.window.title("ui_image/bf4.gg")
        self.window.geometry("1600x900+100+50")
        self.video_source = "bg-video/bg-video.mp4"
        self.vid = MyVideoCapture(self.video_source)
        self.width=1600
        self.height=900
        self.iscapture=0
        self.isdrag=0
        self.up=0
        self.x=0
        self.y=0
        self.ox=0
        self.oy=0
        self.nx=0
        self.ny=0
        self.bx=0
        self.by=0
        self.player_data=''
        self.player_name = " "
        self.scene=0
        self.b1ck=0
        self.bcheck=-1
        self.canvas = Canvas(self.window,  width=self.width, height=self.height)
        self.canvas.pack()
        originimage2 = Image.open("ui_image/bf4.gg.png")
        self.logoImage = ImageTk.PhotoImage(originimage2.resize((160, 32)))
        orlgin_logo_bg=Image.open("ui_image/로고배경.png")
        self.logo_bg = ImageTk.PhotoImage(orlgin_logo_bg.resize((1600, 45)))
        orlgin_search_bg = Image.open("ui_image/검색배경.png")
        self.search_bg = ImageTk.PhotoImage(orlgin_search_bg.resize((1600, 45)))
        orlgin_name_bg = Image.open("ui_image/내용배경.png")
        self.name_bg = ImageTk.PhotoImage(orlgin_name_bg.resize((350, 45)))
        orlgin_gmail= Image.open("ui_image/gmail.png")
        gmail_image = ImageTk.PhotoImage( orlgin_gmail.resize((20, 20)))
        orlgin_capture = Image.open("ui_image/캡쳐.png")
        capture_image = ImageTk.PhotoImage(orlgin_capture.resize((20, 20)))
        orlgin_save = Image.open("ui_image/저장.png")
        save_image = ImageTk.PhotoImage(orlgin_save.resize((20, 20)))
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
        self.e2 = Entry(self.canvas, font=("", 16,), width=15)
        self.e2.insert(0, "Player name")
        self.c2 = tkinter.ttk.Combobox(self.canvas, textvariable=self.str, width=7, font=("", 15))
        self.c2["values"]=("pc", "ps4", "xone", "ps3", "xbox")
        self.c2.set("Platform")
        self.b2 = Button(self.canvas, text="Search", font=("", 10, "bold"), command=self.search,
                         width=7)
        self.b3 = Button(self.canvas, text="Home", font=("", 10, "bold"), command=self.home,
                         width=6)
        self.b4 = Button(self.canvas, image=capture_image, text=" Capture", font=("", 10, "bold"), compound="left",
                         command=self.capture_state,width=90)
        self.b5 = Button(self.canvas, image=save_image, text=" Save", font=("", 10, "bold"), compound="left",
                         command=self.capture,width=70)
        self.b6 = Button(self.canvas, image=gmail_image, text=" Send Email", font=("", 10, "bold"),compound="left",
                         command=self.gmail,width=115)
        self.menu_buttons = [menu_button(300+(i*199),165) for i in range(5)]
        self.menu_buttons[0].btext="개요"
        self.menu_buttons[1].btext ="통계"
        self.menu_buttons[2].btext = "무기"
        self.menu_buttons[3].btext = "탑승장비"
        self.menu_buttons[4].btext = "랭킹"
        self.menu_buttons[0].ckeck=2
        self.start_page = start_page()
        self.window.bind('<MouseWheel>', self.wheel)
        self.window.bind('<Motion>', self.motion)
        self.delay = 10
        self.update()
        self.window.mainloop()

    def send(self):
        send_email(self.ge1.get())
    def gmail(self):
        self.t=tkinter.Toplevel(self.window)
        self.t.geometry("330x200+800+100")
        self.t.title("Send Email")
        gl1 = Label(self.t, text="캡처한 이미지를 이메일로 전송합니다.")
        gl1.pack()
        gl2 = Label(self.t, text="전송할 이메일 주소")
        gl2.pack()
        self.ge1=Entry(self.t)
        self.ge1.pack()
        gb1 = Button(self.t,text="전송",command=self.send())
        gb1.pack()

    def home(self):
        self.scene = 0
        self.e2.place_forget()
        self.c2.place_forget()
        self.b2.place_forget()
        self.b3.place_forget()
        self.b4.place_forget()
        self.b5.place_forget()
        self.b6.place_forget()
        self.e1.insert(0, "Player name")
        self.e1.place(x=500, y=400)
        self.b1.place(x=1100, y=400, anchor="ne")
        self.c1.place(x=835, y=400)


    def capture_state(self):

            if self.iscapture==0:
                self.iscapture=1
            else:
                self.iscapture=0
            self.nx=0
            self.ny=0
            self.ox=0
            self.oy=0

    def parsegeometry(self,geometry):
        m = re.match("(\d+)x(\d+)([-+]\d+)([-+]\d+)", geometry)
        if not m:
            raise ValueError("failed to parse geometry string")
        return list(map(int, m.groups()))
    def capture(self):
        position=self.parsegeometry(self.window.geometry())
        print(self.window.geometry())
        print("ox={0} oy={1} nx={2} ny={3}".format(self.ox+position[2]+9, self.oy+position[3]+32, self.nx+position[2]+8, self.ny+position[3]+30))
        img = ImageGrab.grab(bbox=(self.ox+position[2]+9, self.oy+position[3]+32, self.nx+position[2]+8, self.ny+position[3]+30))
        img.save("screenImage1.jpg")
        self.iscapture = 0
    def capture_mode(self):


        self.window.bind('<Button-1>', self.drag)
        self.window.bind('<B1-Motion>', self.drag_move)
        self.window.bind('<ButtonRelease-1>', self.drag_up)
        print("ox={0} oy={1} nx={2} ny={3} x={4} y={5} is={6}".format(self.ox,self.oy,self.nx,self.ny,self.x,self.y,self.iscapture))

        self.window.bind('<Return>', self.capture)



    def drag(self, event):
        self.x=event.x
        self.y=event.y
        if self.x > 80 or self.x < 0 or self.y > 30 or self.y < 0:
            if self.isdrag==0:
                print(self.window.geometry())
                self.nx = 0
                self.ny = 0
                self.ox = 0
                self.oy = 0
                self.ox, self.oy = event.x, event.y
                self.nx, self.ny = event.x, event.y
                self.isdrag=1

    def drag_move(self, event):
        self.nx, self.ny = event.x, event.y
    def drag_up(self,event):
        if self.isdrag == 1:
            self.isdrag = 0
    def wheel(self,event):
        if self.iscapture == 0:
            if self.scene == 3:
                if self.weapon_page.count >= 0 and self.weapon_page.count <= 166:
                    if event.delta == -120:
                        self.up = 1
                    if event.delta == 120:
                        self.up = -1

                    self.weapon_page.count+=self.up
                    if self.weapon_page.count<0:
                        self.weapon_page.count=0
                    elif self.weapon_page.count>166:
                        self.weapon_page.count=166

            if self.scene == 4:
                if self.vehicle_page.count >= 0 and self.vehicle_page.count <= 70:
                    if event.delta == -120:
                        self.up = 1
                    if event.delta == 120:
                         self.up = -1

                    self.vehicle_page.count += self.up
                    if self.vehicle_page.count < 0:
                        self.vehicle_page.count = 0
                    elif self.vehicle_page.count > 70:
                         self.vehicle_page.count = 70

    def search(self):
        if self.scene==0:
            self.player_name = self.e1.get()
            self.scene=1
            self.e1.place_forget()
            self.b1.place_forget()
            self.c1.place_forget()
            self.player_data=player_data( self.player_name, self.c1.get())
            self. player_main=player_main(self.player_data)
            self.stats_data = stats_data(self.player_data)
            self.weapon_page = weapon_page(self.player_data)
            self.vehicle_page = Vehicle_page(self.player_data)
            self.rank_page = rank_page(self.player_data)
            self.c2.set("Platform")
            self.e2.place(x=300, y=self.height / 16)
            self.c2.place(x=477, y=self.height / 16)
            self.b2.place(x=585, y=self.height / 16)
            self.b3.place(x=659, y=self.height / 16)
            self.b4.place(x=1075, y=55, anchor="ne")
            self.b5.place(x=1160, y=55, anchor="ne")
            self.b6.place(x=1290, y=55,anchor="ne")
        else:
            self.player_name = self.e2.get()
            self.scene = 1
            self.player_data = player_data(self.player_name, self.c2.get())
            self.player_main = player_main(self.player_data)
            self.stats_data = stats_data(self.player_data)
            self.weapon_page = weapon_page(self.player_data)
            self.vehicle_page = Vehicle_page(self.player_data)
            self.rank_page = rank_page(self.player_data)
            self.c2.set("Platform")
    def click(self,event):
        if self.iscapture == 0:
            if self.menu_buttons[self.bcheck].ckeck==1:
                for i in range(5):
                    if self.menu_buttons[i].ckeck == 2:
                        self.menu_buttons[i].ckeck = 0
                self.menu_buttons[self.bcheck].ckeck = 2
                self.scene=self.bcheck+1
                if self.scene==1:
                    self.player_main = player_main(self.player_data)

    def Contents_click(self, event):

        for i in range(5):
            if self.menu_buttons[i].ckeck == 2:
                self.menu_buttons[i].ckeck = 0
        if self.player_main.mouse_count - 1<=5:
            self.menu_buttons[self.player_main.mouse_count].ckeck = 2
            self.scene = self.player_main.mouse_count + 1
    def motion(self,event):
        if self.iscapture == 0:
            if self.scene!=0:
                self.x,self.y=event.x,event.y
                self.mause_update()

    def mause_update(self):

        if self.scene!=0:
            for i in range(5):
                if self.menu_buttons[i].ckeck == 1:
                    self.bcheck = i
                    self.window.bind('<Button-1>', self.click)
                self.menu_buttons[i].update(self.x, self.y)
        if self.scene==1:
            for i in range(1,10):
                if self.player_main.mouse_count == i:
                    self.window.bind('<Button-1>', self.Contents_click)

        if self.scene==3:
            for i in range(1, 11):
                if self.weapon_page.mouse_count == i:
                    self.window.bind('<Button-1>', self.weapon_page.sort)
        if self.scene==4:
            for i in range(1,6):
                if self.vehicle_page.mouse_count == i:
                    self.window.bind('<Button-1>', self.vehicle_page.sort)
    def update(self):
        ret, frame = self.vid.get_frame()
        if self.iscapture==1:
            self.capture_mode()

        if ret:
            self.canvas.delete("grim")
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame).resize((1600, 900)))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW,tag="grim")
            if self.iscapture == 0:
                if self.scene == 1:
                    self.player_main.update(self.x,self.y)
                elif self.scene == 3:
                    self.weapon_page.update(self.x,self.y)
                elif self.scene == 4:
                    self.vehicle_page.update(self.x,self.y)
        self.draw()
        self.window.after(self.delay, self.update)
    def draw(self):
        if self.scene==0:
            self.start_page.draw(self.canvas)
        else:
            self.canvas.create_image(self.width / 2,self.height/40 , image=self.logo_bg,tag="grim")
            self.canvas.create_image(self.width / 2, self.height / 13, image=self.search_bg,tag="grim")
            self.canvas.create_image(300, 10, image=self.logoImage,anchor="nw",tag="grim")
            self.canvas.create_image(300, 108, image=self.name_bg,anchor="nw",tag="grim")
            self.canvas.create_text(320,115, text=self.player_data.player["plat"].upper(),
                                    font=("", 20,"bold"), fill="white smoke", tag="grim",anchor="nw")
            self.canvas.create_text(420,115, text="["+self.player_data.player["tag"]+"]",
                                    font=("", 20, "bold"), fill="white smoke", tag="grim",anchor="nw")
            self.canvas.create_text(510,115, text=self.player_data.player["name"],
                                    font=("", 20, "bold"), fill="white smoke", tag="grim",anchor="nw")
            for menu_button in self.menu_buttons:
                menu_button.draw(self.canvas)
            if self.scene==1:
                self.player_main.draw(self.canvas)
            elif self.scene==2:
                self.stats_data.draw(self.canvas)
            elif self.scene==3:
                self.weapon_page.draw(self.canvas)
            elif self.scene==4:
                self.vehicle_page.draw(self.canvas)
            elif self.scene==5:
                self.rank_page.draw(self.canvas)

        if self.iscapture==1:
            self.canvas.create_rectangle(self.ox, self.oy, self.nx, self.ny, outline="red")
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
            self.orlgin_menu_bg = Image.open("ui_image/메뉴배경.png")
        self.menu_bg = ImageTk.PhotoImage(self.orlgin_menu_bg.resize((198, 35)))
        if menu_button.orlgin_gradient_bg == None:
            self.orlgin_gradient_bg = Image.open("ui_image/그라데이션.png")
        self.gradient_bg = ImageTk.PhotoImage(self.orlgin_gradient_bg.resize((198, 35)))
        if menu_button.orlgin_click__bg == None:
            self.orlgin_click_bg = Image.open("ui_image/클릭시.png")
        self.click_bg = ImageTk.PhotoImage(self.orlgin_click_bg.resize((198, 35)))

    def update(self,x,y):

        if x > self.bx and x < self.bx+198 and y > self.by and y < self.by+35:
            if self.ckeck != 2:
                self.ckeck = 1
        else:
            if self.ckeck != 2:
                self.ckeck=0

    def draw(self,canvas):
        if self.ckeck==0:
            canvas.create_image(self.bx, self.by, image=self.menu_bg, anchor="nw",tag="grim")
            canvas.create_text(self.bx+97,self.by+18, text=self.btext, font=("", 14, "bold"), fill="white smoke", tag="grim")
        if self.ckeck==1:
            canvas.create_image(self.bx, self.by, image=self.gradient_bg, anchor="nw",tag="grim")
            canvas.create_text(self.bx+97,self.by+18, text=self.btext, font=("", 14, "bold"), fill="white smoke", tag="grim")
        if self.ckeck==2:
            canvas.create_image(self.bx, self.by, image=self.click_bg, anchor="nw",tag="grim")
            canvas.create_text(self.bx+97,self.by+18, text=self.btext, font=("", 14, "bold"), fill="black", tag="grim")

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