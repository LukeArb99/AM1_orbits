from numpy import array

def Kepler(U,t):
    x,y,vx,vy = U[0], U[1], U[2], U[3]

    mr = (x**2+y**2)**1.5
    
    return array([vx,vy,-x/mr, -y/mr])
