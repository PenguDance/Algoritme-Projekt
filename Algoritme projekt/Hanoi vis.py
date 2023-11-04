from  p5 import *
import random as ra
import time as T
def setup():
    global rods,N,n,drawings,start,using,end,startTime,waitTime,pauseTime,height,width
    width = 2000
    height = 1000
    size(width,height)
    background(220)
    rectMode('CENTER')
    n = 10
    start = [0]*n
    using = [0]*n
    end = [0]*n
    rods = [0]*3
    drawings = []
    N = 0
    for i in range(n):
        start[i] = Discs(n-i)
    Tstart = []
    
    for i in start:
        Tstart.append(i)
    drawings.append([Tstart,[0]*n,[0]*n])
    hanoi(n,start,end,using)
    for i in range(3):
       rods[i] = Rods(i+1)
    waitTime = 0.1
    pauseTime = 3
    startTime = T.time()
def draw():
    global rods,N,n,drawings,startTime,waitTime,pauseTime,height,width
    if startTime + waitTime < T.time():
        background(220)
        for i in rods:
            fill(i.color)
            rect(i.position*(width/4),height-i.size/2,25,i.size)
        for i in range(len(drawings[N])):
            for j in range(len(drawings[N][i])):
                if drawings[N][i][j] == 0:
                    break
                fill(drawings[N][i][j].color[0],drawings[N][i][j].color[1],drawings[N][i][j].color[2])
                rect((i+1)*(width/4),height-(j+0.5)*drawings[N][i][j].height,drawings[N][i][j].width,drawings[N][i][j].height)
        N += 1 
        if N == len(drawings):
            N = 0
            startTime = T.time() + pauseTime
        else:
            startTime = T.time()

def hanoi(n,s,e,u):
    global drawings,start,using,end
    if n == 1:
        e[findN(e,1)] = s[findN(s)]
        s[findN(s)] = 0
        TStart = []
        TUsing = []
        TEnd = []
        for i in start:
            TStart.append(i)
        for i in using:
            TUsing.append(i)
        for i in end:
            TEnd.append(i)
        drawings.append([TStart,TUsing,TEnd])
        return
    hanoi(n-1,s,u,e)
    e[findN(e,1)] = s[findN(s)]
    s[findN(s)] = 0
    TStart = []
    TUsing = []
    TEnd = []
    for i in start:
        TStart.append(i)
    for i in using:
        TUsing.append(i)
    for i in end:
        TEnd.append(i)
    drawings.append([TStart,TUsing,TEnd])
    hanoi(n-1,u,e,s)

def findN(list,k = 0):
    for i in range(len(list)):
        if list[len(list)-i-1] != 0:
            x = len(list)-i-1+k
            return x
    return 0
        



class Discs:
    def __init__(self,width):
        self.width = 50*(width**0.9)
        self.height = height/n
        self.color = (0,255/width**0.3,200/width**0.5)  

class Rods:
    def __init__(self,position):
        self.size = height-50
        self.color = 50
        self.position = position
run()