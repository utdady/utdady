# an analog clock  \
from datetime import datetime
from tkinter import *
import math

def draw_clock():
    w, h = 300, 300  # size of the canvas
    x, y = w/2, h/2  # center of the canvas and the clock
    size = 200       # size of the clock
    circle1 = canvas.create_oval(x-size/2, y-size/2, 
                                 x+size/2, y+size/2,
                                 fill='ivory')
    circle2 = canvas.create_oval(x-size/2, y-size/2,
                                 x+size/2, y+size/2, 
                                 width=3, outline='black')  
    ticks1, numbers = [], []
    n = 12
    for i in range(n):
        angle = 2*math.pi*i/n
        ticks1.append(canvas.create_line(x+100*math.cos(angle),
                                        y+100*math.sin(angle),
                                        x+90*math.cos(angle),
                                        y+90*math.sin(angle),
                                        fill='black', width=2))
        numbers.append(canvas.create_text(x+80*math.cos(angle),
                                y+80*math.sin(angle), text=str((i+2)%n+1)))
    ticks2 = []
    n = 60
    for i in range(n):
        angle = 2*math.pi*i/n
        ticks1.append(canvas.create_line(x+100*math.cos(angle),
                                        y+100*math.sin(angle),
                                        x+95*math.cos(angle),
                                        y+95*math.sin(angle),
                                        fill='black', width=1))
    global sec_time
    global min_time
    global hr_time
    global curr
    sec_time += 1     # add a time interval = 1 sec
    if sec_time % 60 == 0:
        min_time += 1
    if sec_time % 3600 == 0:
        hr_time += 1
    corr = (math.pi*3) / 2
    sec = ((math.pi*2) / 60) * float(curr[2])
    mins = ((math.pi*2) / 60) * float(curr[1])
    hrs = ((math.pi*2) / 12) * float(curr[0])
    alpha1 = 2*math.pi *(sec_time % 60) /60
    alpha2 = 2*math.pi *(min_time % 60) /60
    alpha3 = 2*math.pi *(hr_time % 60) /60
    arrow1 = canvas.create_line(x,y,x+90*math.cos(alpha1+corr+sec),y+90*math.sin(alpha1+corr+sec), fill='red', width=1, arrow='last')
    arrow2 = canvas.create_line(x,y,x+75*math.cos(alpha2+corr+mins),y+75*math.sin(alpha2+corr+mins), fill='blue', width=4, arrow='last')
    arrow3 = canvas.create_line(x,y,x+60*math.cos(alpha3+corr+hrs),y+60*math.sin(alpha3+corr+hrs), fill='black', width=2, arrow='last')
    gui.after(1000, lambda:draw_clock()) # update after 1000 msecs = 1 sec
    
    
# main program     
gui = Tk()
canvas = Canvas(gui, height=300, width=300)
canvas.pack()
sec_time = 0
min_time = 0
hr_time = 0
time = datetime.now()
curr = (time.strftime("%H"), time.strftime("%M"), time.strftime("%S"))
draw_clock()
gui.mainloop()
