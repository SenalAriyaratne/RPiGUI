from tkinter import *

import RPi.GPIO as io

from tkinter import font
from gpiozero import LED

# setup

io.setmode(io.BCM)

ledr = LED(4)
ledg1 = LED(17)
ledg2 =  LED(27)



#Functions

def red():
    if ledr.is_lit:
        ledr.off()
    else:
        ledr.on()
        ledg1.off()
        ledg2.off()


def green1():
    if ledg1.is_lit:
        ledg1.off()
    else:
        ledg1.on()
        ledg2.off()
        ledr.off()

        
def green2():
    if ledg2.is_lit:
        ledg2.off()
    else:
        ledg2.on()
        ledr.off()
        ledg1.off()


def close():
    win.destroy()
    io.cleanup()
    
# Setting up GUI
win = Tk()
win.title("LED TOGGLE")

myFont = font.Font(family = "Helvetica",size = 24,weight = "bold")

radio_red = Radiobutton(win,
                        text = "Red Led On",
                        font =myFont,
                        command = red,
                        value = 1).pack(anchor="center")
radio_green1 = Radiobutton(win,
                        text = "Green Led One On",
                        font =myFont,
                        command = green1,
                        value = 2).pack(anchor="center")
radio_green2 = Radiobutton(win,
                        text = "Green Led Two On",
                        font =myFont,
                        command = green2,
                        value = 3).pack(anchor="center")

Exit = Button(win, text = " Exit",
              font = myFont,
              command =  close,
              bg = "red",
              height = 1,
              width = 12).pack(anchor = "center")


#close()



