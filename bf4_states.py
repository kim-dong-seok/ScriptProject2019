import tkinter as tk
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure

root = tk.Tk()

canvas1 = tk.Canvas(root, width=1000, height=350)
canvas1.pack()

button1 = tk.Button(root, text='Exit Application', command=root.destroy)
canvas1.create_window(85, 300, window=button1)

entry1 = tk.Entry(root)
canvas1.create_window(100, 200, window=entry1)

entry2 = tk.Entry(root)
canvas1.create_window(100, 220, window=entry2)

entry3 = tk.Entry(root)
canvas1.create_window(100, 240, window=entry3)

figure2 = Figure(figsize=(5, 4), dpi=100)
subplot2 = figure2.add_subplot(111)
labels2 = 'Label1', 'Label2', 'Label3'
pieSizes = [float(5.0), float(5.0), float(5.0)]
explode2 = (0, 0.1, 0)
subplot2.pie(pieSizes, explode=explode2, labels=labels2, autopct='%1.1f%%', shadow=True, startangle=90)
subplot2.axis('equal')
pie2 = FigureCanvasTkAgg(figure2, root)
pie2.get_tk_widget().place(x=0,y=0)



root.mainloop()