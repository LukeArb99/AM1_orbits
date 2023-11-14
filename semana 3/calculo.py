from Richardson import extrapolacion_Richarson_n, g
from numpy import zeros,abs

def error(A):
    m=4
    E =zeros([m,m-1])
    for i in range(0,m):
        for j in range(0,i):
            if A[i,j+1] ==0:
                E[i,j]=0
            else:
                E[i,j]=abs((A[i,j+1]-A[i,j])/A[i,j+1])*100
    return E
                


A = extrapolacion_Richarson_n(g,0.5,1)
print(A)
E=error(A)
print(E)

