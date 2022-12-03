from tkinter import * 
from PIL import ImageTk, Image
import threading
import dos
import fixbadurls as fix
import time
import matplotlib.pyplot as plt

win = Tk ()
win.title("Multi-Threading Dos App")
win.iconbitmap('images\\hotpig_icon.ico')
win.geometry('600x400+50+50')

results = Label(win)
results.place(x=300, y=150)

def requestDos():
    datatrack.start()
    global target    
    dos.threads = int(dosThreads.get())
    webPages = []
    for i in range(len(target)):
        remText = target[i].get()
        target[i].delete(0, END)
        target[i].insert(END, fix.makeValid(remText))
        webPages.append(target[i].get())
    dos.initThreads(webPages)
    results['text'] = target[0].get()

class mainDosThread (threading.Thread):
    def run(self):
        requestDos()
maindosthread = mainDosThread()

def addTarget():
    global targetLen, target
    target.append(Entry(win, width=32))
    target[targetLen].place(x=50, y= + (20*targetLen + 7))
    targetLen+=1

target = []
targetLen = 0
addTarget()

dosBtn = Button(win, text="Attack", command=maindosthread.start)
dosBtn.place(x=260, y=5)

extraInfo = LabelFrame(win, width=170, height=125)
extraInfo.place(x=430, y=5)

targetExplanation = Label(win, text="Target:")
targetExplanation.place(x=5, y=5)

dosThreads = Entry(extraInfo, width=5)
dosThreads.insert(0, 1)
dosThreads.place(x=60, y=5)

dosThreadsExplanation = Label(extraInfo, text="Threads:")
dosThreadsExplanation.place(x=5, y=5)

addTargetButton = Button(win, text="Add Target", command=addTarget)
addTargetButton.place(x=350, y=5)

my_img = ImageTk.PhotoImage(Image.open("images\\bonzibuddy.png"))
bonzi = Label(image=my_img)
bonzi.place(x=450, y=150)

def stop_Dos():
    dos.continueDos=False

stopDos = Button(win, text="Stop", command=stop_Dos)
stopDos.place(x=310, y=5)

dosTracker = Label(extraInfo, text=dos.numRequests)
dosTracker.place(x=5, y = 25)

threadsCreated = Label(extraInfo, text=len(dos.thread))
threadsCreated.place(x=5, y=50)

threadsInit = Label(extraInfo, text=dos.threadsinited)
threadsInit.place(x=5, y=75)

dosPerSecond = 0
dosPerSecondLabel = Label(extraInfo)
dosPerSecondLabel.place(x=5, y=100)


class DataTrack (threading.Thread):
    def run(self):
        global dosPerSecond
        stopWait = time.time()
        dos_Count_At_Start = dos.numRequests
        RPS = []
        for i in range(50000):
            if time.time() > stopWait:
                dosPerSecond = (dos.numRequests - dos_Count_At_Start)
                dos_Count_At_Start = dos.numRequests
                print(dos.numRequests, dos_Count_At_Start)
                stopWait = time.time() + 0.5
                RPS.append(dosPerSecond)
            dosPerSecondLabel["text"] = "{} requests per second".format(dosPerSecond)
            dosTracker["text"] = "{} requests have been sent".format(dos.numRequests)
            threadsCreated["text"] = "{} threads have been created".format(len(dos.thread))
            threadsInit["text"] = "{} threads have been initiated".format(dos.threadsinited)
        plt.plot(range(len(RPS)), RPS)
        plt.xlabel("Time")
        plt.ylabel("RPS")
        plt.show()

datatrack = DataTrack()

win.mainloop()
