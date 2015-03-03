from Tkinter import*
import math
import time
import random
import io
import base64
import tkMessageBox 
import Tkinter as tk
from urllib2 import urlopen
xx = 360
yy = 240
global xx, xx2
global canPlace
canPlace = True
global yy, yy2
global icc
icc = 0
global first
global ic1
ic1 = -1
global treVal
global val
treVal = 0
first = False
global coord1
global coord2
global treasureList
global treList
treList = []
treasureList = []
global treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10, treasure11, treasure12
oneShot = 0
global oneShot
oneShot2 = 0
global oneShot2
global placementXX, placementYY
global counting
global i
i=1
counting = 0
root = Tk()
root.title("Vladimir's Conquest")

image_url = "http://i.imgur.com/gqL0Q5z.gif"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)

canvas=Canvas(root,width = 650, height = 650)
xpos = 0
ypos = 0
canvas.create_image(xpos, ypos, image=photo)
canvas.pack()

class Treasure(object):
    def __init__(self,xx,yy,treName):
        self.treList = []
        self.xx=xx
        self.treName=treName
        self.val = 0
        self.yy=yy
        self.icc = 0
        self.col = 'white'
        self.tre = canvas.create_rectangle(self.xx,self.yy,self.xx+50,self.yy+50,fill=self.col)

    def givecoords(self):
        self.xx2 = self.xx+50
        self.yy2 = self.yy+50
        xx = self.xx
        yy = self.yy
        return self.xx,self.yy,self.xx2,self.yy2
    
    def returnCenter(self):
        self.rx = (self.xx - self.xx2)/2
        self.ry = (self.yy - self.yy2)/2
        self.center = self.xx + self.rx, self.yy + self.ry
        return self.center

    def giveDict(self):
        return treList
'''
    def changeVal(self, tempx, tempy):
        self.tempx=tempx
        self.tempy=tempy
        self.icc+=1
        if self.icc == 1:
            self.col = 'orange'
            print(self.treName + " now has the value of 1")
            print self.val
            self.val = 1
        elif self.icc == 2:
            self.col = 'grey'
            print(self.treName + " now has the value of 2")
            self.val = 2
        elif self.icc == 3:
            self.col = 'yellow'
            print(self.treName + " now has the value of 2")
            self.icc = 0
            self.val = 3
'''
def PlaceOB(event):
    global placementXX, placementYY
    placementXX = event.x
    placementYY = event.y
    global treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10, treasure11, treasure12
    global counting
    global canPlace
    #global treVal
    counting+=1
    global oneShot2
    chkOverlap()
    if canPlace == False:
        chkCoords()
    else: 
        if counting == 1:
            treasure1 = Treasure(placementXX, placementYY, 'Treasure 1')
            nextTreasure(treasure1)
        elif counting == 2:
            treasure2 = Treasure(placementXX, placementYY, 'Treasure 2')
            nextTreasure(treasure2)
        elif counting == 3:
            treasure3 = Treasure(placementXX, placementYY, 'Treasure 3')
            nextTreasure(treasure3)
        elif counting == 4:
            treasure4 = Treasure(placementXX, placementYY, 'Treasure 4')
            nextTreasure(treasure4)
        elif counting == 5:
            treasure5 = Treasure(placementXX, placementYY, 'Treasure 5')
            nextTreasure(treasure5)
        elif counting == 6:
            treasure6 = Treasure(placementXX, placementYY, 'Treasure 6')
            nextTreasure(treasure6)
        elif counting == 7:
            treasure7 = Treasure(placementXX, placementYY, 'Treasure 7')
            nextTreasure(treasure7)
        elif counting == 8:
            treasure8 = Treasure(placementXX, placementYY, 'Treasure 8')
            nextTreasure(treasure8)
        elif counting == 9:
            treasure9 = Treasure(placementXX, placementYY, 'Treasure 9')
            nextTreasure(treasure9)
        elif counting == 10:
            treasure10 = Treasure(placementXX, placementYY, 'Treasure 10')
            nextTreasure(treasure10)
        elif counting == 11:
            treasure11 = Treasure(placementXX, placementYY, 'Treasure 11')
            nextTreasure(treasure11)
        #chkCoords()
    return counting, placementXX, placementYY

