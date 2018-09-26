import numpy as np
import time
from time import sleep
from tkinter import *
import random

w_min = 0
w_max = 1920
h_min = 0
h_max = 1080

r = random.randint(1,100)
c_r = random.randint(0,15)
count = 0

tk = Tk()
tk.attributes('-fullscreen', True)
tk.attributes('-topmost', True)
tk.bind('<Escape>',lambda e: tk.destroy())

w = Canvas(tk, width=1920, height=1080, background='white',bg='white')     #Canvas Resolution
w.pack()

#coordinates for signal status
sig = np.array([[395,455,425,485],
                [535,455,565,485],
                [535,595,565,625],
                [395,595,425,625],
                [875,455,905,485],
                [1015,455,1045,485],
                [1015,595,1045,625],
                [875,595,905,625],
                [1355,455,1385,485],
                [1495,455,1525,485],
                [1495,595,1525,625],
                [1355,595,1385,625],])

s1 = [60,90,120,60]
s2 = [90,120,120,90]
s3 = [120,60,160,120]


source = np.array([[0,523,14,537],
                 [0,503,14,517],
                 [483,0,497,14],
                 [503,0,517,14],
                 [963,0,977,14],
                 [983,0,997,14],
                 [1443,0,1457,14],
                 [1463,0,1477,14],
                 [1906,543,1920,557],
                 [1906,563,1920,577],
                 [1423,1066,1437,1080],
                 [1403,1066,1417,1080],
                 [943,1066,957,1080],
                 [923,1066,937,1080],
                 [463,1066,477,1080],
                 [443,1066,457,1080]])

destination = np.array([[0,563,14,577],
                        [0,543,14,557],
                        [443,0,457,14],
                        [463,0,477,14],
                        [923,0,937,14],
                        [943,0,957,14],
                        [1403,0,1417,14],
                        [1423,0,1437,14],
                        [1906,503,1920,517],
                        [1906,523,1920,537],
                        [1463,1066,1477,1080],
                        [1443,1066,1457,1080],
                        [983,1066,997,1080],
                        [963,1066,977,1080],
                        [503,1066,517,1080],
                        [483,1066,497,1080]])

stop = np.array([[440,500,440,540],
                 [480,500,520,500],
                 [520,540,520,580],
                 [440,580,480,580],
                 [920,500,920,540],
                 [960,500,1000,500],
                 [1000,540,1000,580],
                 [920,580,960,580],
                 [1400,500,1400,540],
                 [1440,500,1480,500],
                 [1480,540,1480,580],
                 [1400,580,1440,580]])

stopLine_x = [440,520,920,1000,1400,1480]
stopLine_y = [500,580]

#functions        
def roads():

    #load divider
    w.create_line(0, 540, 1920, 540, fill="black", dash=(4,4))
    w.create_line(480, 0, 480, 1080, fill="black", dash=(4,4))
    w.create_line(960, 0, 960, 1080, fill="black", dash=(4,4))
    w.create_line(1440, 0, 1440, 1080, fill="black", dash=(4,4))

    #main lane
    w.create_line(0, 500, 440, 500, fill="blue")
    w.create_line(0, 580, 440, 580, fill="blue")
    
    #lane 1
    w.create_line(440, 0, 440, 500, fill="blue")
    w.create_line(440, 580, 440, 1080, fill="blue")

    w.create_line(520, 0, 520, 500, fill="blue")
    w.create_line(520, 580, 520, 1080, fill="blue")

    w.create_line(520, 500, 920, 500, fill="blue")
    w.create_line(520, 580, 920, 580, fill="blue")

    #lane 2
    w.create_line(920, 0, 920, 500, fill="blue")
    w.create_line(920, 580, 920, 1080, fill="blue")

    w.create_line(1000, 0, 1000, 500, fill="blue")
    w.create_line(1000, 580, 1000, 1080, fill="blue")

    w.create_line(1000, 500, 1400, 500, fill="blue")
    w.create_line(1000, 580, 1400, 580, fill="blue")

    #lane 3
    w.create_line(1400, 0, 1400, 500, fill="blue")
    w.create_line(1400, 580, 1400, 1080, fill="blue")

    w.create_line(1480, 0, 1480, 500, fill="blue")
    w.create_line(1480, 580, 1480, 1080, fill="blue")


    w.create_line(1480, 500, 1920, 500, fill="blue")
    w.create_line(1480, 580, 1920, 580, fill="blue")

    #stopline
    w.create_line(440,500,440,540, fill="red")
    w.create_line(480,500,520,500, fill="red")
    w.create_line(520,540,520,580, fill="red")
    w.create_line(440,580,480,580, fill="red")

    w.create_line(920,500,920,540, fill="red")
    w.create_line(960,500,1000,500, fill="red")
    w.create_line(1000,540,1000,580, fill="red")
    w.create_line(920,580,960,580, fill="red")

    w.create_line(1400,500,1400,540, fill="red")
    w.create_line(1440,500,1480,500, fill="red")
    w.create_line(1480,540,1480,580, fill="red")
    w.create_line(1400,580,1440,580, fill="red")






