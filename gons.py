from math import *
from pga import *
# helper libs for calculating polygons and stuff
# use complex numbers for 2D vector
# also generator for polys

def print_v(points,digits=3):
	for v in points:
		s=str(round(v.real,digits))
		s+=(","+str(round(v.imag,digits))+"j")
		print(s)

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
    return ((v1.conjugate())*v2).imag

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
    epsilon=2**-8
    # if at least one distance is diferent, return false
    v_to_c=vectors_to_center(points)
    n=len(v_to_c)
    k=0
    #for v in v_to_c:
    #    print(abs(v))
    while(k < n):
        if abs(abs(v_to_c[k]) - abs(v_to_c[(k+1)%n]))>epsilon:
            return False
        k+=1
    # there are N sides, so check with N regular gon
    # assume first vector to center is radius, since
    # check is passed
    sides=len(points)
    radius=abs(v_to_c[0])
    #print(area(points))
    #print(regular_area(sides,radius))
    return abs(abs(area(points))-abs(regular_area(sides,radius)))<=epsilon

def gen_polyR(Nsides,radius):
    points=[]
    da=2*pi/Nsides
    a=0
    for i in range(1,Nsides+1):
        points.append(complex(cos(a+da*i),sin(a+da*i))*radius)
    return points

