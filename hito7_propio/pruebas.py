from numpy import array,zeros, empty, asarray
from math import log,log10

k=5
lamnbda=2

p=int(6*k/lamnbda)

S=[]
V=[]
chi=[]
E=[]
# x=array([35,85,5,46,13])
# x1=zeros(len(x))
# L=[]
# for i in range(0,p):
#     S.append(2**(i*lamnbda/6))

# print(S)

# for i in range(0,p):
#     chi.append(i)

# print(chi)
# for i in range(0,p):
#     if chi[i] in S:
#         V.append(1)
#     else:
#         V.append(0)
         

# print(V)

# for i in range(0,p):
#     E.append(S[i]*V[i])

# print(E)

# E1 = list(filter(lambda x: x != 0, E))
# print(E1)

# alpha = (2**k-1)/(max(x)-min(x))
# beta = -alpha*min(x)+1
# print(alpha,beta)

# for i in range(0,len(x)):
#     x1[i] = alpha*x[i]+beta
# print(x)
# print(x1)

# mu=2**(lamnbda/6)-1
# D=empty((len(x1),len(E1)))
# for i in range(0,len(x1)):
#     for j in range (0,len(E1)):
#         if abs(x1[i]-E1[j])<=mu:
#             D[i,j]=0
#         else:
#             D[i,j]=x1[i]

# print(D)

# for i in range(0,len(x1)):
#     L.append(min(D[i,:]))

# print(L)

# tau=2
# o=5
# f=55*2**((tau+12*o-10)/12)

# F=[]
# for i in range(0,len(x1)):
#     F.append(f*L[i])

# print(F)
# # print(log(abs(F[1])/440))

# theta=[]
# for i in range(0,len(F)):
#     if abs(F[i]) / 440 <= 0:
#         theta.append(69)
#     else:
#         theta.append(69 + 12 / log10(2) * log10(abs(F[i]) / 440))

# print(theta)

R=[0,1,2,3,4,5,6]
y=array([10000,154896,47953,47812,45786])

alpha = (max(R)-min(R))/(max(y)-min(y))
beta = -alpha*min(y)+min(R)
y1 = zeros(len(y))
y2 = []
for i in range(0,len(y)):
    y1[i] = alpha*y[i]+beta
print(y1)
# y1 = round(y1)
# print(round(y1[1]))
for i in range(0,len(y1)):
    y2.append(round(y1[i]))

# # print(y2)

# # Y=[]
# # tp=70
# # for i in range(0,len(y2)):
# #     Y.append(60/tp*2**y2[i]/2**4)

# # print(Y)
# Z=[]
# for i in range(0,len(R)):
#     Z.append(R[i]/max(R))
# print(Z)
# print(type(Z))
# print(len(Z))

# z=asarray(Z)
# print(z)
# print(type(z))
# print(len(z))