import numpy as np

def hex(x,y):
    return (x,y)
def hex_distance(a, b):
    return max(abs(a.x - b.x), abs(a.y - b.y))

def hex_lerp(a, b, t):
    x = round(a.x+(b.x-a.x)*t)
    y= round(a.y+(b.y-a.y)*t)
    return hex(x,y)

def hex_linedraw(a, b):
    N = hex_distance(a, b)
    results = []
    for i in range(1,N):
        results.append(hex_lerp(a, b, 1.0/N * i))
    return results


class point(object):
    def __init__(self,x,y):
        self.x = x
        self.y = y


diretion_x = np.array([-1,-1,0,1,1,0],dtype=int)
diretion_y = np.array([-1,0,1,1,0,-1],dtype=int)
def hex_neighbor(a):
    neighbors = []
    for i in range(0,6):
        neighbors.append((a.x+diretion_x[i],a.y+diretion_y[i]))
    return neighbors