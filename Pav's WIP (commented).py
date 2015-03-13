from Tkinter import*
import math
import time
import random
import io
import base64
import webbrowser
import tkMessageBox
import copy
import Tkinter as tk
from urllib2 import urlopen

#globaling all the variables for use in multiple functions and classes

xx = 360
yy = 240
global xx, xx2
global skip
global listOfPaths
global name
name = 'yolo'
global trappedList
trappedList = []
listOfPaths = []
skip = []
global canPlace
global colour
colour = 'white'
canPlace = True
global yy, yy2
global icc
global treListIndex
treListIndex = 0
icc = 0
global first
global ic1
ic1 = -1
global treVal
global val
global queue
queue = []
global once
once = True
global score
score = 0
treVal = 0
first = False
global coord1
global coord2
global qIndex
qIndex=-1
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


image_url = "http://i.imgur.com/bSctRVP.gif"
image_byt = urlopen(image_url).read()
image_b64 = base64.encodestring(image_byt)
photo = tk.PhotoImage(data=image_b64)

canvas=Canvas(root,width = 650, height = 650)
xpos = 0
ypos = 0
canvas.create_image(xpos, ypos, image=photo)
canvas.pack()

#i don't fucking know how this works, ask jay or hadiyah

###----------Instructions and Treasure Items List----------###
instructionTextOne = "Become Vladimir and conquer Russia!"
instructionTextTwo = "Left click anywhere on the canvas to choose your destination. You can add as many destinations as you like.\
Once you have placed as many destinations as you like, click 'Start'."

def instructionsLink():
    
   instructionsWindow = Toplevel()

   instructionsLabel = Label(instructionsWindow, text="Instructions", font="Stencil 20", bg="lightgreen", wraplength=250)
   instructionsLabel.pack(side=TOP)
   instructionsLabel = Label(instructionsWindow, text=instructionTextOne, wraplength=250)
   instructionsLabel.pack(side=TOP)
   instructionsLabel = Label(instructionsWindow, text=instructionTextTwo, wraplength=250)
   instructionsLabel.pack(side=TOP)


def descriptionsLabelTwo_callback(event):
    webbrowser.open_new("http://en.wikipedia.org/wiki/Putinka")
    
def descriptionsLabelThree_callback(event):
    webbrowser.open_new("http://en.wikipedia.org/wiki/Koni_(dog)")
    
def descriptionsLabelFour_callback(event):
    webbrowser.open_new("http://en.wikipedia.org/wiki/Gold")
    

def descriptionsLink():
   descriptionsWindow = Toplevel()
   
   descriptionsLabelOne = Label(descriptionsWindow, text="Treasures!", font="Stencil 20", bg="lightgreen", wraplength=250)
   descriptionsLabelOne.pack(side=TOP)
   descriptionsLabelTwo = Label(descriptionsWindow, text="Treasure 1: Crates of Vodka", fg="Blue", wraplength=250)
   descriptionsLabelTwo.pack(side=TOP)
   descriptionsLabelTwo.bind("<Button-1>",descriptionsLabelTwo_callback)
   descriptionsLabelThree = Label(descriptionsWindow, text="Treasure 2: Koni the Dog", fg="Blue", wraplength=250)
   descriptionsLabelThree.pack(side=TOP)
   descriptionsLabelThree.bind("<Button-1>",descriptionsLabelThree_callback)
   descriptionsLabelFour = Label(descriptionsWindow, text="Treasure 3: Tons of Gold", fg="Blue", wraplength=250)
   descriptionsLabelFour.pack(side=TOP)
   descriptionsLabelFour.bind("<Button-1>",descriptionsLabelFour_callback)

menubar = Menu(root)
infomenu = Menu(menubar, tearoff=0)
infomenu.add_command(label="Instructions", command=instructionsLink)
infomenu.add_command(label="Treasure Items", command=descriptionsLink)
menubar.add_cascade(label="Information", menu=infomenu)

root.config(menu=menubar)

#this is where the traps are created

