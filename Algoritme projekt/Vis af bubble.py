from  p5 import *
import random as ra
import time as T
def setup():
   size(800,800)
   SArray = randomArray(10)
   print(SArray)
   bubbleCopy = [number for number in SArray]
   print("Bubblesort:")
   global vis
   global rn 
   rn = 0
   vis = bubblesort(bubbleCopy)

def draw():
    global vis,rn
    background(220)
    if rn == len(vis):
        rn = 0
    for j in range(len(vis[rn])):
        rect(50+j*50,700-vis[rn][j]*50,50,vis[rn][j]*50)

    rn += 1

    startTime = T.time()
    while startTime +1 > T.time():
        0
    
    

        
def randomArray(n = ra.randint(4000,4000)):
    SA = []
    for i in range(n):
        SA.append(ra.randint(1,10))
    return(SA)

def bubblesort(SA):
    print(SA)
    SSA = []
    SSA.append(SA)
    N = 0
    startTid = T.time()
    swapped = True
    while swapped == True:
        swapped  = False
        for i in range(len(SA)-1-N):
            if SA[i] > SA[i+1]:
                SA[i],SA[i+1] = SA[i+1],SA[i]
                swapped = True
            SSA.append((SA))
            print(SSA)
        N += 1
    print(T.time() - startTid)
    print(SSA)
    return SSA

run()