def chkCoords():
    global val
    global treList
    global ic1
    global placementXX, placementYY
    str1 = len(treList)
    ic1 = -1
    try:
        for t in range(0, str1):
            ic1+=1
            strTemp = []
            strTemp = treList[ic1].givecoords()
            if placementXX > strTemp[0] and placementXX < strTemp[2]:
                if placementYY > strTemp[1] and placementYY < strTemp[3]:
                    changeVal()
                    #treList[ic1].changeVal(strTemp[0], strTemp[1])
                    treList[ic1].val = val
    except IndexError:
        pass
    
def changeVal():
    global icc
    global val
    icc+=1
    if icc == 1:
        print("Treasure now has the value of 1")
        val = 1
    elif icc == 2:
        print("Treasure now has the value of 2")
        val = 2
    elif icc == 3:
        print("Treasure now has the value of 3")
        icc = 0
        val = 3
    return val

def chkOverlap():
    global treList
    global ic1
    global nextTre
    global canPlace
    global placementXX, placementYY
    canPlace = True
    str1 = len(treList)
    ic1 = -1
    try:
        for t in range(0, str1):
            ic1+=1
            strTemp = []
            strTemp = treList[ic1].givecoords()
            if placementXX > strTemp[0] and placementXX < strTemp[2]:
                if placementYY > strTemp[1] and placementYY < strTemp[3]:
                    canPlace = False
    except IndexError:
            pass
    return canPlace

canvas.bind("<Button-1>", PlaceOB)

def updateTre(i,storeTre2):
    treList.insert(i,storeTre2)
    return treList

def nextTreasure(storeTre):
    global treList
    treList.append(storeTre)
    return treList

greenTraffic = canvas.create_oval(3,29,3+10,29+10,fill = 'green')
amberTraffic = canvas.create_oval(3,17,3+10,17+10,fill = 'black')
redTraffic = canvas.create_oval(3,5,3+10,5+10,fill = 'black')

textWarning = canvas.create_text(600, 40, anchor=NE, text=".", fill='black')

###----------Buttons----------###

#Start Robot and Timer#
def displayUFO():
    Timer1=Timer(root)
    Timer1.pack()
    Timer1.Start()
    robot1 = Robot(20,20,treList)
    robot1.movement(canvas)

Button(text="Start", cursor="trek", command=displayUFO).pack(side=LEFT, padx=20, pady=5)

#Stop Timer#
def END():
    Timer1=Timer(root)
    Timer1.pack()
    Timer1.Stop()

Button(text="Stop", cursor="trek", command=END).pack(side=LEFT, padx=0, pady=5)

#Exit Program#
def Exit():
    if tkMessageBox.askokcancel("Exit", "Are you sure you want to leave?"):
        if tkMessageBox.askokcancel("Exit", "Really?"):
            root.destroy()

Button(text="Exit", cursor="trek", command=Exit).pack(side=RIGHT, padx=20, pady=5)

###----------Timer----------###

toolbar = Frame(root)
toolbar.pack(side=BOTTOM, anchor=SW, padx=10, pady=5)

class Timer(Frame):

    #Implements timer widget#
    def __init__(self, thing=None,*toolbar):
        Frame.__init__(self, thing,toolbar)
        self.start = 0
        self.elapsedtime = 0
        self.running = 0
        self.timestr = StringVar()
        self.timerwidget()
        
    #Timer widget on screen#
    def timerwidget(self):
        l = Label(self, textvariable=self.timestr)
        self.settime(self.elapsedtime)
        l.pack(padx=25, pady=14)

    #Timer format in (00:00:00) = (Minutes : Seconds : Milliseconds)#
    def settime(self, elaps):
        minutes = int(elaps/60)
        seconds = int(elaps - minutes*60)
        milliseconds = int((elaps - minutes*60 - seconds)*100)
        self.timestr.set('%02d:%02d:%02d'%(minutes, seconds, milliseconds))

    #Makes timer work#
    def update(self):
        self.elapsedtime = time.time() - self.start
        self.settime(self.elapsedtime)
        self.timer = self.after(50, self.update)

    #Starts timer#
    def Start(self):
        if not self.running:
            self.start = time.time() - self.elapsedtime
            self.update()
            self.running = 1

    #Stops timer#
    def Stop(self):
        if self.running:
            self.after_cancel(self.timer)
            self.elapsedtime = time.time() - self.start
            self.settime(self.elapsedtime)
            self.running = 0

