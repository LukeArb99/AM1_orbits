from Esquemas_temporales import Euler,Euler_Implicito,Crank_Nicolson,RK4
from funciones import Kepler
from simulacion import Simulacion
from numpy import array                     

U0=array([1,0,0,1])


Simulacion(Kepler,U0,Euler)
Simulacion(Kepler,U0,Euler_Implicito)
Simulacion(Kepler,U0,Crank_Nicolson)
Simulacion(Kepler,U0,RK4)