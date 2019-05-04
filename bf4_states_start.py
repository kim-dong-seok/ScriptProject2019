import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter.ttk

online=requests.get("https://api.bf4stats.com/api/onlinePlayers?output=json").json()

online_pc=online["pc"]
online_ps4=online["ps4"]
online_ps3=online["ps3"]
online_xone=online["xone"]
online_xbox=online["xbox"]
online_total=online_pc["count"]+online_ps4["count"]+online_ps3["count"]+online_xbox["count"]+online_xone["count"]
class App2:
    def __init__(self, window, window_title, video_source=0):
        self.window = window
        self.window.title(window_title)
        self.video_source = video_source
        self.originimage1 = Image.open("image/ranks/r140.png").resize((100, 100))
        self.rankImage = ImageTk.PhotoImage(self.originimage1)
        self.originimage2 = Image.open("Battlefield_4_logo.png").resize((400, 80))
        self.logoImage = ImageTk.PhotoImage(self.originimage2)
        self.orlginOpacity = Image.open("opacity.png")
        self.opacityImage = ImageTk.PhotoImage(self.orlginOpacity.resize((500, 200)))
        self.count=0
        # open video source (by default this will try to open the computer webcam)
        self.vid = MyVideoCapture(self.video_source)
        # Create a canvas that can fit the above video source size
        self.canvas = Canvas(window, width = 800, height = 600)
        self.canvas.pack()
        self.e1 = Entry(self.canvas,font=("",12),width = 30)
        self.e1.insert(0,"Player name")
        self.e1.place(x=200, y=250)
        self.b1 = Button(self.canvas,  text="검색",font=("",10), command=self.search,highlightbackground="black",width = 6, height = 1)
        self.b1.place(x=550, y=250)
        self.values = ["PC","PS4","XBOXONE","PS3","XBOX360"]
        self.c1 = tkinter.ttk.Combobox(self.canvas, values=self.values,width=9,font=("",12))
        self.c1.set("플랫폼")
        self.c1.place(x=450, y=250)
        # After it is called once, the update method will be automatically called every delay milliseconds
        self.delay = 15
        self.update()
        self.window.mainloop()
    def fpage(self):
        self.canvas.create_image(0, 0, image = self.photo, anchor = NW)
    def search(self):
        pass
    def update(self):
        # Get a frame from the video source
        startTime = time.time()
        ret, frame = self.vid.get_frame()

        if ret:
            self.canvas.delete("grim")
            self.photo = ImageTk.PhotoImage(image = Image.fromarray(frame).resize((800, 600)))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW,tag="grim")
            self.canvas.create_image(400, 400, image=self.opacityImage,tag="grim")
            self.canvas.create_image(400, 180, image=self.logoImage,tag="grim")
            self.canvas.create_text(400,340,text="현재 온라인 플레이어(총"+str(online_total)+"명)",font=("",12),fill="ghost white",tag="grim")
            self.canvas.create_text(200, 370, text=online_pc["label"], font=("",12),fill="ghost white",tag="grim")
            self.canvas.create_text(300, 370, text=online_ps4["label"], font=("",12), fill="ghost white",tag="grim")
            self.canvas.create_text(400, 370, text=online_xone["label"], font=("",12), fill="ghost white",tag="grim")
            self.canvas.create_text(500, 370, text=online_ps3["label"], font=("",12), fill="ghost white",tag="grim")
            self.canvas.create_text(600, 370, text=online_xbox["label"], font=("",12), fill="ghost white",tag="grim")

            self.canvas.create_text(200, 400, text=online_pc["count"], font=("",15,"bold"), fill="ghost white",tag="grim")
            self.canvas.create_text(300, 400, text=online_ps4["count"], font=("",15,"bold"), fill="ghost white",tag="grim")
            self.canvas.create_text(400, 400, text=online_xone["count"], font=("",15,"bold"), fill="ghost white",tag="grim")
            self.canvas.create_text(500, 400, text=online_ps3["count"], font=("",15,"bold"), fill="ghost white",tag="grim")
            self.canvas.create_text(600, 400, text=online_xbox["count"], font=("",15,"bold"), fill="ghost white",tag="grim")

            self.canvas.create_text(200, 430, text="최다 접속", font=("", 10), fill="ghost white",tag="grim")
            self.canvas.create_text(300, 430, text="최다 접속", font=("", 10), fill="ghost white",tag="grim")
            self.canvas.create_text(400, 430, text="최다 접속", font=("", 10), fill="ghost white",tag="grim")
            self.canvas.create_text(500, 430, text="최다 접속", font=("", 10), fill="ghost white",tag="grim")
            self.canvas.create_text(600, 430, text="최다 접속", font=("", 10), fill="ghost white",tag="grim")

            self.canvas.create_text(200, 450, text=online_pc["peak24"], font=("", 12), fill="ghost white",tag="grim")
            self.canvas.create_text(300, 450, text=online_ps4["peak24"], font=("", 12), fill="ghost white",tag="grim")
            self.canvas.create_text(400, 450, text=online_xone["peak24"], font=("", 12), fill="ghost white",tag="grim")
            self.canvas.create_text(500, 450, text=online_ps3["peak24"], font=("", 12), fill="ghost white",tag="grim")
            self.canvas.create_text(600, 450, text=online_xbox["peak24"], font=("", 12), fill="ghost white",tag="grim")
        endTime = time.time() - startTime
        print(endTime)
        self.window.after(self.delay, self.update)


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

# Create a window and pass it to the Application object
App2(Tk(), "Tkinter and OpenCV","bg-video.mp4")