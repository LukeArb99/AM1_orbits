from Esquemas_temporales import RK4,Embedded_RK,leapfrog
from numpy import array
from simulacion import Simulacion

def f(x,t):
    return array([x[1],-x[0],0])


U0 = array([1,5,9])

Simulacion(f,U0,leapfrog)