def signal_box():
    
    #coordinates for signal box
    #junction 1
    w.create_rectangle(390,450,430,490)
    w.create_rectangle(390,590,430,630)
    w.create_rectangle(530,450,570,490)
    w.create_rectangle(530,590,570,630)
    
    #junction 2
    w.create_rectangle(870,450,910,490)
    w.create_rectangle(870,590,910,630)
    w.create_rectangle(1010,450,1050,490)
    w.create_rectangle(1010,590,1050,630)
    
    #junction 3
    w.create_rectangle(1350,450,1390,490)
    w.create_rectangle(1350,590,1390,630)
    w.create_rectangle(1490,450,1530,490)
    w.create_rectangle(1490,590,1530,630)


#classes
class Signals:


    def __init__(self, coordinates):
        self.x0 = coordinates[0]
        self.y0 = coordinates[1]
        self.x1 = coordinates[2]
        self.y1 = coordinates[3]
        self.light()

    #signal status updater
    def light(self, status='red'):
        self.status = status
        w.create_oval(self.x0, self.y0, self.x1, self.y1, fill=self.status)
        tk.update()

    def stat(self):
        return self.status=='green'

class Junction:

    def __init__(self, obj, s, stop_x, stop_y):
        self.i = 0
        self.obj = obj
        self.s = np.copy(s)
        self.sig = np.copy(self.s)
        self.stat = [0,0,0,0]
        self.stop_x = np.copy(stop_x)
        self.stop_y = np.copy(stop_y)



    def change(self):
        if self.sig[self.i] > 0:
            self.obj[self.i].light(status='green')
            self.sig[self.i] -= 1

        else:
            self.obj[self.i].light()
            self.i += 1
            if self.i == len(self.sig):
                self.i = 0
                self.sig = np.copy(self.s)

            

    def status(self):
        for i in range(4):
            self.stat[i] = self.obj[i].stat()
        print(self.stat)




