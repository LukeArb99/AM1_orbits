from error import Error_Problema_Couchy,Ratio_Convergencia
from Physics.Orbitas import Kepler
from ODES.Esquemas_temporales import RK4
from numpy import array, linspace
import matplotlib.pyplot as plt

N = 5000
dt = 0.01
t = linspace(0, 10, N) 
U0 = array( [1, 0, 0, 1 ] )
order = 1 

print("Error Kepler orbit ") 
Error, U = Error_Problema_Couchy(N,dt,Kepler,RK4,order,U0)

plt.plot(t, Error[:,0] )
plt.axis('equal')
plt.grid()
plt.show()

N = 2000
t = linspace(0, 10, N) 
U0 = array( [1, 0, 0, 1 ] )
m = 5

print("Order Euler ") 
order, log_e, log_n = Ratio_Convergencia( t,Kepler, U0, RK4, m )

print( "order =", order)
plt.plot(log_n, log_e )
plt.axis('equal')
plt.grid()
plt.show()