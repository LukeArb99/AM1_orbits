from Esquemas_temporales import Euler
from funciones import Problema_de_Cauchy,Kepler
import matplotlib as plt
from numpy import linspace, array

def Simulation(tf, N, U0): 
   
    """ 
    This is a Simulation code to integrate Cauchy problems with some numerical scheme.

    The objective of this Milestone is to create different functions or abstractions 
    by means of functional programming or function composition. 
    Namely, the following modules are created to allow this functional composition:
            1) ODES.Cauhy_problem
            2) ODES.Temporal_schemes
            3) Physics.Orbits
    
    The idea is to create a Cauchy problem abstraction to integrate different physical 
    problems with different temporal schemes.
    
    Different abstractions : 
                     1) dU/dt = F(U, t) 
                     2) Temporal scheme to integrate one step 
                     3) Cauchy problem to perform different steps 
                         
     """


    t = linspace(0, tf, N)
    schemes = [  (Euler, None, None ) ]

    
    for (method, order, eps)  in schemes:

       if order != None:  
          U =  Problema_de_Cauchy( Kepler, t, U0, method, q=order, Tolerance=eps ) 
       else: 
          U =  Problema_de_Cauchy( Kepler, t, U0, method ) 

       plt.plot( U[:,0] , U[:,1], "." )
       plt.show()

if __name__ == "__main__":

  Simulation(100, 100, array( [ 1., 0., 0., 1. ] ) )