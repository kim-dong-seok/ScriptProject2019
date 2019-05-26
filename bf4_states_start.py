import requests
from tkinter import *
from PIL import Image, ImageTk
import cv2
import time
import tkinter.ttk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure
class App2:
    def __init__(self):
        self.window = Tk()
        self.window.title("bf4.gg")
        self.video_source = "bg-video.mp4"
        self.originimage2 = Image.open("bf4.gg.png").resize((600, 120))
        self.logoImage = ImageTk.PhotoImage(self.originimage2)
        self.orlginOpacity = Image.open("opacity.png")
        self.opacityImage = ImageTk.PhotoImage(self.orlginOpacity.resize((600, 300)))
        online = requests.get("https://api.bf4stats.com/api/onlinePlayers?output=json").json()
        self.online_players = [online["pc"], online["ps4"],online["xone"],online["ps3"],online["xbox"]]
        self.total_players=0
        for i in range(5):
            self.total_players+=self.online_players[i]["count"]


        self.vid = MyVideoCapture(self.video_source)
        self.canvas = Canvas(self.window, width = 1600, height = 900)
        self.canvas.pack()
        self.e1 = Entry(self.canvas,font=("",20),width = 20)
        self.e1.insert(0,"Player name")
        self.e1.place(x=500, y=400)
        self.b1 = Button(self.canvas,  text="Search",font=("",14,"bold"),command=self.search,highlightbackground="black",width = 9,pady=0)
        self.b1.place(x=1100, y=400,anchor="ne")
        self.values = ["pc","ps4","xone","ps3","xbox"]
        self.c1 = tkinter.ttk.Combobox(self.canvas, values=self.values,width=7,font=("",20))
        self.c1.set("Platform")
        self.c1.place(x=835, y=400)

        self.delay = 15
        self.update()
        self.window.mainloop()

        figure2 = Figure(figsize=(5, 4), dpi=100)
        subplot2 = figure2.add_subplot(111)
        labels2 = 'Label1', 'Label2', 'Label3'
        pieSizes = [float(5.0), float(5.0), float(5.0)]
        explode2 = (0, 0.1, 0)
        subplot2.pie(pieSizes, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
        subplot2.axis('equal')
        pie2 = FigureCanvasTkAgg(figure2, self.window)
        pie2.get_tk_widget().place(x=0,y=0)
    def search(self):
            pass
    def update(self):
        # Get a frame from the video source
        startTime = time.time()
        ret, frame = self.vid.get_frame()

        if ret:
            self.canvas.delete("grim")
            self.photo = ImageTk.PhotoImage(image=Image.fromarray(frame).resize((1600, 900)))
            self.canvas.create_image(0, 0, image = self.photo, anchor = NW,tag="grim")
            self.canvas.create_image(800, 600, image=self.opacityImage,tag="grim")
            self.canvas.create_image(800, 280, image=self.logoImage,tag="grim")
            self.canvas.create_text(800,510,text="현재 온라인 플레이어(총"+str(self.total_players)+"명)",font=("",16),fill="ghost white",tag="grim")
            for i in range(5):
                self.canvas.create_text(600+(100*i), 555, text=self.online_players[i]["label"], font=("",16),fill="ghost white",tag="grim")
                self.canvas.create_text(600+(100*i), 600, text=self.online_players[i]["count"], font=("", 19, "bold"), fill="ghost white",tag="grim")
                self.canvas.create_text(600+(100*i), 645, text="최다 접속", font=("", 14), fill="ghost white", tag="grim")
                self.canvas.create_text(600+(100*i), 675, text=self.online_players[i]["peak24"], font=("", 16), fill="ghost white", tag="grim")

        endTime = time.time() - startTime
        #print(endTime)
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
App2()