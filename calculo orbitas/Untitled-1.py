
from numpy import array, zeros, linspace, arange
import matplotlib.pyplot as plt
from scipy.optimize import fsolve, newton
import math
## HITO 2


def ODE(U, t): # df/dx = x
    x, y = [U[0], U[1]]

    vx=y
    vy=-x**3-y+math.cos(t)

    return array( [vx, vy] )

def Von_Der_Por(U,t):
    x,y =[U[0], U[1]]
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


def Euler(F,U,t0, tf):
    dt = tf-t0
    return U + dt * F(U,t0)
    
# def Crank_Nicolson(F,i):
    
#     def g(x):
#         return x - a -dt/2 * (F(a) + F(x))
#     a = U[:,i]
    
#     return newton(g, U[:,i])

def RK4(F,U,t0, tf ):
    dt = tf-t0
    k1 = F( U, t0 )
    k2 = F( U +k1*dt/2, t0 + dt/2 )
    k3 = F( U +k2*dt/2, t0 + dt/2 )
    k4 = F( U + k3*dt, t0 + dt )
     
    k = 1/6 * (k1 + 2*k2 + 2*k3 + k4)
    
    return U + dt * k

# def Inverse_Euler(F,i):
#     def g(x):
#         return x - a - dt * F(x,t) 
#     a = U[:,i]
    
#     return newton(g, U[:,i])

def Integrate_ODE(U, F, t, scheme):

    for i in range(0, N-1):
        U[:,i+1] = scheme(F,U[:,i],t[i],t[i+1])
        
    return U

N = 10000
d_t = 0.01                        
t = linspace(0,N*d_t, N+1)

#Keplerian Orbit initial conditions
U0 = array(zeros((2,len(t)-1)))
U0[:,0] = array( [1, 1] )
#U_0 = array( [1.1, 3] )

#Cauchy df/dx = x initial conditions
#U = array(zeros((1,N)))
#U[:,0] = 1.1

U1 = Integrate_ODE(U0,Von_Der_Por, t, RK4)

f1=plt.figure()
plt.plot(U1[0,:],U1[1,:])

# f2=plt.figure()
# plt.plot(U1[0,:])

plt.show()