class Car:
    #def __init__(self, coordinates, color):
    def __init__(self, src, color):
        self.coord_x = []
        self.coord_y = []
        self.z = random.randint(1,11)
        # self.coord_x.append(coordinates[0])
        # self.coord_y.append(coordinates[1])
        # self.coord_x.append(coordinates[2])
        # self.coord_y.append(coordinates[3])
        self.color = color
        self.coord_src = np.copy(src)
        self.coo_src = np.copy(src)
        self.flag = [0,0,0,0]
        self.ret = 0
        

        self.coord_x.append(self.coord_src[0])
        self.coord_y.append(self.coord_src[1])
        self.coord_x.append(self.coord_src[2])
        self.coord_y.append(self.coord_src[3])

        self.car = w.create_rectangle(self.coord_x[0], self.coord_y[0], self.coord_x[1], self.coord_y[1], fill=self.color)

        # 
        tk.update()

    def __del__(self):
        pass

    # def begin(self):


    def front(self):
        if self.coord_x[0] <= 1920:
            if (self.coord_x[0]+15 == stopLine_x[0]-1 and s[0].stat()==False) or (self.coord_x[0]+15 == stopLine_x[2]-1 and s[4].stat()==False) or (self.coord_x[0]+15 == stopLine_x[4]-1 and s[8].stat()==False):
                pass
            else:    
                w.coords(self.car, self.coord_x[0], self.coord_y[0], self.coord_x[0]+15, self.coord_y[1])
                self.coord_x = [x + 1 for x in self.coord_x]

        if self.coord_x[0] == 1920:
            self.ret = 1


    def back(self):
        if self.coord_x[0] >= 0:
            if (self.coord_x[0]-15 == stopLine_x[1]-1 and s[2].stat()==False) or (self.coord_x[0]-15 == stopLine_x[3]-1 and s[6].stat()==False) or (self.coord_x[0]-15 == stopLine_x[5]-1 and s[10].stat()==False):
                pass
            else:
                w.coords(self.car, self.coord_x[0], self.coord_y[0], self.coord_x[0]-15, self.coord_y[1])
                self.coord_x = [x - 1 for x in self.coord_x]

        if self.coord_x[0] == 0:
            self.ret = 1
        

    def top(self):
        if self.coord_y[0] >= 0:
            if self.coord_y[0]-15 == stopLine_y[1]-1 and ((self.coord_x[0] <= stopLine_x[1] and s[3].stat()==False) or (self.coord_x[0] >= stopLine_x[2] and self.coord_x[0] <= stopLine_x[3] and s[7].stat()==False) or (self.coord_x[0] >= stopLine_x[4] and s[11].stat()==False)):
                pass
            else:
                w.coords(self.car, self.coord_x[0], self.coord_y[0], self.coord_x[1], self.coord_y[0]-15)
                self.coord_y = [y - 1 for y in self.coord_y]

        if self.coord_y[0] == 0:
            self.ret = 1
        

    def bottom(self):
        if self.coord_y[0] <= 1080:
            if self.coord_y[0]+15 == stopLine_y[0]-1 and ((self.coord_x[0] <= stopLine_x[1] and s[1].stat()==False) or (self.coord_x[0] >= stopLine_x[2] and self.coord_x[0] <= stopLine_x[3] and s[5].stat()==False) or (self.coord_x[0] >= stopLine_x[4] and s[9].stat()==False)):
                pass
            else:
                w.coords(self.car, self.coord_x[0], self.coord_y[0], self.coord_x[1], self.coord_y[0]+15)
                self.coord_y = [y + 1 for y in self.coord_y]

        if self.coord_y[0] == 1080:
            self.ret = 1

    def move(self):
        if (self.coord_x[0] == 443 or self.coord_x[0] == 463 or self.coord_x[0] == 923 or self.coord_x[0] == 943 or self.coord_x[0] == 1403 or self.coord_x[0] == 1423) and (self.coord_y[0] == 503 or self.coord_y[0] == 523):
            
            self.z = random.randint(1,11)

            if self.z <= 5:
                self.flag = [0,0,0,1]

            else:
                self.flag = [1,0,0,0]

            self.coo_src[0] = self.coord_x[0] 
            self.coo_src[2] = self.coord_x[1] 
            self.coo_src[1] = self.coord_y[0] 
            self.coo_src[3] = self.coord_y[1] 

        elif (self.coord_x[0] == 483 or self.coord_x[0] == 503 or self.coord_x[0] == 963 or self.coord_x[0] == 983 or self.coord_x[0] == 1443 or self.coord_x[0] == 1463) and (self.coord_y[0] == 543 or self.coord_y[0] == 563):
            
            self.z = random.randint(1,11)

            if self.z <= 5:
                self.flag = [0,0,1,0]
            
            else:
                self.flag = [0,1,0,0]

            self.coo_src[0] = self.coord_x[0] 
            self.coo_src[2] = self.coord_x[1] 
            self.coo_src[1] = self.coord_y[0] 
            self.coo_src[3] = self.coord_y[1] 

        elif (self.coord_x[0] == 483 or self.coord_x[0] == 503 or self.coord_x[0] == 963 or self.coord_x[0] == 983 or self.coord_x[0] == 1443 or self.coord_x[0] == 1463) and (self.coord_y[0] == 503 or self.coord_y[0] == 523):
            
            self.z = random.randint(1,11)

            if self.z <= 5:
                self.flag = [1,0,0,0]
            
            else:
                self.flag = [0,0,1,0]

            self.coo_src[0] = self.coord_x[0] 
            self.coo_src[2] = self.coord_x[1] 
            self.coo_src[1] = self.coord_y[0] 
            self.coo_src[3] = self.coord_y[1] 

        elif (self.coord_x[0] == 443 or self.coord_x[0] == 463 or self.coord_x[0] == 923 or self.coord_x[0] == 943 or self.coord_x[0] == 1403 or self.coord_x[0] == 1423) and (self.coord_y[0] == 543 or self.coord_y[0] == 563):
            
            self.z = random.randint(1,11)

            if self.z <= 5:
                self.flag = [0,1,0,0]

            else:
                self.flag = [0,0,0,1]

            self.coo_src[0] = self.coord_x[0] 
            self.coo_src[2] = self.coord_x[1] 
            self.coo_src[1] = self.coord_y[0] 
            self.coo_src[3] = self.coord_y[1] 

        else:
            if self.coo_src[0] == 0:
                self.flag = [1,0,0,0]

            if self.coo_src[2] == 1920:
                self.flag = [0,1,0,0]

            if self.coo_src[1] == 0:
                self.flag = [0,0,1,0]

            if self.coo_src[3] == 1080:
                self.flag = [0,0,0,1]

        if self.flag[0] == 1:
            self.front()
        elif self.flag[1] == 1:
            self.back()
        elif self.flag[2] == 1:
            self.bottom()
        elif self.flag[3] == 1:
            self.top()

        return self.ret


        


        


