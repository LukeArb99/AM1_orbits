from numpy import array,zeros,linspace
from ODES.Probema_Cauchy import Problema_de_Cauchy


def Error_Problema_Couchy(N,dt,F,Scheme,orden,U0):
    Nv = len(U0)

    t1=linspace(0,N*dt,N+1)
    t2=linspace(0,N*dt/2,N+1)

    U1=zeros((N,Nv))
    U2=zeros((N,Nv))
    Error = zeros((N,Nv))

    U1[:,0]=U0[:,0]
    U2[:,0]=U0[:,0]

    U1 = Problema_de_Cauchy(F,t1,U1,Scheme)
    U2 = Problema_de_Cauchy(F,t2,U2,Scheme)

    for i in range(N):
        Error[i,:]=(U2[2*i,:]-U1[i,:])/(1-1/2**orden)
    
    return Error