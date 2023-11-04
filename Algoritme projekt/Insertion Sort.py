from  p5 import *
import random as ra
import time as T
def setup():
    SArray = randomArray(2500)
    insertionCopy = [number for number in SArray]
    insertionSort(insertionCopy)

def randomArray(n = ra.randint(4000,4000)):
    SA = []
    for i in range(n):
        SA.append(ra.randint(0,100))
    return(SA)

def insertionSort(SA):
    startTid = T.time()
    for i in range(len(SA)):
        nN = SA[i]
        lm = i-1
        while lm >= 0 and nN < SA[lm]:
            SA[lm+1] = SA[lm]
            lm -= 1
        SA[lm+1] = nN
    print(SA)
    print(f"Det tog {T.time()-startTid} sekunder")

run()