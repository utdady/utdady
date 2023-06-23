from tkinter import *
import pygame

def play_A(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("A.wav") # file path depends on where you place the file 
    sound.play()

def play_B(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("B.wav") # file path depends on where you place the file 
    sound.play()

def play_Bb(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("Bb.wav") # file path depends on where you place the file 
    sound.play()

def play_C(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("C.wav") # file path depends on where you place the file 
    sound.play()

def play_C_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("C_s.wav") # file path depends on where you place the file 
    sound.play()

def play_C_sharp1(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("C_s1.wav") # file path depends on where you place the file 
    sound.play()

def play_C1(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("C1.wav") # file path depends on where you place the file 
    sound.play()

def play_D(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound('D.wav')
    sound.play()

def play_D_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("D_s.wav") # file path depends on where you place the file 
    sound.play()

def play_D_sharp1(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("D_s1.wav") # file path depends on where you place the file 
    sound.play()

def play_D1(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("D1.wav") # file path depends on where you place the file 
    sound.play()

def play_E(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("E.wav") # file path depends on where you place the file 
    sound.play()

def play_E1(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("E1.wav") # file path depends on where you place the file 
    sound.play()

def play_F(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("F.wav") # file path depends on where you place the file 
    sound.play()

def play_F_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("F_s.wav") # file path depends on where you place the file 
    sound.play()

def play_F1(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("F1.wav") # file path depends on where you place the file 
    sound.play()

def play_G(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("G.wav") # file path depends on where you place the file 
    sound.play()

def play_G_sharp(event):
    if not pygame.mixer.get_init():
        pygame.mixer.init()
    sound = pygame.mixer.Sound("G_s.wav") # file path depends on where you place the file 
    sound.play()

# main program
gui = Tk()           # make a GUI window
topframe = Frame(gui, width=20, height=5)
topframe.grid(column=0, row=0)
bottomframe = Frame(gui, width=20, height=15)
bottomframe.grid(column=0, row=1)

# white keys
button1 = Button(bottomframe, width=3, height=10, bg='ivory', )
button1.bind('<Button-1>', play_C)
button1.grid(column=0, row=0, columnspan=2, rowspan=3)

button3 = Button(bottomframe, width=3, height=10, bg='ivory')
button3.bind('<Button-1>', play_D)
button3.grid(column=2, row=0, columnspan=2, rowspan=3)

button5 = Button(bottomframe, width=3, height=10, bg='ivory')
button5.bind('<Button-1>', play_E)
button5.grid(column=4, row=0, columnspan=2, rowspan=3)

button6 = Button(bottomframe, width=3, height=10, bg='ivory')
button6.bind('<Button-1>', play_F)
button6.grid(column=7, row=0, columnspan=2, rowspan=3)

button8 = Button(bottomframe, width=3, height=10, bg='ivory')
button8.bind('<Button-1>', play_G)
button8.grid(column=9, row=0, columnspan=2, rowspan=3)

button10 = Button(bottomframe, width=3, height=10, bg='ivory')
button10.bind('<Button-1>', play_A)
button10.grid(column=11, row=0, columnspan=2, rowspan=3)

button12 = Button(bottomframe, width=3, height=10, bg='ivory')
button12.bind('<Button-1>', play_B)
button12.grid(column=13, row=0, columnspan=2, rowspan=3)

# black keys

button2 = Button(bottomframe, width=2, height=7, bg='black')
button2.bind('<Button-1>', play_C_sharp)
button2.grid(column=1, row=0, columnspan=2, rowspan=2)

button4 = Button(bottomframe, width=2, height=7, bg='black')
button4.bind('<Button-1>', play_D_sharp)
button4.grid(column=3, row=0, columnspan=2, rowspan=2)

button7 = Button(bottomframe, width=2, height=7, bg='black')
button7.bind('<Button-1>', play_F_sharp)
button7.grid(column=8, row=0, columnspan=2, rowspan=2)

button9 = Button(bottomframe, width=2, height=7, bg='black')
button9.bind('<Button-1>', play_G_sharp)
button9.grid(column=10, row=0, columnspan=2, rowspan=2)

button11 = Button(bottomframe, width=2, height=7, bg='black')
button11.bind('<Button-1>', play_Bb)
button11.grid(column=12, row=0, columnspan=2, rowspan=2)

mainloop()
