from scipy.optimize import newton


def Euler(U,dt,t,F):
    return U + dt*F(U,t)

def Crank_Nicolson(U,dt,t,F):

    def G(x):
     return x-U-dt/2*(F(U,t)+F(x,t+dt))
    
    return newton(G,U)
    
def RK4(U,dt,t,F):
   
    k1 = F( U, t )
    k2 = F( U +k1*dt/2, t+ dt/2 )
    k3 = F( U +k2*dt/2, t + dt/2 )
    k4 = F( U + k3*dt, t + dt )

    return U+dt/6*(k1+2*k2+2*k3+k4)

def Euler_Implicito(U,dt,t,F):
   
   def H(x):
      return x-U-dt*F(x,t)
   
   return newton(H,U)

def leapfrog(U,dt,t,F):
        # Paso 1
    k1 = F(U, t)
        # Paso 2
    mid_x = U + 0.5 * dt * k1
        # Paso 3
    k2 = F(mid_x, t + 0.5 * dt)

    return U + dt * k2