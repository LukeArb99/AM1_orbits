import numpy as np

def g(x):
    resultado = - 0.1*x**4 - 0.15*x**3 - 0.5*x**2 - 0.25*x + 1.2
    return resultado

def diferencia_adelante(f,x,h):
    derivada = (f(x+h) - f(x))/h
    return derivada

def extrapolacion_Richarson_n(f,x,h):
    m = 4
    N = np.zeros((m,m))
    for i in range(0,m):
        N[i,0] = diferencia_adelante(f,x,h)
        for j in range(1,i+1):
            N[i,j] =  N[i,j-1] + (N[i,j-1] - N[i-1,j-1])/(2**j - 1)
        h = h/2
    return N   