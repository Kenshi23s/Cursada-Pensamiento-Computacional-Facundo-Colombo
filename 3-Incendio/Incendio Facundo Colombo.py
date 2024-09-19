import random
import numpy as np
import matplotlib.pyplot as plt


# Facundo Colombo

def generar_bosque(n):
    return np.array([0] * n)


def cuantos(bosque, tipo_celda):
    apariciones = 0
    for i in range(len(bosque)):
        if tipo_celda == bosque[i]:
            apariciones += 1

    return apariciones


def suceso_aleatorio(p):
    return p > random.randint(0, 100)


def brotes(bosque, p):
    for i in range(len(bosque)):
        if bosque[i] != 0: continue
        if not suceso_aleatorio(p): continue
        bosque[i] = 1
    return bosque


def rayos(bosque, f):
    for i in range(len(bosque)):
        if bosque[i] != 1: continue
        if not suceso_aleatorio(f): continue
        bosque[i] = -1
    return bosque


def propagacion(bosque):
    for i in range(len(bosque)):
        if bosque[i] >= 0: continue
        quemarvecinos(bosque, i)
    return bosque


def quemarvecinos(bosque, indice):
    siguiente = indice + 1
    if siguiente < bosque.size and bosque[siguiente] == 1:
        bosque[siguiente] = -1
        quemarvecinos(bosque, siguiente)

    anterior = indice - 1
    if anterior >= 0 and bosque[anterior] == 1:
        bosque[anterior] = -1
        quemarvecinos(bosque, anterior)


def limpieza(bosque):
    for i in range(len(bosque)):
        if bosque[i] >= 0: continue
        bosque[i] = 0
    return bosque


def dinamica(n, a, p, f):
    bosque = generar_bosque(n)
    cantidadvivos = 0
    for i in range(a):
        bosque = brotes(bosque, p)
        bosque = rayos(bosque, f)
        bosque = propagacion(bosque)
        bosque = limpieza(bosque)
        cantidadvivos += cuantos(bosque, 1)

    return cantidadvivos / a * 100


def arboles_sobrevivientes(f, a, n):
    col = np.zeros(101)
    for p in range(101):
        col[p] = dinamica(n, a, p, f)

    return col


def p_optimo(f, a, n):
    col = arboles_sobrevivientes(f, a, n)
    # indice 1 = p
    # indice 2 = indice
    actual = (-1, -1)
    for i in range(len(col)):
        if col[i] > actual[0]:
            actual = (col[i], i)

    return actual[1]


def graficar(p):
    chances = arboles_sobrevivientes(100, 500, 2)
    plt.plot(range(101), chances)
    plt.show()
