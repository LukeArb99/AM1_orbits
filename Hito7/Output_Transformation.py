#Módulo para pasar de soluciones en X, Y, Z
#a frecuencias, ritmos y velocidades
from numpy import zeros,empty, asarray
from math import log

def Intervalos_Escala(x,E1,tau):
    '''
    x = solucion en x del sistema
    E1 = escala
    tau = tono musical
    o = octava -- cogemos 3
    '''
    k=7
    lamnbda= 1/2

    x1=zeros(len(x))

    '''Normalizacion de la variable'''
    alpha = (2**k-1)/(max(x)-min(x))
    beta = -alpha*min(x)+1

    for i in range(0,len(x)):
        x1[i] = alpha*x[i]+beta

    '''Mapeo al valor mas proximo'''
    mu=2**(lamnbda/6)-1
    D=empty((len(x1),len(E1)))
    for i in range(0,len(x1)):
        for j in range (0,len(E1)):
            if abs(x1[i]-E1[j])<=mu:
                D[i,j]=0
            else:
                D[i,j]=x1[i]

    L=[]
    for i in range(0,len(x1)):
        L.append(min(D[i,:]))

    f=55*2**((tau+12*0-10)/12)

    '''Frecuencias de las notas'''
    F=[]
    for i in range(0,len(x1)):
        F.append(f*L[i])

    '''valores de la frecuencia para MIDI'''
    theta=[]
    for i in range(0,len(F)):
        if abs(F[i]) / 440 <= 0:
            theta.append(69)
        else:
            theta.append(69 + 12 / log(2) * log(abs(F[i]) / 440))
    theta2=[]
    for i in range(0,len(theta)):
        theta2.append(round(theta[i]))
    return asarray(theta2)


def Ritmo(y,tp):
    '''
    y = solucion y del sistema
    tp = tiempo musical
    '''

    R=[0,1,2,3,4,5,6]
    '''
    0 - semifusa
    1 - fusa
    2 - semichorchea
    3 - corchea
    4 - negra
    5 - blanca
    6 - redonda
    '''
    '''Normalizacion de la variable'''
    alpha = (max(R)-min(R))/(max(y)-min(y))
    beta = -alpha*min(y)+min(R)
    y1 = zeros(len(y))

    for i in range(0,len(y)):
        y1[i] = alpha*y[i]+beta

    '''Redondeo a valor proximo'''
    y2=[]
    for i in range(0,len(y)):
        y2.append(round(y1[i]))

    '''Conversion a MIDI'''
    Y=[]
    for i in range(0,len(y2)):
        Y.append(60/tp*2**y2[i]/2**4)

    return asarray(Y)

def Dinamica(z):
    '''
    z = solucion del sistema z
    '''

    U=[10, 30, 45, 60, 75, 92, 108, 127]
    '''
    0-10 ppp
    11-30 pp
    31-45 p
    46-60 mp
    61-75 mf
    76-92 f
    93-108 ff
    109-127 fff
    '''

    '''Normalizacion de la variable'''
    alpha = (max(U)-min(U))/(max(z)-min(z))
    beta = -alpha*min(z)+min(U)
    z1 = zeros(len(z))

    for i in range(0,len(z)):
        z1[i] = alpha*z[i]+beta

    '''Mapeo al valor mas proximo'''
    mu=10
    D=empty((len(z),len(U)))
    for i in range(0,len(z)):
        for j in range (0,len(U)):
            if abs(z[i]-U[j])<=mu:
                D[i,j]=0
            else:
                D[i,j]=z[i]

    L=[]
    for i in range(0,len(z)):
        L.append(min(D[i,:]))

    Z=[]
    for i in range(0,len(L)):
        if max(L) != 0:
            Z.append(L[i]/max(L))
        else:
            Z.append(100)

    return asarray(Z)
