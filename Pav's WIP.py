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
global xx
global yy
global first
global treVal
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
global counting
global i
i=1
counting = 0
root = Tk()
root.title("Virtual Robot Treasure Hunt")

image_url = "http://i.imgur.com/Q9VXPIw.gif"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)

canvas=Canvas(root,width = 650, height = 650)

xpos = 0
ypos = 0
canvas.create_image(xpos, ypos, image=photo)
canvas.pack()

class Treasure(object):
    def __init__(self,xx,yy):
        self.treList = []
        self.xx=xx
        self.val = 0
        self.yy=yy
        self.tre = canvas.create_rectangle(self.xx,self.yy,self.xx+50,self.yy+50,fill='white')

    def givecoords(self):
        self.xx2 = self.xx+50
        self.yy2 = self.yy+50
        return self.xx,self.yy,self.xx2,self.yy2
    
    def coordChange(self,xx,yy):
        self.xx=xx
        self.yy=yy
        canvas.coords(self.tre,self.xx,self.yy,self.xx+50,self.yy+50)
        canvas.update()

    def returnCenter(self):
        self.rx = (self.xx - self.xx2)/2
        self.ry = (self.yy - self.yy2)/2
        self.center = self.xx + self.rx, self.yy + self.ry
        return self.center

    
def updateTre(i,storeTre2):
    treList.insert(i,storeTre2)
    return treList

def nextTreasure(storeTre):
    global treList
    treList.append(storeTre)
    print treList
    return treList

amountTreasure=Listbox(root, selectmode=SINGLE, width=10, height=4)
amountTreasure.insert(1, '3 Treasure')
amountTreasure.insert(2, '5 Treasure')
amountTreasure.insert(3, '7 Treasure')
amountTreasure.insert(4, '11 Treasure')
amountTreasure.pack(side=LEFT)
global treasure1
treasure1 = Treasure(360,240)

def Selection():
    global oneShot
    oneShot+=1
    global varTreasure
    varTreasure = 1
    global i
    if oneShot>1:
        print "Your choice has already been made"
    else:
        if amountTreasure.curselection() == ():
            print "please choose an option"
        else:
            selection = amountTreasure.curselection()
            if selection == (0,):
                varTreasure+=2
            elif selection == (1,):
                varTreasure+=4
            elif selection == (2,):
                varTreasure+=6
            elif selection == (3,):
                varTreasure+=10
    return varTreasure, treasure1

buttonSelect=Button(root, text='confirm', command=Selection)
buttonSelect.pack(side=LEFT)

coord1 = Spinbox(root, from_=0, to=640, width=4)
coord1.pack(side=LEFT)
coord2 = Spinbox(root, from_=0, to=640, width=4)
coord2.pack(side=LEFT)

def newTre():
    global treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10, treasure11, treasure12
    global counting
    global treVal
    counting+=1
    global oneShot2
    if counting == 1:
        nextTreasure(treasure1)
        treasure2 = Treasure(360,240)
    elif counting == 2:
        nextTreasure(treasure2)
        treasure2.val = treVal
        treasure3 = Treasure(360,240)
    elif counting == 3:
        nextTreasure(treasure3)
        treasure3.val = treVal
        treasure4 = Treasure(360,240)
    elif counting == 4:
        nextTreasure(treasure4)
        treasure4.val = treVal
        treasure5 = Treasure(360,240)
    elif counting == 5:
        nextTreasure(treasure5)
        treasure5.val = treVal
        treasure6 = Treasure(360,240)
    elif counting == 6:
        nextTreasure(treasure6)
        treasure6.val = treVal
        treasure7 = Treasure(360,240)
    elif counting == 7:
        nextTreasure(treasure7)
        treasure7.val = treVal
        treasure8 = Treasure(360,240)
    elif counting == 8:
        nextTreasure(treasure8)
        treasure8.val = treVal
        treasure9 = Treasure(360,240)
    elif counting == 9:
        nextTreasure(treasure9)
        treasure9.val = treVal
        treasure10 = Treasure(360,240)
    elif counting == 10:
        nextTreasure(treasure10)
        treasure10.val = treVal
        treasure11 = Treasure(360,240)
    elif counting == 11:
        nextTreasure(treasure11)
        treasure11.val = treVal
        treasure12 = Treasure(360,240)
    return counting

def coordSet():
    xx = coord1.get()
    yy = coord2.get()
    xx = int(xx)
    yy = int(yy)
    if xx>640:
        print "invalid x coordinate"
    elif yy>640:
        print "invalid y coordinate"
    else:
        if counting == 0:
            treasure1.coordChange(xx,yy)
            updateTre(0,treasure1)
        elif counting == 1:
            treasure2.coordChange(xx,yy)
            updateTre(1,treasure2)
        elif counting == 2:
            treasure3.coordChange(xx,yy)
            updateTre(2,treasure3)
        elif counting == 3:
            treasure4.coordChange(xx,yy)
            updateTre(3,treasure4)
        elif counting == 4:
            treasure5.coordChange(xx,yy)
            updateTre(4,treasure5)
        elif counting == 5:
            treasure6.coordChange(xx,yy)
            updateTre(5,treasure6)
        elif counting == 6:
            treasure7.coordChange(xx,yy)
            updateTre(6,treasure7)
        elif counting == 7:
            treasure8.coordChange(xx,yy)
            updateTre(7,treasure8)
        elif counting == 8:
            treasure9.coordChange(xx,yy)
            updateTre(8,treasure9)
        elif counting == 9:
            treasure10.coordChange(xx,yy)
            updateTre(9,treasure10)
        elif counting == 10:
            treasure11.coordChange(xx,yy)
            updateTre(10,treasure11)
        elif counting == 11:
            treasure12.coordChange(xx,yy)
            updateTre(11,treasure12)
        return xx, yy

