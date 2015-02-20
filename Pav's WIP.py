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
global coord1
global coord2
global treasureList
treasureList = []
#global configure
#global tList
#global tre1, tre2, tre3, tre4, tre5, tre6, tre7, tre8, tre9, tre10, tre11
#tList=[]
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
#print(xpos, ypos)
canvas.create_image(xpos, ypos, image=photo)
canvas.pack()

class Treasure(object):
    def __init__(self,xx,yy):
        self.treList = []
        self.xx=xx
        self.yy=yy
        self.tre = canvas.create_rectangle(self.xx,self.yy,self.xx+50,self.yy+50,fill='white')
        
    def coordChange(self,xx,yy):
        self.xx=xx
        self.yy=yy
        canvas.coords(self.tre,self.xx,self.yy,self.xx+50,self.yy+50)
        canvas.update()
                      
    def nextTre(self,i):
        self.i=i
        self.treList.append(self.tre)
        return self.treList

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
    #    canvas.coords(configure,xx,yy,xx+10,yy+10)
    #    canvas.update()
        treasure1.coordChange(xx,yy)
        return xx, yy

buttonSet=Button(root, text='set', command=coordSet)
buttonSet.pack(side=LEFT)

def randCoord():
    xx = random.randint(0, 640)
    yy = random.randint(0, 640)
    #canvas.coords(configure, xx, yy, xx+10, yy+10)
    #canvas.update()
    treasure1.coordChange(xx,yy)
    return xx, yy

btnRand=Button(root, text='Randomize', command=randCoord)
btnRand.pack(side=LEFT)

treasureValue=Listbox(root, selectmode=SINGLE, width=6, height=3)
treasureValue.insert(1, 'Bronze')
treasureValue.insert(2, 'Silver')
treasureValue.insert(3, 'Gold')
treasureValue.pack(side=LEFT)


def newTre():
    global i
    global treasure1
    treasure1.nextTre(i)
    treasure1 = Treasure(360,240)
    i+=1
   # global tre1, tre2, tre3, tre4, tre5, tre6, tre7, tre8, tre9, tre10, tre11

def varNext():
    global oneShot2
    global treasureList
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
    return oneShot2
   
buttonNext=Button(root, text='Next', command=varNext)
buttonNext.pack(side=LEFT)

wishlist = Listbox(root, selectmode=MULTIPLE, width=7, height=4)
wishlist.insert(1, 'All')
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
    robot1 = Robot(20,20)
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


            
###----------Robot----------###

class Robot(object):


    def __init__(self, x, y):
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
        self.rotated = False
        

      

        ##Call the method search
        self.search()

        robotimage_url = "http://i.imgur.com/zR2sDWw.gif"
        image2_byt = urlopen(robotimage_url).read()
        image2_b64 = base64.encodestring(image2_byt)
        self.photo2 = tk.PhotoImage(data=image2_b64)
        self.id1 = canvas.create_image(self.x,self.y, image=self.photo2)
        canvas.update()

       # self.z = canvas.create_line(self.x+10,self.y+10,self.x+100,self.x+100)
       # self.rr = self.returncenter()


    ##The search method decides what LandMarks need to be visited and avoided
    def search(self):
        self.q += 1


        ###this needs work

        
        LMcoordtemp = treList[self.q].givecoords()
        destx = LMcoordtemp[2] - LMcoordtemp[0]
        destx = destx/2
        destx = destx+LMcoordtemp[0]
        desty = LMcoordtemp[3] - LMcoordtemp[1]
        desty = desty/2
        desty = desty + LMcoordtemp[1]
        self.destxy = [destx,desty]
        self.search()

    ##Not really used finds the center on the robots oval
    def returncenter(self):
        self.center = self.x + self.rx, self.y + self.ry
        return self.center




    ##Looks at the end of the LookAhead vector to determin whether the robot need to avoid anything or not
    def LookAhead(self):
            unit = self.vec1.unit()
            #print "From Look ", unit
            self.xAhead = self.x + unit[0]*70
            self.yAhead = self.y + unit[1]*70

            canvas.coords(self.z,self.x+10,self.y+10,self.xAhead,self.yAhead)

            i=0
            ###########x,x1,y,y1############
            for i in range (0,self.obnum):
                if self.LMList[i].havetresure() == False and self.xAhead >= self.listx[i] and self.xAhead <= self.listx2[i] and self.yAhead >= self.listy[i]  and self.yAhead <= self.listy2[i]:
                    
                    #print "Hit the sqr"
                    self.rotated = self.vec1.rotate(90)
                    canvas.update
            else:
                pass
    ##Move from a to b
    ##This function is to move our robot while continually call look ahead
    def movement(self,canvas):
        dest = self.destxy
        self.rr = self.returncenter()
        self.vec1 = vector(self.rr,dest)
        #canvas.create_line(self.rr,dest)
        end = []
        dist = self.vec1.distance()
        i = 0

        global counting
        counting = 1

        global sleeping
        sleeping = 1

        global lightchange    
        lightchange = 1

        while i <= dist:
            #print dist
            i+= 1
            sum1 = self.vec1.unit()
            self.LookAhead()
            
