import numpy as np
import scipy.integrate as integrate
from Probema_Cauchy import Problema_de_Cauchy
from Esquemas_temporales import RK4

def G(Y):
    X = np.zeros(6)
    X[:3] = Y

    GX = CR3BP(X, 0.)
    G = GX[3:]

    return G

def CR3BP(X, t):
    # Implement the CR3BP equations of motion here
    x,y,z,vx,vy,vz = [X[0],X[1],X[2],X[3],X[4],X[5]]
    mu=0.012150586550569

    d=np.sqrt((x-mu)**2+y**2+z**2)
    r=np.sqrt((x-1+mu)**2+y**2+z**2)
    dvxdt = x + 2 * vy - (1-mu) * ( x + mu )/d**3 - mu*(x-1+mu)/r**3
    dvydt = y - 2 * vx - (1-mu) * y/d**3 - mu * y/r**3
    dvzdt = - (1-mu)*z/d**3 - mu*z/r**3

    return np.array([vx,vy,vz,dvxdt,dvydt,dvzdt])

def System_matrix(F, U0, t):
    # Implement the Jacobian matrix calculation here
    # Calculate partial derivatives of F
    F_dU0 = np.gradient(F, U0)

    # Copy partial derivatives to the Jacobian matrix
    A[:3, :3] = F_dU0[:3, :3]  # Copy partial derivatives of position components
    A[3:6, 3:6] = F_dU0[3:6, 3:6]  # Copy partial derivatives of velocity components

    # Return the Jacobian matrix
    return A

def Eigenvalues_QR(A, lanbda):
    # Perform QR decomposition of the Jacobian matrix
    Q, R = np.linalg.qr(A)

    # Extract diagonal matrix of R
    diag_R = np.diag(R)

    # Calculate eigenvalues
    lanbda = diag_R

    return lanbda

def plotm(U, mu, N):
    # Implement the plotting routine for the orbit and Jacobian eigenvalues

    return

def qplot(x, y, N):
    # Implement the quick plotting routine for the orbit

    return

if __name__ == "__main__":
    N = 20000    # Number of timesteps
    M = 6           # Number of variables
    U = np.zeros((N, M))      # State vector
    E = np.zeros((N, M))      # Error for different timesteps
    Time = np.linspace(0, 4*np.pi/0.3, N)   # Time domain
    NL = 5           # Number of Lagrange points
    U0 = np.zeros((NL, M))   # Lagrange points
    eps = np.zeros(M)       # Disturbances around Lagrange points
    A = np.zeros((M, M))     # Jacobian
    lanbda = np.zeros(M, dtype=complex)  # Eigenvalues

    # Initialize Lagrange points
    for i in range(1, NL + 1):
        U0[i-1] = [0.8, 0.6, 0., 0., 0., 0.]

    # Integrate the orbits and compute errors
    for i in range(1, NL + 1):
        # Solve the Cauchy problem for the orbit
        # U = Cauchy_ProblemS(Time, CR3BP, U0[i-1])
        U = Problema_de_Cauchy(CR3BP,Time,U0[i-1],RK4)

        # Plot the orbit
        # plotm(U, mu, N)

        # Calculate error in the orbit
        # E = Error_Cauchy_Problem(Time, CR3BP, RK_method, order, U, E)

        # Print the Lagrange point and its stability
        print("Lagrange point = ", U0[i-1])
        print("F in Lagrange point = ", CR3BP(U0[i-1], 0.))
