from math import *
from pga import *
# helper libs for calculating polygons and stuff
# use complex numbers for 2D vector

# center point
def average(points):
    n=len(points)
    avg=complex(0,0)
    for v in points:
        avg+=v
    avg=avg/n
    return avg

# cross product
def exterior(v1,v2):
    # a1*b2-b1*a2
    return (v1.conjugate)*v2).imag

def vectors_to_center(points):
    center=average(points)
    # calculate vectors from center to points
    v_to_c=[]
    i=0
    while(i < len(points)):
        v_to_c.append(points[i]-center)
        i+=1
    return v_to_c

# Uses exterior algebra formula for calculating area,
# by using the center point
def area(points):
    v_to_c=vectors_to_center(points)
    t_area=0
    k=0
    n=len(v_to_c)
    while(k < n):
        t_area+=(exterior(v_to_c[k],v_to_c[(k+1)%n])/2)
        k+=1
    return t_area

def regular_area(Nsides,radius):
    angle = (2*pi)/Nsides
    base = radius
    height = radius*sin(angle)
    return Nsides*(base*height/2)

def is_regular(points):
    # if at least one distance is diferent, return false
    v_to_c=vectors_to_center(points)
    n=len(v_to_c)
    while(k < n):
        if(abs(v_to_c[k]) != abs(v_to_c[(k+1)%n])):
            return False
        k+=1
    # there are N sides, so check with N regular gon
    # assume first vector to center is radius, since
    # check is passed
    sides=len(points)
    radius=abs(v_to_c[0])
    return abs(area(points))==regular_area(sides,radius)

