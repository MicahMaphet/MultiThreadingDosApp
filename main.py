from tkinter import * 
from PIL import ImageTk, Image
import threading
import dos
import fixbadurls as fix

win = Tk ()
win.title("Bonzi Buddy the Website Dosing Monkey")
win.iconbitmap('images\\hotpig_icon.ico')
win.geometry('600x400+50+50')

results = Label(win)
results.place(x=200, y = 100)


def requestDos():
    global target    
    dos.threads = int(dosThreads.get())
    webPages = []
    for i in range(len(target)):
        remText = target[i].get()
        target[i].delete(0, END) # this will delete everything inside the entry
        target[i].insert(END, fix.makeValid(remText))
        webPages.append(target[i].get())
    dos.initThreads(webPages)
    results['text'] = target[0].get()

class mainDosThread (threading.Thread):
    def run(self):
        requestDos()
maindosthread = mainDosThread()

target = []
targetLen = 1
target.append(Entry(win, width=25))
# target[0].insert(0, "https://")
target[0].place(x=50, y=7)

dosBtn = Button(win, text="Attack", command=maindosthread.start)
dosBtn.place(x=210, y=5)

my_img = ImageTk.PhotoImage(Image.open("images\\bonzibuddy.png"))
bonzi = Label(image=my_img)
bonzi.place(x=400, y=120)

extraInfo = LabelFrame(win, width=170, height=100)
extraInfo.place(x=380, y=5)

targetExplanation = Label(win, text="Target:")
targetExplanation.place(x=5, y=5)

dosThreads = Entry(extraInfo, width=5)
dosThreads.insert(0, 1)
dosThreads.place(x=60, y=5)

dosThreadsExplanation = Label(extraInfo, text="Threads:")
dosThreadsExplanation.place(x=5, y=5)

def addTarget():
    global targetLen, target
    target.append(Entry(win, width=25))
    # target[targetLen].insert(0, "https://")
    target[targetLen].place(x=50, y=7 + (20*targetLen))
    targetLen+=1

addTargetButton = Button(win, text="Add Target", command=addTarget)
addTargetButton.place(x=300, y=5)

def stop_Dos():
    dos.continueDos=False

stopDos = Button(win, text="Stop", command=stop_Dos)
stopDos.place(x=260, y=5)

dosTracker = Label(extraInfo, text=dos.numRequests)
dosTracker.place(x=5, y = 25)

threadsCreated = Label(extraInfo, text=len(dos.thread))
threadsCreated.place(x=5, y=50)

threadsInit = Label(extraInfo, text=len(dos.thread))
threadsInit.place(x=5, y=75)

class DataTrack (threading.Thread):
    def run(self):
        while 1:
            dosTracker["text"] = "{} requests have been sent".format(dos.numRequests)
            threadsCreated["text"] = "{} threads have been created".format(len(dos.thread))
            threadsInit["text"] = "{} threads have been initiated".format(dos.threadsinited)

datatrack = DataTrack()
datatrack.start()

win.mainloop()
