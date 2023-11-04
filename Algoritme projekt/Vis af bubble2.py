from  p5 import *
import random as ra
import time as T
def setup():
    global SA,startTime,waitTime,pauseTime,N,n,q
    width = 1000
    height = 1000
    size(width,height)
    background(220)
    SA = randomArray(1)
    N,n,q = 0,0,True
    waitTime = 0
    pauseTime = 1
    startTime = T.time()
def draw():
    global startTime,N,n,q,SA,swapped
    if startTime + waitTime < T.time() and N != len(SA)-1:
        background(220)
        for i in range(len(SA)-N):
            create(i,0,0,0)
        if N != 0:
                for j in range(N):
                    create(len(SA)-j-1,0,255,0)
        if q:
            create(n,0,0,255)
            create(n+1,255,0,0)
            if SA[n] > SA[n+1]:
                SA[n],SA[n+1] = SA[n+1],SA[n]
                swapped = True
            else:
                swapped = False
            q = False
        else:
            if swapped == True:
                create(n,255,0,0)
                create(n+1,0,0,255)
            else:
                create(n,0,0,255)
                create(n+1,255,0,0)
            q = True
            n += 1
        if n == len(SA)-1-N:
            n = 0
            N += 1
       
        startTime = T.time()
    if N == len(SA)-1:
        background(220)
        for j in range(N+1):
                    create(j,0,255,0)
    if startTime + pauseTime < T.time():
        N,n,q = 0,0,True
        SA = randomArray(len(SA)*2)
def create(l,r,g,b):
    fill(r,g,b)
    if r != 0 or g != 0 or b != 0:
        fill(r,g,b)
    else:
        fill(120) 
    rect(l*width/len(SA),height-25,width/len(SA),-SA[l]*1.5)
def randomArray(n):
    SA = []
    for i in range(n):
        SA.append(ra.randint(10.0,500.0))
    return(SA)
run()