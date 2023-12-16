from numpy import zeros, float64



def Problema_de_Cauchy(F,t,U0,Metodo):

    N=len(t)-1
    Nv=len(U0)
    U = zeros( (Nv, N+1), dtype=float64 ) 


    U[:,0]=U0

    for n in range(N):
        U[:,n+1] = Metodo(U[:,n],t[n+1]-t[n],t[n],F)

    return U