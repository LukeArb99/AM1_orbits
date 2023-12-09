from numpy import zeros,empty

def Intervalos_Escala(x,delta,k,chi,tau, o):
    '''
    x = solucion en x del sistema
    delta = division del tono, se supone que va de 0 a 0.5
    k = numero de octavas: 0<=k<7
    chi = estructura de la escala
    tau = tono musical
    o = octava
    '''
    
    '''Generacion de Escala'''
    lamnbda= 1/delta 

    p=int(6*k/lamnbda)

    S=[]
    E=[]
    V=[]
    x1=zeros(len(x))

    #Escala de intervalos
    for i in range(0,p):
        S.append(2**(i*lamnbda/6))

    ##hallar el vector binario V
    for i in range(0,p):
        if chi[i] in S:         ##Aqui va la estructura de la escala tonal del cual no se el formato 
            V.append(1)
        else:
            V.append(0)

    for i in range(0,p):
        E.append(S[i]*V[i])
    
    E1 = list(filter(lambda x: x != 0, E))

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

    f=55*2**((tau+12*o-10)/12)

    '''Frecuencias de las notas'''
    F=[]
    for i in range(0,len(x1)):
        F.append(f*L[i])

    return F
