from error import Error_Problema_Couchy,Ratio_Convergencia
from Orbitas import Kepler
from Esquemas_temporales import RK4,Euler,Euler_Implicito,Crank_Nicolson
from numpy import array, linspace
import matplotlib.pyplot as plt

N = 5000
t = linspace(0, 10, N) 
U0 = array( [1, 0, 0, 1 ] )
order = 1 
m=5

schemes = [Euler,Euler_Implicito,RK4,Crank_Nicolson]

for scheme in schemes:

    print("Error orbita Kepler con esquema", scheme) 
    Error, U = Error_Problema_Couchy(t,Kepler,scheme,order,U0)

    plt.plot(t, Error[0,:] )
    plt.axis('equal')
    plt.grid()
    plt.show()

    print("orden de convergencia ",scheme) 
    order, log_e, log_n = Ratio_Convergencia( t,Kepler, U0, scheme, m )

    print( "order =", order)
    plt.plot(log_n, log_e )
    plt.axis('equal')
    plt.grid()
    plt.show()