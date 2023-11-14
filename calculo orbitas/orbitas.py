from Esquemas_temporales import RK4,Euler
from calculos import Problema_Couchy
from numpy import array, linspace, zeros
import math
import matplotlib.pyplot as plt

def Duffin(U0,t):
    x, y = [U0[0], U0[1]]
    A, B = [0.25,1]

    vx=y
    vy=-x**3-A*y+B*math.cos(t)

    return array( [vx, vy] )
def Von_Der_Por(U0,t):
    x,y =[U0[0], U0[1]]
    nu,w =[0.2,5]

    vx=y
    vy=-nu*(x**2-1)*y-w*x

    return array([vx,vy])
def Lord_Rayleigh(U,t):
    x,y = [U[0], U[1]]
    f0 = 2

    vx=y
    vy=x-x**3-y+f0*math.cos(t)

    return array([vx,vy])


N = 10000
d_t = 0.01                        
t = linspace(0,N*d_t, N+1)

U = array(zeros((2,len(t)-1)))
U[:,0] = array( [1, 1] )

U = Problema_Couchy(Von_Der_Por,t,U,RK4)

plt.plot(U[0,:],U[1,:])

plt.show()