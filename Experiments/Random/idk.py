import time
import turtle
from tkinter import *

def updateScreen(window):
    window.mainloop()

msg = input("Enter a number: ")
broken = False
while broken == False:
    try:
        if (int(msg) <= 0) or (int(msg) >= 0):
            broken = True
            print("Good job, you can follow directions!")
    except ValueError:
        print("We're going to try that again...")
        msg = input("Enter a number: ")
time.sleep(2)
print("Now that you can follow simple directions, we are going to try some harder questions!")
time.sleep(2)

def placeObj(obj, relx, rely):
    obj.place(relx= relx, rely= rely, anchor=CENTER)

win = Tk()
win.title("Focus on the questions")
win.configure(background="tan")
win.geometry("600x600")

textLabel = StringVar()
textLabel.set("")
midText = Label(win, textvariable=textLabel, font="Sans", bg="tan")
midText.place(relx=0.5, rely=0.5, anchor=CENTER)
print('Running...')

def resetLevel(endScreen, text):
    if endScreen == True:
        turtle.clear()
        print("Worked?!")
        txt = Label(win, text=text, font="Sans", bg="tan")
        placeObj(txt, 0.5, 0.5)
        time.sleep(2)
        win.quit()
    win.quit()

def nextSlide(correct, wrong, next1, next2):
    if correct == true1:
        textLabel.set("Which one of these is correct?")
        correct.destroy()
        wrong.destroy()
        placeObj(next1, 0.25, 0.75)
        placeObj(next2, 0.75, 0.75)
    elif correct == true2:
        textLabel.set("There are 11 vowels in this sentence.")
        correct.destroy()
        wrong.destroy()
        placeObj(next1, 0.25, 0.75)
        placeObj(next2, 0.75, 0.75)
    elif correct == true3:
        textLabel.set("Why did the chicken cross the road?")
        correct.destroy()
        wrong.destroy()
        placeObj(next1, 0.5, 0.75)
        placeObj(next2, 0.5, 0.85)
    elif txt.get == "To get to the other side.":
        textLabel.set("Are you enjoying this game?")
        correct.destroy()
        wrong.destroy()
        placeObj(next1, 0.25, 0.75)
        placeObj(next2, 0.75, 0.75)



true1 = Button(win, text="True", width=5, height=2, bg="white", command= lambda: nextSlide(true1, false1, true2, false2))
false1 = Button(win, text="False", width=5, height=2, bg="white", command=resetLevel)

true2 = Button(win, text="True", width=5, height=2, bg="white", command= lambda: nextSlide(true2, false2, true3, false3))
false2 = Button(win, text="False", width=5, height=2, bg="white", command= lambda: resetLevel)

true3 = Button(win, text="True", width=5, height=2, bg="white", command= lambda: nextSlide(true3, false3, true4, skip4))
false3 = Button(win, text="False", width=5, height=2, bg="white", command= lambda: resetLevel)

txt = StringVar()
true4 = Entry(win, text=txt, width=5, bg="white")
skip4 = Button(win, text="Skip", width=5, height=2, bg="white", command= lambda: resetLevel(True, "You will never be given skips in the real world..."))

win.after(5000, lambda: textLabel.set("This was a blank screen."))
win.after(5000, lambda: placeObj(true1, 0.25, 0.75))
win.after(5000, lambda: placeObj(false1, 0.75, 0.75))
#lambda: textLabel.set("Which one of these is correct?"))

mainloop()