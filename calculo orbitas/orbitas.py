from Esquemas_temporales import RK4,Euler
from calculos import Problema_Couchy
from numpy import array, linspace, zeros
import math
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d
import plotly.graph_objects as go

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

def Lorentz(U,t):
    x,y,z =[U[0],U[1],U[2]]
    b=8/3
    r=28
    s=10

    vx=-s*x+s*y
    vy=r*x-x*z-y
    vz=-b*z+x*y

    return array([vx,vy,vz])

def Rossleir(U,t):
    x,y,z = [U[0],U[1],U[2]]
    a=0.398
    b=2
    c=4

    vx=-y-z
    vy=a*y+x
    vz=b+z*(x-c)

    return array([vx,vy,vz])


N = 10000
d_t = 0.01                        
t = linspace(0,N*d_t, N+1)

U = array(zeros((3,len(t)-1)))
U[:,0] = array( [1, 1, 1] )

U = Problema_Couchy(Rossleir,t,U,RK4)


# plt.plot(U[0,:],U[1,:])

# # plt.show()

# fig = plt.figure("proyeccion 3d")
# ax = plt.axes(projection='3d')
# ax.plot3D(U[0,:],U[1,:],U[2,:], 'red')
# plt.show()

# fig = go.Figure(data=go.scatter3d(x=U[0,:],y=U[1,:],z=U[2,:]))
fig = go.Figure(data=[go.Scatter3d(x=U[0,:], y=U[1,:], z=U[2,:])])
fig.update_traces(marker_color='red', selector=dict(type='scatter3d'))
fig.update_traces(marker_size=4, selector=dict(type='scatter3d'))
fig.show()