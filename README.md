# polygon
Program for finding how many regular subpolygons 
are inside a regular one

## Problem
Given a regular polygon with N sides, draw all the 
diagonals and find the intersections.For the union of
this set of vertices, find all the posible regular 
subpolygons that can be made by all the posible 
combinations of vertices.

## Tools
* pga.py : Poor man's Projective Geometric Algebra
  for making lines and finding their intersections
* gons.py : Helper functions for regular N-gons
* main : Main program

The program can output csv files of the obtained
vertices for use on another plotting program,and
can read arguments from standard input:

```> python main.py Nsides radius "csv" "quiet"```

The quiet option disables vertices's printing,
"csv" and "quiet" must be entered as is (strings).

## Other links
* [PGA video](https://youtu.be/0i3ocLhbxJ4?si=fh26FObLpxmlrt2X)
* [Intersection of diagonals sequence](https://oeis.org/A006561)
