from math import *

# Poor man's 2D Projective Geometric Algebra

def complex_exterior(v1,v2):
    # a1*b2-b1*a2
    return (v1.conjugate()*v2).imag

# complex as "vector" v1,v2
class line():
    # l = ax+by+c -> (a,b,c)
    def __init__(self,v1,v2):
        dv=v2-v1
        dx=dv.real
        dy=dv.imag
        self.a=0
        self.b=0
        self.c=0
        # vertical line, x intercept
        if(dx==0):
            self.b=0
            self.a=-1
            self.c=v.real
        # horizontal line, y intercept
        elif(dy==0):
            self.a=0
            self.b=-1
            self.c=v1.imag
        else:
            m=dv.imag/dv.real #slope
            y0=v1.imag-m*v1.real
            self.c=-1*y0
            self.a=-1*m
            self.b=1

    def __getitem__(self,i):
        try:
            if(i==1):
                return self.a
            if(i==2):
                return self.b
            if(i==0):
                return self.c
            else:
                raise ValueError
        except ValueError:
            print("Line index out of bounds")
            #quit()

    def exterior_ij(self,l1,l2,i,j):
        if(i==j):
            return 0
        else:
            v1=complex(l1[i],l1[j])
            v2=complex(l2[i],l2[j])
            return complex_exterior(v1,v2)
    # this was from PGA video on YT, dont ask lol
    def exterior(self,l0,l1):
        # we dont do the i==j cases, for optimization
        ext=[]
        ext.append(self.exterior_ij(l0,l1,1,2))
        ext.append(self.exterior_ij(l0,l1,2,0))
        ext.append(self.exterior_ij(l0,l1,0,1))
        return ext

    # this is the exterior product divided by Ae1^e2!!
    # returns [x,y]
    def intersect(self,l0,l1):
        ext=self.exterior(l0,l1)
        e12=ext[0]
        if(e12==0):
            # paralel lines
            return [math.inf, math.inf]
        return [ext[1]/e12,ext[2]/e12]

    def do_intersect(self,l0,l1):
        if(intersect(l0,l1)[0]==math.inf):
            return False
        else:
            return True
# return "line" repr. from first to end
