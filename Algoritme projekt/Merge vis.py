from  p5 import *
import random as ra
def setup():
   sArray = randomArray()
   print(sArray)
   print(mergeSort(sArray)) 

def randomArray(n = ra.randint(5,9),P = 10):
    SA = []
    for i in range(n):
        SA.append(ra.randint(0,P))
    return(SA)

def mergeSort(SA):
    if len(SA) == 1:
        return SA
    mid = len(SA)//2
    left = mergeSort(SA[mid:])
    right = mergeSort(SA[:mid])
    return merge(left,right)

def merge(left,right):
    SSA = []
    while len(left) > 0 and len(right) > 0:
        if left[0] > right[0]:
            SSA.append(right[0])
            right.remove(right[0])
        else:
            SSA.append(left[0])
            left.remove(left[0])
    while len(left) > 0:
        SSA.append(left[0])
        left.remove(left[0])    
    while len(right) > 0:
        SSA.append(right[0])
        right.remove(right[0])  
    return SSA
run()