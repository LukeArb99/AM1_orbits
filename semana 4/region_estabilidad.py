from numpy import linspace,zeros,array,abs,transpose,float64
import matplotlib.pyplot as plt
from Esquemas_temporales import RK4, Euler_Implicito,Crank_Nicolson

def Region_estabilidad(Scheme,N,x0,xf,y0,yf):
    #Scheme===Esquema numerico
    #N===mallado
    #x===nuemro real
    #y===nuemro imaginario
    x, y = linspace(x0, xf, N), linspace(y0, yf, N)
    rho =  zeros( (N, N),  dtype=float64)

    for i in range(N): 
      for j in range(N):

          w = complex(x[i], y[j])
          r = Scheme( 1., 1., 0., lambda u, t: w*u )
          rho[i, j] = abs(r) 

    return rho, x, y


def Test_Estabilidad():
    schemes = [RK4, Euler_Implicito,Crank_Nicolson]

    for scheme in schemes: 
      rho, x, y  = Region_estabilidad(scheme, 100, -4, 2, -4, 4)
      plt.contour( x, y, transpose(rho), linspace(0, 1, 11) )
      plt.axis('equal')
      plt.grid()
      plt.show()

if __name__ == '__main__':  
    Test_Estabilidad()