def treDesc():
    itn = random.randint(0, 5)
    if itn == 0:
        xXx1337h4x0rzxXx = "You have conquered Kiev!!!"
    elif itn == 1:
        xXx1337h4x0rzxXx = "You have annihilated Dnipropetrovsk"
    elif itn == 2:
        xXx1337h4x0rzxXx = "You just made Chenobryl your bitch"
    elif itn == 3:
        xXx1337h4x0rzxXx = "Odessa is now under the rule of putin!!!"
    elif itn == 4:
        xXx1337h4x0rzxXx = "Lviv is now under the command of Putin!!!"
    elif itn == 5:
        xXx1337h4x0rzxXx = "More gold to add to the stockpile!!!"
    if tkMessageBox.showinfo("Treasure Found", xXx1337h4x0rzxXx):
        pass
            
###----------Robot----------###

class Robot(object):

    def __init__(self, x, y, treList):
        self.treList = treList
        self.q = -1
        self.obnum = 5-1
        self.x = x
        self.y = y
        self.x1 = x + 20
        self.y1 = y + 20
        self.pp=0
        self.rx = (self.x1 - self.x)/2
        self.ry = (self.y1 - self.y)/2
        self.tempxy =[]
        self.sum1 = 1
        self.sum2 = 1
        self.valX = False
        self.valY = False
        self.rotated = False
        self.stillSearch = True
        self.ic = 0
        self.search()
        self.varTreasure = len(self.treList)

        robotimage_url = "http://i.imgur.com/1AaKbvj.gif"
        image2_byt = urlopen(robotimage_url).read()
        image2_b64 = base64.encodestring(image2_byt)
        self.photo2 = tk.PhotoImage(data=image2_b64)
        self.id1 = canvas.create_image(self.x,self.y, image=self.photo2)
        canvas.update()

    def EndCheck(self):
        self.ic+=1

        if self.ic == self.varTreasure:
            self.stillSearch = False
        else:
            self.search()
                
    def search(self):  
        try:
            self.q += 1
            LMcoordtemp = treList[self.q].givecoords()
            destxx = LMcoordtemp[0]
            destxx+=20
            destyy = LMcoordtemp[1]
            destyy+=20
            destxx2 = LMcoordtemp[2]
            destxx2-=20
            destyy2 = LMcoordtemp[3]
            destyy2-=20
            self.destxy = [destxx, destyy, destxx2, destyy2]
        except IndexError:
            pass
        
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center

    def movement(self,canvas):
        global counting
        counting = 1

        global sleeping
        sleeping = 1

        global lightchange    
        lightchange = 1
        
        dest = self.destxy
        self.current_coord = (self.x,self.y)

        while self.stillSearch == True:
            if self.valX == True and self.valY == True:
                self.EndCheck()
                treDesc()
                dest = self.destxy
                self.valX = False
                self.valY = False
            else:
                if self.valY == True:
                    pass
                else:
                    if self.y > dest[1]:
                        self.sum2 = -1
                    elif self.y < dest[1]:
                        self.sum2 = 1
                    if self.y > dest[1] and self.y < dest[3]:
                        self.valY = True
                        self.sum2 = 0
                    
                if self.valX == True:
                    pass
                else:
                    if self.x > dest[0]:
                        self.sum1 = -1
                    elif self.x < dest[0]:
                        self.sum1 = 1
                    if self.x > dest[0] and self.x < dest[2]:
                        self.sum1 = 0
                        self.valX = True
                        
                self.y+=self.sum2
                self.x+=self.sum1
                self.x1 = self.x + 20
                self.y1 = self.y +20
                self.current_coord = (self.x,self.y)
                canvas.coords(self.id1, self.current_coord)
                canvas.update()
                
            if sleeping == 1:
               time.sleep(0.01)
            elif sleeping == 2:
                time.sleep(0.07)
            elif sleeping == 3:
                time.sleep(1.0)

            counting += 1
        
            if counting == 1:
                lightchange = 4
            elif counting == 15:
                lightchange = 1

            if counting == 200:
                lightchange = 2
            elif counting == 235:
                counting = 0
                lightchange = 3

            if lightchange == 1:
                canvas.itemconfigure(greenTraffic, fill = 'green')
                canvas.itemconfigure(amberTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'black')
                sleeping = 1
                canvas.itemconfigure(textWarning, text=".", fill='black')
        
            elif lightchange == 2:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'black')
                sleeping = 2
                canvas.itemconfigure(textWarning, text="Military checkpoint incoming!!!", fill='white')
            
            elif lightchange == 3:
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(amberTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 3
                canvas.itemconfigure(textWarning, text="Military checkpoint", fill='white')
                print "Stop"

            elif lightchange == 4:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 2



root.mainloop()
