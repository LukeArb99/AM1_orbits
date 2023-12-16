

def Problema_Couchy(F,t,U,Metodo):
    N=len(t)-1

    for n in range(0,N-1):
        U[:,n+1] = Metodo(U[:,n],t[n+1]-t[n],t[n],F)

    return U 
