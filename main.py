from math import *
import gons
import pga
import sys
import itertools

def diagonals(points):
	n=len(points)
	diags=[]
	#k+2 modulo n, n-2 points
	for i in range(0,n-2):
		for k in range(2,n-3+2):
			v1=points[i]
			v2=points[(i+k)%n]
			l=pga.line(v1,v2)
			diags.append(l)
	return diags

def find_intersections(diags,poly,radius):
	i=0
	j=0
	n=len(diags)
	intersect=diags[0].intersect
	points=[]
	p=0
	do_intersect=diags[0].do_intersect
	for i in range(0,n):
		for j in range(i,n):
			if(i==j):
				continue #FIXME: FLOAT COMPARISONS!
			if(do_intersect(diags[i],diags[j])):
				p=intersect(diags[i],diags[j])
				if(gons.is_insideRadius(p,poly,radius) and (not gons.is_in(p,points))):
					points.append(p)
	return points

if(len(sys.argv)==1):
	sides=int(input("Nº of sides: "))
	radius=float(input("Radius: "))
else:
	sides=int(sys.argv[1])
	radius=float(sys.argv[2])
def void(x,y=0):
	return

def total_combinations(union):
	count=0
	for r in range(3,len(union)+1):
		for subset in itertools.combinations(union,r):
			count+=1
	return count

#make csvs
make_csv=void
if("csv" in sys.argv):
	make_csv=gons.to_csv
verts=gons.print_v
#print vertices
if("quiet" in sys.argv):
	verts=void
poly=gons.gen_polyR(sides,radius)
verts(poly)
make_csv(poly,f"polygon{sides}.csv")
p=find_intersections(diagonals(poly),poly,radius)
print("## intersections:")
verts(p)
print(f"## Total number: {len(p)}")
make_csv(p,f"intersections{sides}.csv")
print("Testing all subpolys...")
union=p+poly
count=0
comb=total_combinations(union)
print(f"Total number of combinations:{comb}")
for r in range(3,len(union)+1):
	print(f"r={r}")
	for subset in itertools.combinations(union,r):
		if(gons.is_regular(subset)):
			print(f" *** Found regular {count+1}")
			verts(subset)
			count+=1
print(f"Total count: {count}")
