
from numpy  import array, zeros, dot
import matplotlib.pyplot as plt

## FUNCION PARA KEPLER
# def F_Kepler(U):

#     x,y,vx,vy = U[0], U[1], U[2], U[3]

#     mr = (x**2+y**2)**1.5
    
#     return array([vx,vy,-x/mr, -y/mr])

N=10000
U=array([1,0,0,1])

dt=0.001
x=array(zeros(N))
y=array(zeros(N))
x[0]=U[0]
y[0]=U[1]

## EULER
for i in range(0,N):
    F = array([U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5])
    # F = F_Kepler(U)
    U = U + dt*F

    x[i]=U[0]
    y[i]=U[1]


plt.plot(x,y)
plt.show()

## CRANK-NICOLSON

for i in range(0,N):
    F1 = array([U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5])
    F2 = 
    
    U = U + dt*(F1+F2)/2

## RK 4

U=array([1,0,0,1])
x[0]=U[0]
y[0]=U[1]

for i in range(0,N):

    F1 = array([U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5])
    k1=dt*F1
    U2 = U + 1/2*k1
    F2 = array([U2[2], U2[3], -U2[0]/(U2[0]**2+U2[1]**2)**1.5, -U2[1]/(U2[0]**2+U2[1]**2)**1.5])
    k2=dt*F2
    U3 = U + 1/2*k2
    F3 = array([U3[2], U3[3], -U3[0]/(U3[0]**2+U3[1]**2)**1.5, -U3[1]/(U3[0]**2+U3[1]**2)**1.5])
    k3=dt*F3
    U4 = U + k3
    F4 = array([U4[2], U4[3], -U4[0]/(U4[0]**2+U4[1]**2)**1.5, -U4[1]/(U4[0]**2+U4[1]**2)**1.5])
    k4=dt*F4
    
    U = U + 1/6 * (k1+2*k2+2*k3+k4)

    x[i]=U[0]
    y[i]=U[1]

plt.plot(x,y)
plt.show()