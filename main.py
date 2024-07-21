from math import *
import gons
import pga

def diagonals(points):
	n=len(points)
	diags=[]
	#k+2 modulo n, n-3 points
	for i in range(0,n):
		for k in range(2,n-3+2):
			v1=points[i]
			v2=points[(i+k)%n]
			l=pga.line(v1,v2)
			diags.append(l)
	return diags

def find_intersections(diags):
	i=0
	j=0
	n=len(diags)
	intersect=diags[0].intersect
	points=[]
	do_intersect=diags[0].do_intersect
	for i in range(0,n):
		for j in range(0,n):
			if(i==j):
				continue
			if(do_intersect(diags[i],diags[j])):
				points.append(intersect(diags[i],diags[j]))
	return points

sides=int(input("Nº of sides: "))
radius=float(input("Radius: "))
poly=gons.gen_polyR(sides,radius)
gons.print_v(poly)
p=find_intersections(diagonals(poly))
print("# intersections:")
gons.print_v(p)
