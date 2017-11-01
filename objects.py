import random
import numpy as np

class ledger:
    __init__(self,list=[]):
    self.ledger=list

object_ledger=ledger([])

def add_to_ledger(attributes):
    if attributes not in object_ledger:
        object_ledger=object_ledger+[attributes]


    #def constructible_operation(self,construct_fn):
    #    constructible_operations=(makepoint(),makeline(),make_circle_center_radius())
        #the equality of right angles and infering the crossing of lines less than
        #180 degrees apart can happen with logic rather than extra construction
        #thus this covers all 5 postulates
     #   if (construct_fn is in constructible_operations):
      #      return True
       # else
        #    return False
class point:
    def __init__(self,coords,name=None):
        self.xy=np.array(coords)
        if name==None:
            self.attributes=np.array(['point',self.xy])
        else:
            self.attributes=np.array(['point '+str(name),self.xy])
        add_to_ledger(self.attributes)
    def __str__(self):
        return self.attributes


class line:
    def __init__(self,point,otherpoint):
        self.point1=point
        self.point2=otherpoint
        self.points=np.vstack(self.point1,self.point2)
        if (np.dtype(self.point1.xy) and np.dtype(self.point2.xy))==('float64' or 'int64'):
            self.equation='r=',self.point1.xy, '+',(self.point2.xy-self.point1.xy),'t'
            self.eqnknown=True
        else:
            self.equation='r='+str(self.point1.xy)+'+('+str(self.point2.xy)+'-'+str(self.point1.xy)+')t'
            self.eqnknown=False
        self.attributes=np.array(['line',self.equation,self.line])
        add_to_ledger(self.attributes)
        
    def __str__(self):
        return np.vstack(self.point1,self.point2)
        def getdirection(self):
            return (self.onepoint-self.otherpoint)
  #  def is_same(self,otherline):
  #  def is_parallel(self,otherline):
  #  def is_skew(self,otherline):
  #  def intersects(self,otherline):
  #  def equation(self):
  #  def ispointonline(self,point):
  #  directionvect=aline-apoint
  #  componentlist=[]
  #  x=(apoint[0]-aline.onepoint[0])/aline.getdirection[0]
  #      for i in range(apoint.dimension)
  #          if (x!=(apoint[i]-aline.onepoint[i])/aline.getdirection[i]):
  #              return False
  #      return True

        
class segment: #line segment
    def __init__(self,point,otherpoint):
        self.point1=point
        self.point2=otherpoint
        if (np.dtype(self.point1.xy) and np.dtype(self.point2.xy))==('float64' or 'int64'):
            self.length=np.linalg.norm(self.point1.xy-self.point2.xy)
            self.lengthknown=True
        else:
            self.length=np.array(['sqrt((x-'+str(self.point2.xy[0])+'-'+str(self.point1.xy[0])+')^2+(y-'+str(self.point2.xy[1])+'='+str(self.point1.xy[1])+')^2)'], dtype=object)
            self.lengthknown=False
        self.points=np.vstack(self.point1,self.point2)
        if (np.dtype(self.point1.xy) and np.dtype(self.point2.xy))==('float64' or 'int64'):
            self.equation='r=',self.point1.xy, '+',(self.point2.xy-self.point1.xy),'t'
            self.eqnknown=True
        else:
            self.equation='r='+str(self.point1.xy)+'+('+str(self.point2.xy)+'-'+str(self.point1.xy)+')t'
            self.eqnknown=False
        self.attributes=np.array(['segment',self.equation,self.line])
        add_to_ledger(self.attributes)
    __str__(self):
        return self.attributes

       # def is_same(self,otherline):
       # def is_parallel(self,otherline):
       # def is_skew(self,otherline):
       # def intersects(self,otherline):
       # def is_equal(self,otherlinesegment):
       # def is_shorter(self,otherlinesegment):
       # def is_longer(self,otherlinesegment):
       # def extend(self,endpoint):
       # def ispointonsegment(self,point):

class ray:
    __init__(self,endpoint,otherpoint):
        self.endpoint=endpoint
        self.arb=otherpoint #arbitrary point
        self.points=np.vstack(self.endpoint,self.arb)
        if (np.dtype(self.endpoint.xy) and np.dtype(self.arb.xy))==('float64' or 'int64'):
            self.equation='r=',self.endpoint.xy, '+',(self.arb.xy-self.endpoint.xy),'t'
        else:
            self.equation='r='+str(point1.xy)+'+('+str(point2.xy)
        self.attributes=np.array(['ray',self.equation,self.line])
        add_to_ledger(self.attributes)
    __str__(self):
        return self.attributes
class intersection:
    __init__(self,line1,line2)
    #self.angle1:define 4 angles (minimum)

class angle:
    def __init__(self,vertex,point1,point2):
        self.intersection
        self.vertex=vertex
        self.p1=point1
        self.p2=point2
    def is_straightangle
    
class circle:
    def __init__(self,center,radius):
        self.cent=center
        self.radius=radius
        if type(self.radius==(int or float):
            self.dia=2*radius
        else:
            self.dia=np.array(['2'+str(radius)],dtype=object)
    def is_equal(othercircle):
    def point_is_on(self,point):
    def point_is_in(self,point):
    def point_is_outside(self,point):
class intersection(self,oneline,twoline):

class route:
    def __init__(self,pointlist,curvelist):
    def is_closed(self):
class figure(closedroute):
class rect_figure(closed_route with lines):
class polygon(n_sides,rect_figure):
class reg_polygon(n_equal sides,polygon):
#equilateral, equiangular, subtending, congruence, equality, in ratio, similar, adjacent
