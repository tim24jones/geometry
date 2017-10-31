import random
import numpy as np

class geo_object:
    __init__(self,geo_session):

    def constructible_operation(self,construct_fn):
        constructible_operations=(makepoint(),makeline(),make_circle_center_radius())
        #the equality of right angles and infering the crossing of lines less than
        #180 degrees apart can happen with logic rather than extra construction
        #thus this covers all 5 postulates
        if (construct_fn is in constructible_operations):
            return True
        else
            return False

    class geopoint:
        def __init__(self,coordinates,geo_session):
            self.coords=coordinates
            self.dimens=np.array(coordinates).ravel.shape[1]
            self.attributes=np.array('point',self.dimens,self.coords) #attributes not tuples so that printable variables can be assigned and then changed to numbers
            if self.attributes not in geo_session.ledger:
                geo_session.ledger=geo_session.ledger+[self.attributes]
        def __str__(self):
            return np.array(coordinates).ravel

    class geoline:
        def __init__(self,point,otherpoint,geo_session):
            self.point1=point
            self.point2=otherpoint
            self.pointlist=np.array([self.point1],[self.point2])
            self.dimens=np.array(self.point1.dimens,self.point2.dimens).max
            self.attributes=np.array(['line',self.dimens,self.pointlist])
            #self.equation to be done
            if self.attributes not in geo_session.ledger:
                geo_session.ledger=geo_session.ledger+[self.attributes]
        def __str__(self):
            return np.vstack(self.point1,self.point2)
            def getdirection(self):
                return (self.onepoint-self.otherpoint)
        def is_same(self,otherline):
        def is_parallel(self,otherline):
        def is_skew(self,otherline):
        def intersects(self,otherline):
        def equation(self):
        def ispointonline(self,point):
        directionvect=aline-apoint
        componentlist=[]
        x=(apoint[0]-aline.onepoint[0])/aline.getdirection[0]
        for i in range(apoint.dimension)
            if (x!=(apoint[i]-aline.onepoint[i])/aline.getdirection[i]):
                return False
        return True

        
    class geolseg:#line segment
        def __init__(self,point,otherpoint,geo_session):
            self.point1=point
            self.point2=otherpoint
            self.pointlist=np.array([self.point1],[self.point2])
            self.dimens=np.array(self.point1.dimens,self.point2.dimens).max
            #self.equation to be done
            self.attributes=np.array(['lseg',self.dimens,self.pointlist])
            if self.attributes not in geo_session.ledger:
                geo_session.ledger=geo_session.ledger+[self.attributes]
        def __str__(self):
            return np.vstack(self.point1,self.point2)
        def is_same(self,otherline):
        def is_parallel(self,otherline):
        def is_skew(self,otherline):
        def intersects(self,otherline):
        def equation(self)
        def is_equal(self,otherlinesegment):
        def is_shorter(self,otherlinesegment):
        def is_longer(self,otherlinesegment):
        def extend(self,endpoint):
        def ispointonsegment(self,point):


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