###----------Traps----------###
class Traps(object):
    def __init__(self):
        LM5IMG_url = "http://i.imgur.com/Bx3oHvN.gif"
        image5_byt = urlopen(LM5IMG_url).read()
        image5_b64 = base64.encodestring(image5_byt)
        self.photo5 = tk.PhotoImage(data=image5_b64)

        self.numX = 0
        self.numY = 0
        self.rand()
        self.numXX = (self.numX+15)
        self.numYY = (self.numY+15)
        cl4pTP = canvas.create_rectangle(self.numX, self.numY, self.numXX, self.numYY, fill='blue')
        self.img2 = canvas.create_image(self.numX+8, self.numY+8, image= self.photo5)

    #this makes up some bullshit coords for the traps

    def rand(self):
        self.numX = random.randint(50, 600)
        self.numY = random.randint(50, 600)
        return self.numX, self.numY

    #returns the coords of the trap

    def givecoords(self):
        return self.numX, self.numY, self.numXX, self.numYY

#creates treasures

###----------Treasure to set----------###
class Treasure(object):
    def __init__(self,xx,yy,treName):
        LM4IMG_url = "http://i.imgur.com/P6nMzm5.gif"
        image4_byt = urlopen(LM4IMG_url).read()
        image4_b64 = base64.encodestring(image4_byt)
        self.photo4 = tk.PhotoImage(data=image4_b64)

        self.treList = []
        self.xx=xx
        self.treName=treName
        self.val = 0
        self.yy=yy
        self.valName = "No value"
        self.icc = 0
        self.col = 'white'
        self.tre = canvas.create_rectangle(self.xx,self.yy,self.xx+50,self.yy+50,fill=self.col)
        self.img = canvas.create_image(self.xx+25, self.yy+25, image= self.photo4)


    #returns coords of traps

    def givecoords(self):
        self.xx2 = self.xx+50
        self.yy2 = self.yy+50
        xx = self.xx
        yy = self.yy
        return self.xx,self.yy,self.xx2,self.yy2

    #i forgot to delete this shit, not used anymore
    
    def returnCenter(self):
        self.rx = (self.xx - self.xx2)/2
        self.ry = (self.yy - self.yy2)/2
        self.center = self.xx + self.rx, self.yy + self.ry
        return self.center

    #and this

    def givedummy(self):
        self.rcx = 5000
        self.rcy = 5000
        self.rxx = 5050
        self.ryy = 5050
        return self.rcx, self.rcy, self.rxx, self.ryy

    #and this -_-

    def giveDict(self):
        return treList

#this is the shit that creates the sub menu when you right click

def popup(event):
    global placementXX, placementYY
    placementXX = event.x
    placementYY = event.y
    menu.post(event.x_root, event.y_root)
    return placementXX, placementYY

#it looks like shit with the massive "if" statement
#but it defines the treasures name for later use
#restrains the user from adding more than 11 tre's BIATCH

def PlaceOB(event):
    global placementXX, placementYY
    placementXX = event.x
    placementYY = event.y
    global treasure1, treasure2, treasure3, treasure4, treasure5, treasure6, treasure7, treasure8, treasure9, treasure10, treasure11, treasure12
    global counting
    global canPlace
    counting+=1
    global oneShot2
    chkOverlap()
    if canPlace == False:
        #chkCoords()
        print "cannot place treasure onto another treasure"
    else:
        placementXX-=25
        placementYY-=25
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
    placementXX+=25
    placementYY+=25
    return counting, placementXX, placementYY

#listbox of collected tre's
#gonna say tre's now instead of treasure because it's 01:06 IN THE FUCKING MORNING
lstCol = Listbox(root, selectmode=SINGLE)
lstCol.pack(side=LEFT)

#creates the wishlist listbox
lstWish = Listbox(root, selectmode=SINGLE)
lstWish.pack(side=RIGHT)


#forgot what this does
#oh wait... i remember!!! :D
#this is what allows you to change the values of the treasure
#it takes the coords of the mouse click
#and checks if it's in the middle of a tre
#if yes:
#holy fuck i'm losing my mind
#where was i again? oh yeah
#then when you click on what value you want, it changes the value of the tre
#ARE YOU EVEN LISTENING
def setVal():
    global val
    global treList
    global ic1
    global qIndex
    global name
    global lstWish
    global colour
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
                    treList[ic1].val = val
                    canvas.itemconfigure(treList[ic1].tre, fill = colour)
                    treList[ic1].valName = name
                    canvas.update()
    except IndexError:
        pass