##################################################################
                
            if sleeping == 1:
               time.sleep(0.01)
            elif sleeping == 2:
                time.sleep(0.07)
            elif sleeping == 3:
                time.sleep(1.0)

            counting += 1

        
            if counting == 1:
                lightchange = 4
            elif counting == 5:
                lightchange = 1

            if counting == 90:
                lightchange = 2
            elif counting == 110:
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
                #print "Stop"

            elif lightchange == 4:
                canvas.itemconfigure(amberTraffic, fill = 'yellow')
                canvas.itemconfigure(greenTraffic, fill = 'black')
                canvas.itemconfigure(redTraffic, fill = 'red')
                sleeping = 2
            
###############################################################################
            
            if self.rr == dest:
                #print "FUFUFUFU:LASJFJSLKNFQQNOFNPIFQ"
                dest[0] = tempxdest
                dest[1] = tempydest
                
                self.vec1 = vector(self.rr,dest)
                
                dist = self.vec1.distance()
                i=0
                #dist = self.vec1.distance()
            #print "HI", self.y
            self.y+=sum1[1]
            self.x+=sum1[0]
            self.x1 = self.x + 20
            self.y1 = self.y +20 
            #self.current_coord = (self.x,self.y,self.x1,self.y1)
            self.current_coord = (self.x,self.y)

            
            enddest1 = dest[0]
            enddest2  = dest[1]
            finalenddest = int(enddest1),int(enddest2)
            current1 = self.x
            current2 = self.y
            finalcurrent = int(current1)+10,int(current2)+10
            #print finalenddest
            #print finalcurrent
            #print "yy"
  
            ####need to create a small square
            var1= self.destxy[0]+1
            var2= self.destxy[0]-1
            var3= self.destxy[1]+1
            var4= self.destxy[1]-1
            if self.rotated == True:
                #print "Nothing to see here..."
                tempxdest = dest[0]
                tempydest = dest[1]
                tempxy = dest
                self.LookAhead()
                dest[0] = self.xAhead
                dest[1] = self.yAhead
                self.rr= (self.x,self.y)
                
                self.vec2 = vector(self.rr,dest)
                
                end = self.vec2.returnend()
                dist = self.vec2.distance()
                #print dist
                i=0
                for x in range(0,int(dist)):
                    sum2 = self.vec2.unit()
                    #print"This is sum2 ", sum2
                    self.y+=sum2[1]
                    self.x+=sum2[0]
                    self.x1 = self.x + 20
                    self.y1 = self.y +20 
                    self.current_coord = (self.x,self.y)
                    canvas.coords(self.z,self.x+10,self.y+10,self.xAhead,self.yAhead)
                    canvas.coords(self.id1, self.current_coord)
                    canvas.update()
                    time.sleep(0.01)
                    dist = 0
                self.q = self.q -1
                    #dest = tempxy
                self.rotated = False
                self.movement(canvas)
            
            if finalcurrent[0] >= var2 and finalcurrent[0] <= var1 and finalcurrent[1] >= var4  and finalcurrent[1] <= var3:
                #print "Of course it worked i never doubted it!"
                self.search()
                self.movement(canvas)
            print end
            if self.rr == end:
                print "Or here..."
                
                           
            canvas.coords(self.id1, self.current_coord)
            canvas.update()
            
            
            time.sleep(0.01)


## class that deals with all land marks
class LandMark:
    def __init__(self,x,x1,y,y1,fill,tresure):
        self.x = x
        self.x1= x1
        self.y = y
        self.y1 = y1
        self.colour = fill
        self.visitmaybe = tresure
        
    
    def CreateLM(self):
        canvas.create_rectangle(self.x,self.x1,self.y,self.y1,fill = self.colour)        
    def givecoords(self):
        return self.x,self.x1,self.y,self.y1

    def havetresure(self):
        if self.visitmaybe == True:
            return True
            
        else:
            return False



class vector():
    def __init__(self,list1,list2):
        self.list2 = list2
        self.diff = [list2[0] - list1[0], list2[1] - list1[1]]
        

    def distance(self):
        self.a = self.diff[0]
        self.b = self.diff[1]
        return math.sqrt(self.a**2 + self.b**2)

    def unit(self): 
        distance = self.distance()
        self.aunit = self.a/distance
        self.bunit = self.b/distance

        return self.aunit, self.bunit

    def rotate(self,angle):
        oldx = self.diff[0]
        oldy = self.diff[1]

        newx = oldx*math.cos(angle)-oldy*math.sin(angle)
        newy = oldx*math.sin(angle)+oldy*math.cos(angle)

        self.diff = (newx, newy)
        return True
    def returnend(self):
        return self.list2




#robot1 = Robot(20,20)
#robot1.movement(canvas)


root.mainloop()
