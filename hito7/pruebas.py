from numpy import array,zeros, empty

k=5
lamnbda=2

p=int(6*k/lamnbda)

S=[]
V=[]
chi=[]
E=[]
x=array([35,85,5,46,13])
x1=zeros(len(x))
L=[]
for i in range(0,p):
    S.append(2**(i*lamnbda/6))

print(S)

for i in range(0,p):
    chi.append(i)

print(chi)
for i in range(0,p):
    if chi[i] in S:
        V.append(1)
    else:
        V.append(0)
         

print(V)

for i in range(0,p):
    E.append(S[i]*V[i])

print(E)

E1 = list(filter(lambda x: x != 0, E))
print(E1)

alpha = (2**k-1)/(max(x)-min(x))
beta = -alpha*min(x)+1
print(alpha,beta)

for i in range(0,len(x)):
    x1[i] = alpha*x[i]+beta
print(x)
print(x1)

mu=2**(lamnbda/6)-1
D=empty((len(x1),len(E1)))
for i in range(0,len(x1)):
    for j in range (0,len(E1)):
        if abs(x1[i]-E1[j])<=mu:
            D[i,j]=0
        else:
            D[i,j]=x1[i]

print(D)

for i in range(0,len(x1)):
    L.append(min(D[i,:]))

print(L)

tau=2
o=5
f=55*2**((tau+12*o-10)/12)

F=[]
for i in range(0,len(x1)):
    F.append(f*L[i])

print(F)