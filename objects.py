import random
#%matplotlib inline (if this turns into a jupyter notebook)
#plotting is an output to illustrate objects that exist logically independently
def make_rand_point(dimension,minvalues=[0]*dimension,maxvalues=[1]*dimension):
#takes number of dimensions, and optional lists of the minimum and maximum values for each dimension
#(listing x,y,z... etc. as needed), defaulting to ranges between 0 and 1
    if dimension<(len(minvalues) or len(maxvalues)):
        print('Dimension specified is too small for the number of specified parameters.  A larger dimension will be used')
    if len(minvalues)!=len(maxvalues):
        print('Dimension mismatch: There must be the same number of maximum and minumum values specified.')
        try:
            while len(minvalues)<len(maxvalues):
                minvalues=minvalues+[0]

            while len(minvalues)>len(maxvalues):
                maxvalues=maxvalues+[1]
    point_dimens=[]
    for n in range(dimension):
        pt_domain=random.randrange(minvalue[n],maxvalue[n])
        point_dimens=point_dimens+pt_domain
    return point(point_dimens)
def connect_lineseg(onepoint,anotherpoint)
    
def ispointonline(point,line)
    
def ispointonlinesegment(point,lineseg)
    
class space:
    def __init__(self,dimension):
        
    def add_dimension(self,dims_added):
        #add dimension to contained points, initialize with 0 by default
class point:
    def __init__(self,coordinates):
class line:
    def __init__(self,onepoint,anotherpoint):
    def is_equal(self,otherline):
    def is_parallel(self,otherline):
    def is_skew(self,otherline):
    def intersects(self,otherline):
class linesegment
    def __init__(self,firstpoint,lastpoint):
    def is_equal(self,otherlinesegment):
    def is_shorter(self,otherlinesegment):
    def is_longer(self,otherlinesegment):
    def extend(self,endpoint)
class circle
    def __init__(onepoint,twopoint,threepoint):
        center
        radius
        diameter
    def is_equal(othercircle):
    def point_is_on(self,point):
    def point_is_in(self,point):
    def point_is_outside(self,point):
class intersection(self,oneline,twoline):
    def angle_1
    def angle_2
    def angle_3
    def angle_4
    #adjacent angles belong to class straightangle
    #opposite angles equal

class straightangle:
    def __init__(line,point):
class route:
    def __init__(self,pointlist,curvelist):
    def is_closed(self
class figure(closedroute)
class rect_figure(closed_route with lines)
class polygon(n_sides,rect_figure)
class reg_polygon(n_equal sides,polygon)

equilateral, equiangular, subtending, congruence, equality, in ratio, similar, adjacent
