from numpy import zeros, array, float64



def Problema_de_Cauchy(F,t,U0,Metodo):

    N=len(t)-1
    Nv=len(U0)
    U = zeros( (Nv, N+1), dtype=float64 ) 


    U[:,0]=U0

    for n in range(N):
        U[:,n+1] = Metodo(U[:,n],t[n+1]-t[n],t[n],F)

    return U

def Kepler(U,t):
    x,y,vx,vy = U[0], U[1], U[2], U[3]

    mr = (x**2+y**2)**1.5
    
    return array([vx,vy,-x/mr, -y/mr])

def funcion(U,t):
    x=U[0]
    y=U[1]
    return array([3*x-2*y,2*x-2*y])