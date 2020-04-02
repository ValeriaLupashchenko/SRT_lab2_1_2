from math import sin, cos, pi
from random import randrange
import matplotlib.pyplot as plt
import matplotlib as mpl

def iexp(n):
    return complex(cos(n), sin(n))

def DFT(x_n, N):
    return [sum((x_n[k] * iexp(-2 * pi * i * k /N) for k in range(N)))
            for i in range(N)]

def show(t, name="DFT"):
    plt.title(name)
    plt.xlabel('N')
    plt.ylabel(name)
    plt.plot([i for i in range(len(t))], t, color='blue',
             label='X(k)')
    plt.show()

def create_process(n=12, N=256, W=900):
        """Function for create random signal"""
        x = [0 for i in range(N)]
        for i in range(N):
            for j in range(n):
                A = randrange(0, 100)
                q = randrange(0, 100)
                SINUS = A * sin((W/n * (j + 1) / n) * i + q)
                x[i] += SINUS
        return [round(x[i], 3) for i in range(len(x))]

x_n = create_process()
a = DFT(x_n, len(x_n))

show(x_n, name="X(t)")
show(a)
