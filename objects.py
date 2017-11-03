import random
import numpy as np

class ledger:
    __init__(self,list=[]):
    self.ledger=list

object_ledger=ledger([])

#constructible operations, others postulates can be covered with logic:
construct_ops('make point','connect line','make circle with center and radius')
curve_types(line,ray,segment)

def add_to_ledger(attributes):
    if attributes not in object_ledger:
        object_ledger=object_ledger+[attributes]

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

    def ispointonline(self,point):
        if self.eqnknown==False:
            return 'Unknown'
        elif self.eqnknown==True:
            t=(self.point1.xy[0]-point.xy[0])/(self.point1.xy[0]-self.point2.xy[0]
            for component in range(len(point)):
                if t!=(self.point1.xy[component]-point.xy[component])/(self.point1.xy[component]-self.point2.xy[component]):
                    return False
            return True

    def is_same(self,otherline)
        if self.ispointonline(otherline.point1)==True and self.ispointonline(otherline.point2)==True:
            if otherline.ispointonline(self.point1)==True and otherline.ispointonline(self.point2)==True:
                return True
            else:
                return 'Error in calculation'
         else:
             return False
    def is_parallel(self,otherline):
        if not is_same(self,otherline):
            if self.point1-self.point2==((otherline.point1-otherline.point2)*(1 or -1)):
                if otherline.point1-otherline.point2==((self.point1-self.point2)(*1 or *-1)):
                return True
        else:
            return False

    def intersects(self,otherline): #returns intersection point
        if self.is_same(otherline)==True
            return True #returns true when it intersects at all its points
        elif self.is_parallel(otherline):
            return False
        #find t with extra point from other line, then use to solve for new point

  #  def intersects(self,otherline):
  #  def equation(self):
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

    def is_same(self,othersegment):
        if (self.point1 in othersegment.points) and (self.point2 in othersegment.points):
            return True
        else:
            return False

    def ispointonsegment(self,point):
        if self.eqnknown==False:
            return 'Unknown'
        elif self.eqnknown==True:
            t=(point.xy[0]-self.point2.xy[0])/(self.point1.xy[0]-self.point2.xy[0])
            for comp in range(len(point)):
                u=((point.xy[comp]-self.point1.xy[comp])/(self.point1.xy[comp]-self.point2.xy[comp])>1)
                if u!=t or u>1 or u<-1:
                    return False
                else:
                    return True

    def is_parallel(self,otherline):
        if not is_same(self,otherline):
            if self.point1-self.point2==((otherline.point1-otherline.point2)*(1 or -1)):
                if otherline.point1-otherline.point2==((self.point1-self.point2)(*1 or *-1)):
                return True
        else:
            return False

    def is_shorter(self,othersegment):
        return self.length<othersegment.length

    def is_longer(self,othersegment):
        return self.length>othersegment.length

    def is_equal(self,othersegment):
        return self.length==othersegment.length

       # def is_skew(self,otherline):
       # def intersects(self,otherline):

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
        if (np.dtype(self.center.xy) and np.dtype(self.radius))==('float64' or 'int64'):
            self.eqn=np.array([radius**2,self.cent[0],self.cent[1])
            self.eqnknown=True
        else:
            self.eqn=np.array([str(radius)+'^2=(x-'+str(center[0])+')^2+(y-'+str(center[1])+')^2'])
            self.eqnknown=False

    def is_equal(othercircle):
        return self.radius==othercircle.radius and self.cent==othercircle.cent

    def is_congruent(othercircle):
        return self.radius==othercircle.radius

    def point_is_on(self,point):
        if eqnknown=False
            return 'Unknown'
        else:
            return self.radius**2==(self.cent.xy[0]-point.xy[0])**2+(self.cent.xy[1]-point.xy[1])**2

    def point_is_in(self,point):
        if eqnknown=False
            return 'Unknown'
        else:
            return self.radius**2>(self.cent.xy[0]-point.xy[0])**2+(self.cent.xy[1]-point.xy[1])**2

    def point_is_in(self,point):
        if eqnknown=False
            return 'Unknown'
        else:
            return self.radius**2<(self.cent.xy[0]-point.xy[0])**2+(self.cent.xy[1]-point.xy[1])**2

class route:
    def __init__(self,pointlist,curvelist):
    def is_closed(self):
class figure(closedroute):
class rect_figure(closed_route with lines):
class polygon(n_sides,rect_figure):
class reg_polygon(n_equal sides,polygon):
#equilateral, equiangular, subtending, congruence, equality, in ratio, similar, adjacent
