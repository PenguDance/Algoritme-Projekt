from  p5 import *
import random as ra
import time as T
def setup():
   maxNumber = 10000
   arraySize = 1000
   SArray = randomArray(arraySize, maxNumber)
   print(SArray)
   startTid = T.time()
   print(mergeSort(SArray)) 
   
   print(f"It took {T.time()-startTid} seconds to sort")

def randomArray(n = ra.randint(4000,4000),P = 10):
    SA = []
    for i in range(n):
        SA.append(ra.randint(0,P))
    return(SA)

def mergeSort(SA):
    if len(SA) == 1:
        return SA
    mid = len(SA)//2
    left = SA[:mid]
    right = SA[mid:]
    left = mergeSort(left)
    right = mergeSort(right)
    return merge(left,right)

def merge(l,r):
    SSA = []
    while len(l) > 0 and len(r) > 0:
        if l[0] > r[0]:
            SSA.append(l[0])
            l.remove(l[0])
        else:
            SSA.append(r[0])
            r.remove(r[0])
    while len(l) > 0:
        SSA.append(l[0])
        l.remove(l[0])
    while len(r) > 0:
        SSA.append(r[0])
        r.remove(r[0])
    return SSA
run()