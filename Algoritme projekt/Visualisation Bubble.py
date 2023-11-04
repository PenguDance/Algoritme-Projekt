from  p5 import *
import random as ra
import time as T
def setup():
   size(1200,600)
   tegn = False
   
   
def draw(SA = ra.randint(1,10),tegn = False):
    print(SA,tegn)
    if tegn == True:
        print("Tegner")
        waitTime = T.time()
        while waitTime + 1 > T.time():
            0
        background(220)
        for j in range(len(SA)):
            rect(100+j*105,300-(SA[j]*10),100,SA[j]*10)
    else:
        print("Sorterer")
        background(220)
        SArray = randomArray(7)
        print(SArray)
        bubbleCopy = [number for number in SArray]
        print("Bubblesort:")
        bubblesort(bubbleCopy)
        waitTime = T.time()
    while waitTime + 1 > T.time():
        0

def randomArray(n = ra.randint(4000,4000)):
    SA = []
    for i in range(n):
        SA.append(ra.randint(1,10))
    return(SA)

def bubblesort(SA):
    N = 0
    startTid = T.time()
    swapped = True
    while swapped == True:
        swapped  = False
        for i in range(len(SA)-1-N):
            if SA[i] > SA[i+1]:
                SA[i],SA[i+1] = SA[i+1],SA[i]
                swapped = True
        draw(SA,tegn = True)        
                 
            
       
    print(T.time() - startTid)
def tegn(SA):
    print("Tegner")
    background(220)
    
    rect(ra.randint(0,400),ra.randint(0,400),100,100)
    #for j in range(len(SA)):
       # rect(100+j*105,300-(SA[j]*10),100,SA[j]*10)
run()