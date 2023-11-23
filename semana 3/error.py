from numpy import array,zeros,linspace,log10,ones,vstack
from numpy.linalg import norm,lstsq
from ODES.Probema_Cauchy import Problema_de_Cauchy


def Error_Problema_Couchy(N,dt,F,Scheme,orden,U0):
    Nv = len(U0)

    t1=linspace(0,N*dt,N+1)
    t2=linspace(0,N*dt/2,N+1)

    Error = zeros((N,Nv))

    U1 = Problema_de_Cauchy(F,t1,U0,Scheme)
    U2 = Problema_de_Cauchy(F,t2,U0,Scheme)

    for i in range(N):
        Error[i,:]=(U2[2*i,:]-U1[i,:])/(1-1/2**orden)
    
    return Error


def Ratio_Convergencia(t,F,U0,Scheme,m):
    log_E=zeros(m)
    log_N=zeros(m)
    N=len(t)-1
    t1=t
    U1=Problema_de_Cauchy(F,t1,U0,Scheme)

    for i in range(m):
        N=2*N
        t2=array(zeros(N+1))
        t2[0:N+1:2]=t1, t2[1:N:2]=(t1[1:int(N/2)+1]+t1[0:int(N/2)])/2
        U2=Problema_de_Cauchy(F,t2,U0,Scheme)

        error=norm(U2[N,:]-U1[int(N/2),:])
        log_E[i]=log10(error); log_N[i]=log10(N)
        t1=t2; U1=U2

    for j in range(m):
        if abs(log_E[j])>12 : break

    j=min(j,m-1)
    x=log_N[0:j+1]; y=log_E[0:j+1]
    A=vstack([x,ones(len(x))]).T
    m,c =lstsq(A,y,rcond=None)[0]
    order=abs(m)
    log_E =log_E-log10(1-1/2**order)

    return order, log_E, log_N