roads()
signal_box()

s = []
for i in range(12):
    s.append(Signals(sig[i]))


c = []
c.append(Car(source[0],'magenta'))
c.append(Car(source[1],'magenta'))
c.append(Car(source[2],'magenta'))
c.append(Car(source[3],'magenta'))
c.append(Car(source[4],'magenta'))
c.append(Car(source[5],'magenta'))
c.append(Car(source[6],'magenta'))
c.append(Car(source[7],'magenta'))
c.append(Car(source[8],'magenta'))
c.append(Car(source[9],'magenta'))
c.append(Car(source[10],'magenta'))
c.append(Car(source[11],'magenta'))
c.append(Car(source[12],'magenta'))
c.append(Car(source[13],'magenta'))
c.append(Car(source[14],'magenta'))
c.append(Car(source[15],'magenta'))




sig1 = Junction(s[0:4], s1, stopLine_x[0:2], stopLine_y)
sig2 = Junction(s[4:8], s2, stopLine_x[2:4], stopLine_y)
sig3 = Junction(s[8:12], s3, stopLine_x[4:6], stopLine_y)

while(True):
    
    if count == r:
        c.append(Car(source[c_r],'magenta'))
        r = random.randint(1,100)
        c_r = random.randint(0,15)
        count = 0
    count = count + 1
    sig1.change()
    sig2.change()
    sig3.change()
    for i in c:
        ret = i.move()
        if ret == 1:
            del i
       
    tk.update()
    time.sleep(0.001)
    print(len(c))



time.sleep(2)

tk.destroy()


# while(destination == 0)
# {
    
# }
tk.mainloop()