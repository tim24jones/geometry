import random
import numpy as np
#%matplotlib inline (potentially for demonstrations, but not the central logic)
#plotting is an output to illustrate objects that exist with independent logic, usually thought of visually
class geo_session:
    def __init__(self,ledger=[],canvas_sizemin=[-500,-500],canvas_sizemax=[500,500]):#ordered pairs
        self.ledger=ledger
        self.canvas_maxpt=canvas_sizemax
        self.canvas_minpt=canvas_sizemin
        self.canvas_xwidth=self.canvas_maxpt[0]-self.canvas_minpt[0]
        self.canvas_ywidth=self.canvas_maxpt[1]-self.canvas_minpt[1]
        #including just these two as they will be most likely called for visualization
        #could be generalized if important
    def addtoledger(self,geo_object)
        ledger=ledger+(geo_object,)+tuple(geo_object.attributes)
    #def add_shape(self,) or add_construction
#added to list as a tuple of {object:object.attributes} with default attributes=Null
#attributes are things that necessarily connect or are part of the object, such as line objects for an intersection object

class geo_object:
    __init__():

    def constructible_operation(self,construct_fn):
        constructible_operations=(makepoint(),makeline(),make_circle_center_radius())
        #the equality of right angles and infering the crossing of lines less than
        #180 degrees apart can happen with logic rather than extra construction
        #thus this covers all 5 postulates
        if (construct_fn is in constructible_operations):
            return True
        else
            return False

    class space:
        def __init__(self,dimension=2):
            self.dimen=dimension
        def points_in_space(self):
            for points in 
        def add_dimension(self,dims_added):
            self.dimen=self.dimen+dims_added
            #for point in space
                #point=point+[0]
            #add dimension to contained points, initialize with 0 by default
        def points_in_space(self):
            #return list of points in space

    class point()
        def __init__(space_name,coordinates):
            self.space=space_name
            self.coords=coordinates
            self.dimens=len(coordinates)
            self.attributes=(space_name,)+tuple(self.coords)
        def __str__(self):
            glue=','
            return '('+glue.join(str(n) for n in self.coords)+')'

    def make_point(geo_session,space_name,minvalues=[0]*dimension,maxvalues=[1]*dimension):
        #takes number of dimensions, and optional lists of the 
        #minimum and maximum values for each dimension
        #(listing x,y,z... etc. as needed), defaulting to ranges between 0 and 1
        while dimension<(len(minvalues) or len(maxvalues)):
            print('Dimension specified is too small for the number of specified parameters.  Now trying a larger dimension')
            dimension=dimension+1
        if len(minvalues)!=len(maxvalues):
            print('Dimension mismatch: There must be the same number of maximum and minimum values specified.  Adding extra values to compensate.')
            while len(minvalues)<len(maxvalues):
                minvalues=minvalues+[0]
            while len(minvalues)>len(maxvalues):
                maxvalues=maxvalues+[1]
        point_value=[]
        for n in range(dimension):
            pt_domain=random.randrange(minvalue[n],maxvalue[n])
            point_value=point_value+pt_domain
        new_point=point(space_name,point_dimens)
        geo_session.ledger=geo_session.ledger+[('Point',)+tuple(new_point.attributes)]
        #point is added to the ledger as ('Point',space_in_which_point_is_defined,[coordinates])
        return new_point

def connect_lineseg(onepoint,anotherpoint):
    
def ispointonline(apoint,aline):
        directionvect=aline-apoint
        componentlist=[]
        x=(apoint[0]-aline.onepoint[0])/aline.getdirection[0]
        for i in range(apoint.dimension)
            if (x!=(apoint[i]-aline.onepoint[i])/aline.getdirection[i]):
                return False
        return True
        
def ispointonlinesegment(point,lineseg):

class line:
    def __init__(self,onepoint,anotherpoint):
        parallelvect=anotherpoint-onepoint
    def getpoint(self):
        return self.onepoint
    def getotherpoint(self):
        return self.otherpoint
    def getdirection(self):
        return (self.onepoint-self.otherpoint)
    def is_equal(self,otherline):
    def is_parallel(self,otherline):
    def is_skew(self,otherline):
    def intersects(self,otherline):
    def equation(self)

class linesegment:
    def __init__(self,firstpoint,lastpoint):
    def is_equal(self,otherlinesegment):
    def is_shorter(self,otherlinesegment):
    def is_longer(self,otherlinesegment):
    def extend(self,endpoint):
class circle:
    def __init__(onepoint,twopoint,threepoint):
        center
        radius
        diameter
    def is_equal(othercircle):
    def point_is_on(self,point):
    def point_is_in(self,point):
    def point_is_outside(self,point):
class intersection(self,oneline,twoline):
    def angle_1:
    def angle_2:
    def angle_3:
    def angle_4:
    #adjacent angles belong to class straightangle
    #opposite angles equal

class straightangle:
    def __init__(line,point):
class route:
    def __init__(self,pointlist,curvelist):
    def is_closed(self):
class figure(closedroute):
class rect_figure(closed_route with lines):
class polygon(n_sides,rect_figure):
class reg_polygon(n_equal sides,polygon):
#equilateral, equiangular, subtending, congruence, equality, in ratio, similar, adjacent
