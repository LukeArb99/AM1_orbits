from oscilador import Oscilador
from Esquemas_temporales import Euler,Euler_Implicito,RK4,Crank_Nicolson,leapfrog
from numpy import linspace,array,zeros
from simulacion import Simulacion
from region_estabilidad import Test_Estabilidad

##Resolucion Oscilador lineal
N = 10000
d_t = 0.01                        
t = linspace(0,N*d_t, N+1)
U0=array([1,1])

schemes = [Euler,Euler_Implicito,RK4,Crank_Nicolson,leapfrog]

for scheme in schemes:
    U = array(zeros((2,len(t)-1)))
    U[:,0]=U0
    Simulacion(Oscilador,U,scheme)

##Region de estabilidad de los esquemas
Test_Estabilidad()