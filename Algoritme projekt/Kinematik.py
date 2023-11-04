from  p5 import *
def setup():
    global L1,L2,a,b
    L1 = 480
    L2 = 380
    a = 50*PI/180
    b = -90*PI/180

def draw():
    global L1,L2,a,b
    line(100,800,L1*cos(a),-L1*sin(a))
    line(100+L1*cos(a),800-L1*sin(a),L2*cos(a+b),L2*sin(a+b))

run()