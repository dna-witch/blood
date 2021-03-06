from math import cos, sin, pi
#import matplotlib.pyplot as plt


def point_inside_polygon(x,y,poly):
    # determine if a point is inside a given polygon or not
    # Polygon is a list of (x,y) pairs.
    n = len(poly)
    inside =False

    p1x,p1y = poly[0]
    for i in range(n+1):
        p2x,p2y = poly[i % n]
        if y > min(p1y,p2y):
            if y <= max(p1y,p2y):
                if x <= max(p1x,p2x):
                    if p1y != p2y:
                        xinters = (y-p1y)*(p2x-p1x)/(p2y-p1y)+p1x
                    if p1x == p2x or x <= xinters:
                        inside = not inside
        p1x,p1y = p2x,p2y

    return inside


def check(a,b,x,y,l,phi):
    # for rectangle [-a,a]X[-b,b], check if box centered at (x,y) with side length l is inside region generated by
    # rotating the rectangle phi radians clockwise intersected with original rectangle
    rect = [[-a,-a,a,a],[-b,b,b,-b]]  # vertices of rectangle
    rot = [[cos(phi),sin(phi)],[-sin(phi),cos(phi)]]  # rotation matrix
    it1 = [0,1]  # common iterable number 1 (since x and y coord)
    it2 = range(0,4)  # common iterable number 2
    # compute rotated rectangle vertices
    newRect = [[sum([rot[i][k]*rect[k][j] for k in it1]) for j in it2] for i in it1]

    boxCenter = [[x],[y]]  # vector representation of box center
    # compute new box center
    newBoxCenter = [[sum([rot[i][k] * boxCenter[k][0] for k in it1])] for i in it1]
    # generate vertices of new box
    newBox = [[newBoxCenter[k][0] + (-1)**(k*j+j+i)*l/2 for i in it1 for j in it1] for k in it1]

    # rearrange old rectangle and rotated rectangle into lists of [x,y] points
    poly1 = [[rect[j][i] for j in it1] for i in range(-1,4)]
    poly2 = [[newRect[j][i] for j in it1] for i in range(-1,4)]

    test1 = [point_inside_polygon(newBox[0][i],newBox[1][i],poly1) for i in it2]
    test2 = [point_inside_polygon(newBox[0][i],newBox[1][i],poly2) for i in it2]

    # visualization
    #plt.plot([i for i in rect[0]], [i for i in rect[1]])
    #plt.plot([i for i in newRect[0]], [i for i in newRect[1]])
    #plt.plot([i for i in newBox[0]], [i for i in newBox[1]])
    #plt.show()
    return all(test1 + test2)


def angles(a,b,x,y,l):
    # returns list of acceptable angles for original rectangle [-a,a]X[-b,b] and box centered at (x,y) w/ side length
    n = 100  # number of angles to test
    degFlag = 0  # set equal to 1 to get degrees

    angs = [2*pi*i/100 for i in range(1,100)]  # generate list of angles from 0 to 2pi
    test = [check(a,b,x,y,l,i) for i in angs]  # check if box is in appropriate region for each angle
    newAngs = [test[i]*angs[i] for i in range(0,len(angs))]  # zero out failed angles
    for i in range(0,newAngs.count(0)):  # remove zeros
        newAngs.remove(0)
    if degFlag == 1:  # convert to degrees if degFlag == 1
        newAngs = [i*360/2/pi for i in newAngs]

    return newAngs