buttonSet=Button(root, text='set', command=coordSet)
buttonSet.pack(side=LEFT)

def randCoord():
    xx = random.randint(0, 640)
    yy = random.randint(0, 640)
    if counting == 0:
        treasure1.coordChange(xx,yy)
        updateTre(0,treasure1)
    elif counting == 1:
        treasure2.coordChange(xx,yy)
        updateTre(1,treasure2)
    elif counting == 2:
        treasure3.coordChange(xx,yy)
        updateTre(2,treasure3)
    elif counting == 3:
        treasure4.coordChange(xx,yy)
        updateTre(3,treasure4)
    elif counting == 4:
        treasure5.coordChange(xx,yy)
        updateTre(4,treasure5)
    elif counting == 5:
        treasure6.coordChange(xx,yy)
        updateTre(5,treasure6)
    elif counting == 6:
        treasure7.coordChange(xx,yy)
        updateTre(6,treasure7)
    elif counting == 7:
        treasure8.coordChange(xx,yy)
        updateTre(7,treasure8)
    elif counting == 8:
        treasure9.coordChange(xx,yy)
        updateTre(8,treasure9)
    elif counting == 9:
        treasure10.coordChange(xx,yy)
        updateTre(9,treasure10)
    elif counting == 10:
        treasure11.coordChange(xx,yy)
        updateTre(10,treasure11)
    elif counting == 11:
        treasure12.coordChange(xx,yy)
        updateTre(11,treasure12)
    return xx, yy

btnRand=Button(root, text='Randomize', command=randCoord)
btnRand.pack(side=LEFT)

treasureValue=Listbox(root, selectmode=SINGLE, width=6, height=3)
treasureValue.insert(1, 'Bronze')
treasureValue.insert(2, 'Silver')
treasureValue.insert(3, 'Gold')
treasureValue.pack(side=LEFT)

def varNext():
    print treasure1.givecoords()
    global oneShot2
    global treasureList
    global first
    oneShot2+=1
    treVal = 0
    treVar = treasureValue.curselection()
    if treasureValue.curselection() == ():
        print "Please select the value for the treasure"
    elif treVar == (0,):
        treVal = 1
    elif treVar == (1,):
        treVal = 2
    elif treVar == (2,):
        treVal = 3
    if first == False:
        treasure1.val = treVal
        print treasure1.val
        first = True
    if varTreasure == 3:
        if oneShot2>2:
            print "Press start to begin"
        else:
            treasureList.insert(oneShot2, treVal)
            newTre()
    if varTreasure == 5:
        if oneShot2>4:
            print "Press start to begin"
        else:
            treasureList.insert(oneShot2, treVal)
            newTre()
    if varTreasure == 7:
        if oneShot2>6:
            print "Press start to begin"
        else:
            treasureList.insert(oneShot2, treVal)
            newTre()
    if varTreasure == 11:
        if oneShot2>10:
            print "Press start to begin"
        else:
            treasureList.insert(oneShot2, treVal)
            newTre()
    return oneShot2, treVal
   
buttonNext=Button(root, text='Next', command=varNext)
buttonNext.pack(side=LEFT)

wishlist = Listbox(root, selectmode=MULTIPLE, width=11, height=4)
wishlist.insert(1, '-WISHLIST-')
wishlist.insert(2, 'Bronze')
wishlist.insert(3, 'Silver')
wishlist.insert(4, 'Gold')
wishlist.pack(side=LEFT)

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
        #if itn == 0:
        #    xXx1337h4x0rzxXx = "You have discovered Mechatite, an expensive and rare material"
        #elif itn == 1:
        #    xXx1337h4x0rzxXx = "Upon searching the planet, you have discovered an ancient relic from the extinct natives of the planet"
        #elif itn == 2:
    xXx1337h4x0rzxXx = "You have discovered all the fucks i give for project 3... non!"
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

        self.search()

        robotimage_url = "http://i.imgur.com/zR2sDWw.gif"
        image2_byt = urlopen(robotimage_url).read()
        image2_b64 = base64.encodestring(image2_byt)
        self.photo2 = tk.PhotoImage(data=image2_b64)
        self.id1 = canvas.create_image(self.x,self.y, image=self.photo2)
        canvas.update()

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

        while 1==1:
            if self.valX == True and self.valY == True:
                self.search()
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
                canvas.itemconfigure(textWarning, text="Meteor shower incoming!!!", fill='white')
            
            elif lightchange == 3:
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(amberTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 3
                canvas.itemconfigure(textWarning, text="Meteor shower in effect!!!", fill='white')
                print "Stop"

            elif lightchange == 4:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 2



root.mainloop()
