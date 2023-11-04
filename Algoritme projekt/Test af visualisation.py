from  p5 import *
import random as ra
import time as T
from random import shuffle
def setup():
    size(800,800)
    array = [1,2,3,4,5]
    draw(array)
    
def draw():
    if sorted(array) != False:
        array = [1,2,3,4,5]
        ra.shuffle(array)
        print(array)
        N = 0
        Q = 0
    if  sorted(array) == False:
        print("Sorterer")
        bubble(array,N,Q)
        N +=1
        if N+Q+1 == len(array):
            N = 0
            Q += 1
        
        background(220)
        for j in range(len(array)):
            rect(100+105*j,500-array[j]*50,100,array[j]*50)
        waitTime = T.time()
        while waitTime +1 > T.time():
            0

def bubble(SA,N,Q):
    
    print(N,Q,len(SA))
    if SA[N] > SA[N+1]:
        SA[N],SA[N+1] = SA[N+1],SA[N]
def sorted(SA):
    sorted = True
    for i in range(len(SA)-1):
        if SA[i] > SA[i+1]:
            sorted = False
    return sorted
run()
