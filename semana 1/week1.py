
from numpy  import array, zeros, linalg
from scipy.optimize import newton
import matplotlib.pyplot as plt

## FUNCION PARA KEPLER
# def F_Kepler(U):

#     x,y,vx,vy = U[0], U[1], U[2], U[3]

#     mr = (x**2+y**2)**1.5
    
#     return array([vx,vy,-x/mr, -y/mr])

N=1000
U=array([1,0,0,1])

dt=0.01
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

plt.title("EULER")
plt.axis('equal')
plt.plot(x,y)
plt.show()

## CRANK-NICOLSON

U=array([1,0,0,1])
x[0]=U[0]
y[0]=U[1]

for i in range(0,N):

    sigmaF = array([0,0,0,0])
    F1 = array([U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5])
    F2 = array([U[2], U[3], -U[0]/(U[0]**2+U[1]**2)**1.5, -U[1]/(U[0]**2+U[1]**2)**1.5])
    # F2 = array([0.1,0.1,0.1,0.1])
    sigma = 1

    while sigma >= dt*10:
        # F2 = array([1.,1.,1.,1.])
        F2 = F2 + sigmaF
        U1 = U + 0.5*dt*(F1+F2)
        F3 = array([U1[2], U1[3], -U1[0]/(U1[0]**2+U1[1]**2)**1.5, -U1[1]/(U1[0]**2+U1[1]**2)**1.5])
        # print(F3)

        sigmaF = F2-F3
        sigma = linalg.norm(sigmaF)
    
    U = U + dt*(F1+F2)/2

    x[i]=U[0]
    y[i]=U[1]

plt.title("CRANK-NICOLSON")
plt.axis('equal')
plt.plot(x,y)
plt.show()


## definicion de funcion para crank-nicolson
# U = array(zeros[4,N])
# U[:,0]=array([1,0,0,1])
# for n in range(0,N-1):
#     a=U[:,N]
#     U[:,N+1]= newton(G(x),U[:,N])


# def G(x):
#     return x-a-dt/2*(F_Kepler(a)+F_Kepler(x))


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

plt.title("RK4")
plt.axis('equal')
plt.plot(x,y)
plt.show()