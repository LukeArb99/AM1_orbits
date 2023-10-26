from funciones import Problema_de_Cauchy, funcion
from Esquemas_temporales import RK4, Euler
from numpy import array, linspace, zeros, arange
import matplotlib.pyplot as plt

N=10
U0 = array(zeros(2))  #tiene q ser vector!!!!!!!
# U0[:,0]=array([0,0])
dt = 0.01
t =arange(N)

# def integrador(U, funcion, esquema):
#     for i in range (0, N-1):
#         U[:,i+1]=esquema(funcion,i)

#     return U

# U=integrador(U0,funcion,Euler(U0,dt,t,funcion))
U = Problema_de_Cauchy(funcion,t,U0,RK4)
print(U)

plt.plot(U[0,:],U[1,:])
plt.show()
plt.axis('equal')

