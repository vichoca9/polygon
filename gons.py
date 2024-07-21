from math import *
from pga import *
import csv
# helper libs for calculating polygons and stuff
# use complex numbers for 2D vector
# also generator for polys

def print_v(points,digits=5):
	print("# Points of polygon:")
	for v in points:
		s=" * "+str(round(v.real,digits))
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

def center_equal(v_to_c,epsilon):
    n=len(v_to_c)
    for k in range(0,len(v_to_c)):
        if abs(abs(v_to_c[k]) - abs(v_to_c[(k+1)%n]))>epsilon:
            return False
    return True

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
    v_to_c=vectors_to_center(points)
    # if at least one distance is diferent, return false
    if(not center_equal(v_to_c,epsilon)):
        return False
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

def is_insideRadius(point,poly,radius):
	center=average(poly)
	epsilon=2**-8
	return (radius-abs(point-center))>=epsilon

def is_in(point,list):
	epsilon=2**-10
	for v in list:
		if(abs(point-v)<=epsilon):
			return True
	return False

def to_csv(points,filename):
	file=open(filename,"w")
	csv.writer(file).writerow(['x','y'])
	for v in points:
		csv.writer(file).writerow([v.real,v.imag])
