from error import Error_Problema_Couchy
from Physics.Orbitas import Kepler
from ODES.Esquemas_temporales import RK4
from numpy import array

N=1000
dt=0.01
U0=array([1,0,0,1])


U=Error_Problema_Couchy(N,dt,Kepler,Scheme=RK4,1,U0)