#sets tre to be bronze
#like my artist name
#on soundcloud
#btw guys check out my soundcloud
def setB():
    global placementXX, placementYY
    global val
    global colour
    global name
    name = 'Bronze'
    val = 1
    colour = 'brown'
    setVal()
    return val, colour

#sets tre to be silver
def setS():
    global placementXX, placementYY
    global val
    global colour
    global name
    name = 'Silver'
    val = 2
    colour = 'grey'
    setVal()
    return val, colour

#sets value to be gold
def setG():
    global placementXX, placementYY
    global val
    global colour
    global name
    name = 'Gold'
    val = 3
    colour = 'yellow'
    setVal()
    return val, colour

#adds the item to the wishlist
def add_to_wishlist():
    global queue
    global qIndex
    global placementXX, placementYY
    str1 = len(treList)
    ic1 = -1
    icc2 = -1
    noDupes = False
    try:
        for t in range(0, str1):
            ic1+=1
            strTemp = []
            strTemp = treList[ic1].givecoords()
            if placementXX > strTemp[0] and placementXX < strTemp[2]:
                if placementYY > strTemp[1] and placementYY < strTemp[3]:
                    for t in range(0, len(queue)):
                        icc2+=1
                        if ic1 == queue[icc2]:
                            noDupes = True
                    if noDupes == True:
                        print "Treasure is already in wishlist"
                    else:
                        queue.append(ic1)
                        qIndex+=1
                        lstWish.insert(qIndex, (treList[ic1].valName, ' ', ic1))
                        noDupes = False
    except IndexError:
        pass

#creates right click menu
menu = Menu(root, tearoff=0)
menu.add_command(label="Set as Bronze", command=setB)
menu.add_command(label="Set as Silver", command=setS)
menu.add_command(label="Set as Gold", command=setG)
menu.add_command(label="Add to wishlist", command=add_to_wishlist)

#i'm watching a documentary about cars
#it's awesome
#whoops getting off track here
#i don't think this is used anymore
#hold on lemme check
#yeah it's not used anymore
def changeVal():
    global icc
    global val
    global colour
    icc+=1
    if icc == 1:
        print("Treasure now has the value of 1")
        #if tkMessageBox.showinfo("Treasure Value Changed!", "The value of this treasure is now 1"):
        #    pass
        val = 1
        colour = 'brown'
    elif icc == 2:
        print("Treasure now has the value of 2")
        #if tkMessageBox.showinfo("Treasure Value Changed!", "The value of this treasure is now 2"):
        #    pass
        val = 2
        colour = 'grey'
    elif icc == 3:
        print("Treasure now has the value of 3")
        #if tkMessageBox.showinfo("Treasure Value Changed!", "The value of this treasure is now 3"):
        #    pass
        icc = 0
        val = 3
        colour = 'yellow'
    return val, colour

#stops the user from placing a tre on top of another tre
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

#unused
def printCoord(event):
    print event.x
    print event.y

#loops 15 times and creates tre's with bullshit coords
def setTraps():
    global ListTrap
    ListTrap = []
    for t in range(0, 15):
        trap1 = Traps()
        ListTrap.append(trap1)
    return ListTrap

#sets the left click to placing a tre
canvas.bind("<Button-1>", PlaceOB)
#sets the right click to the popup menu
canvas.bind("<Button-3>", popup)

#unused i think
def updateTre(i,storeTre2):
    treList.insert(i,storeTre2)
    return treList

#puts the tre into a list
def nextTreasure(storeTre):
    global treList
    treList.append(storeTre)
    return treList

#idek
def sortChoice():
    pass

#just read the variable names, you'll know what this is
greenTraffic = canvas.create_oval(3,29,3+10,29+10,fill = 'green')
amberTraffic = canvas.create_oval(3,17,3+10,17+10,fill = 'black')
redTraffic = canvas.create_oval(3,5,3+10,5+10,fill = 'black')

#creates text
textWarning = canvas.create_text(600, 40, anchor=NE, text=".", fill='black')



###----------Buttons----------###

#Start Robot and CountdownTimer#

#creates robot
def displayUFO():
    global once
    if once == True:
        once = False
        setTraps()
        DisplayTimer1=DisplayTimer()
        robot1 = Robot(20,20,treList)
        robot1.movement(canvas)
    else:
        pass

