from  p5 import *
import random as ra
import time as T
def setup():
    size(800,800)
    rectMode('CENTER')
    global start, using, end,rods,N,n,j,drawings
    start = []
    using = []
    end = []
    rods = []
    drawings = []
    N = 0
    n = 2
    j = 0
    for i in range(n):
        start.append(Discs(n-i,1))  
    drawings.append([start,using,end])
    for i in range(1,4):
        rods.append(Rods(i))
    print(drawings)
    hanoi(n,start,end,using)
def draw():
    background(220)
    global start,using,end,rods,N,n,j,drawings
    for i in range(len(rods)):
        fill(rods[i].color)
        rect(rods[i].position*200,800-(rods[i].size/2),30,rods[i].size)
    
   # for i in range(len(drawings[j][0])):
    #    fill(start[i].color[0],start[i].color[1],start[i].color[2])
     #   rect(1*200,800-((i+0.5)*start[i].height),start[i].width,start[i].height)   
    #for i in range(len(drawings[j][1])):
     #   fill(using[i].color[0],using[i].color[1],using[i].color[2])
      #  rect(2*200,800-((i+0.5)*using[i].height),using[i].width,using[i].height)
    #for i in range(len(drawings[j][2])):
     #   fill(end[i].color[0],end[i].color[1],end[i].color[2])
      #  rect(3*200,800-((i+0.5)*end[i].height),end[i].width,end[i].height)
    if frame_count % 60 == 0:
        j += 1
        if j == len(drawings):
            j = 0


   
    #for i in range(len(start)):
     #   fill(start[i].color[0],start[i].color[1],start[i].color[2])
      #  rect(1*200,800-((i+0.5)*start[i].height),start[i].width,start[i].height)
#    for i in range(len(using)):
 #       fill(using[i].color[0],using[i].color[1],using[i].color[2])
  #      rect(2*200,800-((i+0.5)*using[i].height),using[i].width,using[i].height)
   # for i in range(len(end)):
    #    fill(end[i].color[0],end[i].color[1],end[i].color[2])
     #   rect(3*200,800-((i+0.5)*end[i].height),end[i].width,end[i].height)
    

def hanoi(n,s,e,u):
    global N,drawings,start,using,end
    if n == 1:
        #print(f"Move {n} from {start} to {end}")
        e.append(s[-1])
        s.pop()
        print(f"Skal til at flytte i {drawings}")
        drawings.append([0,0,0])
        drawings[-1][0] = start
        drawings[-1][1] = using
        drawings[-1][2] = end
        #drawings.append([start,using,end])
        print(f"Har flyttet rundt på {drawings}")
        N +=1
        return
    hanoi(n-1,s,u,e)
    #print(f"Move {n} from {start} to {end}")
    e.append(s[-1])
    s.pop()
    print(f"Skal til at flytte i {drawings}")
    drawings.append(0)
    drawings[-1][0] = start
    drawings[-1][1] = using
    drawings[-1][2] = end
    #drawings.append([start,using,end])
    print(f"Har flyttet rundt på {drawings}")
    N += 1
    hanoi(n-1,u,e,s)

class Discs:
    def __init__(self,width,position):
        self.width = 80*(width**0.9)
        self.height = 300/n
        self.position = position
        self.color = (ra.randint(0,255),ra.randint(0,255),ra.randint(0,255))       

class Rods:
    def __init__(self,position):
        self.size = 500
        self.color = 50
        self.position = position
run()
