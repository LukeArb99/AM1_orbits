import numpy as np

def leapfrog(f, x0, t0, tf, dt):
    """
    Integra la ecuación diferencial x'(t) = f(x, t) utilizando el esquema de Leapfrog.
    Args:
        f: La función diferencial.
        x0: El valor inicial del estado x.
        t0: El tiempo inicial t0.
        tf: El tiempo final tf.
        dt: El paso de tiempo dt.
    Returns:
        Una matriz que contiene los valores del estado en cada paso de tiempo.
    """
    t = np.arange(t0, tf, dt)
    # x = np.zeros_like(t)
    # x[0] = x0

    N=len(t)-1
    Nv=len(x0)
    x = np.zeros( (Nv, N+1), dtype=np.float64 ) 


    x[:,0]=x0

    for i in range(1, len(t)):
        # Paso 1
        k1 = f(x[:,i - 1], t[i - 1])

        # Paso 2
        mid_x = x[:,i - 1] + 0.5 * dt * k1

        # Paso 3
        k2 = f(mid_x, t[i - 1] + 0.5 * dt)
        x[:,i] = x[:,i - 1] + dt * k2

    return x

def f(x, t):
    """
    La función diferencial del problema de tres cuerpos restringido a órbita circular.
    Args:
        x: El estado actual del sistema.
        t: El tiempo actual.
    Returns:
        La derivada del estado actual del sistema.
    """
    x1, x2, x3 = x[0], x[1], x[2]
    return np.array([x2, -x1, 0])


# Parámetros del problema
m1, m2, m3 = 1,5,9
r = 1

# Condiciones iniciales
x0 = np.array([m1,m2,m3])

# Tiempo de simulación
t_final = 1000
dt = 0.01

# Simulación
x = leapfrog(f, x0, 0, t_final, dt)
print(x)

# Visualización
import matplotlib.pyplot as plt

plt.plot(x[:, 0], x[:, 1])
plt.xlabel("x")
plt.ylabel("y")
plt.show()