Button(text="Start", cursor="trek", command=displayUFO).pack(side=LEFT, padx=20, pady=5)

#Exit Program#
def Exit():
    if tkMessageBox.askokcancel("Exit", "Are you sure you want to leave?"):
        if tkMessageBox.askokcancel("Exit", "Really?"):
            root.destroy()

Button(text="Exit", cursor="trek", command=Exit).pack(side=RIGHT, padx=20, pady=5)


#ask hadiyah or jay how this works because idfk
###----------CountdownTimer----------###
class DisplayTimer(tk.Tk):
    
    def __init__(self):
        tk.Tk.__init__(self)
        self.label = Label(self, text="", font=('arial black', 25), width=8)
        self.label.pack()
        self.remaining = 0
        self.countdowntimer(60)

    def countdowntimer(self, remaining = None):
        if remaining is not None:
            self.remaining = remaining

        if self.remaining <= 0:
            self.label.configure(text="Time's Up!", font=('arial black', 25), fg='red')
        else:
            self.label.configure(text="%d" % self.remaining)
            self.remaining = self.remaining - 1
            self.after(1000, self.countdowntimer)
            

#displays pop up message telling the user what they have conquered               
def treDesc():
    itn = random.randint(0, 5)
    if itn == 0:
        xXx1337h4x0rzxXx = "You have conquered Kiev!!!"
    elif itn == 1:
        xXx1337h4x0rzxXx = "You have annihilated Dnipropetrovsk"
    elif itn == 2:
        xXx1337h4x0rzxXx = "Dnipropetrovsk bows before your excellence"
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
        #Y SO MANY VARIABLES
        #robot itself
        #bleep bloop bleep
        #that was my robot impression
        #WELL FUCK YOU THEN! i thought it was a good impression
        self.treList = treList
        self.q = -1
        self.obnum = 5-1
        self.x = x
        self.y = y
        self.path1 = 0
        self.x1 = x + 20
        self.y1 = y + 20
        self.score = 0
        self.pp=0
        self.rx = (self.x1 - self.x)/2
        self.ry = (self.y1 - self.y)/2
        self.tempxy =[]
        self.sum1 = 1
        self.sum2 = 1
        self.ici=-1
        self.icci = -1
        self.valX = False
        self.qc = -1
        self.valY = False
        self.rotated = False
        self.stillSearch = True
        self.ic = 0
        self.trappedList = []
        self.varTreasure = len(self.treList)
        self.skip = skip

        robotimage_url = "http://i.imgur.com/p5w3mCP.gif"
        image2_byt = urlopen(robotimage_url).read()
        image2_b64 = base64.encodestring(image2_byt)
        self.photo2 = tk.PhotoImage(data=image2_b64)
        self.id1 = canvas.create_image(self.x,self.y, image=self.photo2)
        canvas.update()

    #not sure if used
    def newIndex(self,Index):
        self.index = Index

    #checks wishlist, if there is an item in the wishlist, then it goes to it, else go to nearest
    def check_queue(self):
        if queue == []:
            self.search()
        else:
            try:
                self.qc+=1
                self.qlen = len(queue)
                if self.qc >= self.qlen:
                    self.search()
                else:
                    self.treListIndex = queue[self.qc]
                    skip.append(queue[self.qc])
                    self.qSearch()
            except IndexError:
                self.qc+=1
                self.treListIndex = queue[self.qc]
                self.qSearch()
               

    #removes treasure from listbox if trap is hit
    #also fucks with your score
    #and sister
    #i hate this function
    #YOU STAY AWAY FROM MY SISTER YOU ASSHOLE
    def removeFrom(self):
        if lstCol.get(self.ici) == "":
            pass
        elif self.ici < 0:
            pass
        else:
            if lstCol.get(self.ici) == "Random treasure":
                self.score-=50
            if lstCol.get(self.ici) == "Bronze Value Treasure":
                self.score-=100
            if lstCol.get(self.ici) == "Silver Value Treasure":
                self.score-=250
            if lstCol.get(self.ici) == "Gold Value Treasure":
                self.score-=500
            lstCol.delete(self.ici)
            self.ici-=1
            self.trapScen()

    #if the robot collects the tre, it adds it to the listbox
    #and gives you score
    #and a hug
    #this function is nicer than the last one
    def addTo(self):
        self.ici+=1
        if treList[self.treListIndex].val == 0:
            lstCol.insert(self.ici, "Random treasure")
            self.score+=50
        elif treList[self.treListIndex].val == 1:
            lstCol.insert(self.ici, "Bronze Value Treasure")
            self.score+=100
        elif treList[self.treListIndex].val == 2:
            lstCol.insert(self.ici, "Silver Value Treasure")
            self.score+=250
        elif treList[self.treListIndex].val == 3:
            lstCol.insert(self.ici, "Gold Value Treasure")
            self.score+=500
            
    #this is the code that makes the robot move to the nearest coord
    #trying to explain this will be a nightmare
    #here we go
    #wish me luck
    def wishList(self):
        #gets robot coords and store in local variable
        self.xRo = self.x
        self.yRo = self.y
        #not sure
        self.ic2 = -1
        #finds out how many tre's
        self.str1 = len(treList)
        #declares data dickshunary
        self.sortedNodePath = []
        #this is a boolean i think
        self.fake = False
        #not sure
        self.ic1 = -1
        #declares more data dick's
        self.nodePathList = []
        self.trappedList = []
        #makes local numbers
        self.lenX = 0
        self.lenY = 0
        #loops for ever tre
        for t in range(0, self.str1):
            #i forgot
            self.ic1+=1
            #this data dick will store the tre coords for every loop
            #i put it in the loop because it needs to be reset after every loop
            self.strTemp = []
            #forgot again
            self.count=-1
            #skip is the list of tre's that have already been collected. if non has been collected, then perform as normal
            if skip == []:
                self.strTemp = treList[self.ic1].givecoords()
            #if not, find out if the loop is now on the treasure that is in skip
            else:
                self.lenSkip = len(skip)
                for t in range(0, self.lenSkip):
                    self.count+=1
                    if self.ic1 == skip[self.count]:
                        self.fake = True
                    else:
                        self.strTemp = treList[self.ic1].givecoords()
            #self.fake becomes true if the tre is already collected
            #it tricks the code into thinking that the tre's coords are 5000x5000
            if self.fake == True:
                self.lenX = 5000
                self.lenY = 5000
            #if self.fake is false (the tre hasn't been collected yet) then perform this
            else:
                #sets the variables to the coord of the tre - robot coords
                #this then tells you how many pixels it takes to reach that tre
                self.lenX = (self.xRo - self.strTemp[0])
                self.lenY = (self.yRo - self.strTemp[1])
                if self.lenX < 0:
                    self.lenX = (self.strTemp[0] - self.xRo)
                if self.lenY < 0:
                    self.lenY = (self.strTemp[1] - self.yRo)
            #sets self.fake to be false for the next loop
            self.fake = False
            #adds the pixel count of the tre into a list for every loop
            self.nodePathList.append(self.lenX+self.lenY)
        #this copies the data of the pixel count list into a new list
        self.sortedNodePath = copy.copy(self.nodePathList)
        #this bubble sorts self.sortednodepath
        for passnum in range(len(self.sortedNodePath)-1,0,-1):
            for i in range(passnum):
                if self.sortedNodePath[i]>self.sortedNodePath[i+1]:
                    self.temp = self.sortedNodePath[i]
                    self.sortedNodePath[i] = self.sortedNodePath[i+1]
                    self.sortedNodePath[i+1] = self.temp
        #takes the 1st index of the sorted list
        #because that's the tre with the shorted distance
        self.shortestPath = self.sortedNodePath[0]
        #loops for tre
        for t in range(0, self.str1):
            #counts, on first loop this is 0
            self.ic2+=1
            #checks if the 1st index of the sorted pixel count list matches any index of the unsorted pixel count list
            if self.shortestPath == self.nodePathList[self.ic2]:
                #if it does match then it will take the index of the unsorted pixel count list
                #the index represents the tre with the smallest distance
                #yes there was no other way to do this other than this massive function
                #sets self.treListIndex to be the tre with the smallest distance
                self.treListIndex = self.ic2
                #adds that tre to skip so that the robot won't go to it again
                skip.append(self.treListIndex)
                

    #this checks if the robot is trapped
    #basically takes the robot coords and checks if it's within a trap
    def check_if_trapped(self):
        self.length = len(ListTrap)
        self.icci = -1
        self.fake2 = False
        for t in range(0, self.length):
            self.tempCoord = []
            self.icci+=1
            self.counting = -1
            if trappedList == []:
                pass
            else:
                for t in range(0, len(trappedList)):
                    self.counting+=1
                    if self.icci == trappedList[self.counting]:
                        self.fake2 = True
            if self.fake2 == True:
                self.fake2=False
            else:
                self.tempCoord = ListTrap[self.icci].givecoords()
                if self.x > self.tempCoord[0] and self.x < self.tempCoord[2]:
                    if self.y > self.tempCoord[1] and self.y < self.tempCoord[3]:
                        trappedList.append(self.icci)
                        self.removeFrom()

    #popup message if trapped      
    def trapScen(self):
        self.itn = random.randint(0, 5)
        if self.itn == 0:
            self.xXx1337h4x0rzxXx = "a tank malfunction caused you to be robbed by locals of ukraine, you have been robbed of 1 treasure"
        elif self.itn == 1:
            self.xXx1337h4x0rzxXx = "a pot hole caused you to drop a treasure without realizing"
        elif self.itn == 2:
            self.xXx1337h4x0rzxXx = "a traitor within your convoy has ran off with one of your treasures"
        elif self.itn == 3:
            self.xXx1337h4x0rzxXx = "the wildlife animals have surrounded you, oh no! a wolf has taken off with one of your treasures"
        elif self.itn == 4:
            self.xXx1337h4x0rzxXx = "a street dealer offers you top dollar for one of your treasures, as soon as you handed him the treasure he ran off with it"
        elif self.itn == 5:
            self.xXx1337h4x0rzxXx = "whilst camping for the night, a group of locals raided your stash, you have lost 1 treasure"
        if tkMessageBox.showinfo("Oh no!!! you have been trapped, ", self.xXx1337h4x0rzxXx):
            pass

    #this will end the code if the last treasure is collected
    def EndCheck(self):
        self.ic+=1

        if self.ic == self.varTreasure:
            self.stillSearch = False
            if tkMessageBox.showinfo("Congratulations!!! ", ("your score is: ", self.score)):
                pass
        else:
            self.check_queue()

    #this creates a small hitbox within the tre for the robot to get to
    def search(self):  
        try:
            self.wishList()
            LMcoordtemp = treList[self.treListIndex].givecoords()
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

    #same as last but for wishlist items
    def qSearch(self):
        try:
            LMcoordtemp = treList[self.treListIndex].givecoords()
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

    #unused    
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center

    #this is the actual movement itself
    def movement(self,canvas):
        global counting
        counting = 1

        global sleeping
        sleeping = 1

        global lightchange    
        lightchange = 1

        #checks wishlist
        self.check_queue()

        #sets the destination to the hitbox
        dest = self.destxy
        #sets coords of robot
        self.current_coord = (self.x,self.y)

        #this the movement algorithm
        #if the x and y coord doesnt match the destination coords
        #+1 to robot's x and y
        #or -1, which ever gets the robot closest
        #if the x coord matches the x coord of the destination then only move y
        #same with the y coord
        #if both x and y match the destination then the tre is collected
        #and the cycle continues
        #this also refers to a lot of the previous functions so
        #check the comments on those if you don't know why it's calling that function
        while self.stillSearch == True:
            if self.valX == True and self.valY == True:
                self.addTo()
                #skip.append(self.treListIndex)
                self.EndCheck()
                treDesc()
                self.search
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
                self.check_if_trapped()      
                self.y+=self.sum2
                self.x+=self.sum1
                self.x1 = self.x + 20
                self.y1 = self.y +20
                self.current_coord = (self.x,self.y)
                canvas.coords(self.id1, self.current_coord)
                canvas.update()
                
            if sleeping == 1:
               time.sleep(0.02)
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
                canvas.itemconfigure(textWarning, text="Military checkpoint incoming!!!", fill='black')
            
            elif lightchange == 3:
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(amberTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 3
                canvas.itemconfigure(textWarning, text="Military checkpoint", fill='black')

            elif lightchange == 4:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 2
#FINALLY, TIME FOR SLEEP
                


root.mainloop()
