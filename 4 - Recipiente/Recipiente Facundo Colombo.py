import random
import numpy as np
import matplotlib.pyplot as plt


# Facundo Colombo

def crear_recipiente(x, y):
    col = np.zeros((x, y), np.int16)
    col = setearbordesY(col)
    col = setearbordesX(col)

    return col


def setearbordesY(recipiente):
    maximo = recipiente.shape[0] - 1
    for j in range(recipiente.shape[1]):
        recipiente[0, j] = -1
        recipiente[maximo, j] = -1
    return recipiente


def setearbordesX(recipiente):
    maximo = recipiente.shape[1] - 1
    for i in range(recipiente.shape[0]):
        recipiente[i, 0] = -1
        recipiente[i, maximo] = -1
    return recipiente


def agregar_particulas(recipiente, posicion, cantidad):
    # bordes son 0 o shape de dimension
    # for i in range(posicion):
    #     if posicion[i] == 0 or posicion >= recipiente.shape[i]:
    #         return recipiente
    recipiente[posicion] += cantidad
    return recipiente


def es_borde(recipiente, posicion):
    return recipiente[posicion[0], posicion[1]] < 0


def dame_uno_al_azar(lista):
    return lista[random.randint(0, len(lista) - 1)]


def vecinos(recipiente, posicion):
    misVecinos = []

    dirs = [-1, 1]
    for i in dirs:
        for j in dirs:
            posicionChequear = (posicion[0] + i, posicion[1] + j)
            if not es_borde(recipiente, posicionChequear):
                misVecinos.append(posicionChequear)

    return misVecinos


def mover_particula(recipiente, posicion):
    coleccion = vecinos(recipiente, posicion)
    azar = dame_uno_al_azar(coleccion)
    recipiente[posicion[0], posicion[1]] -= 1
    recipiente[azar[0], azar[1]] += 1


def mover_muchas_particulas(recipiente, posicion, cantidad):
    for i in range(cantidad):
        recipiente = mover_particula(recipiente, posicion)

    return recipiente


def mover_particulas_recipiente(recipiente, recipiente_original):
    dim = recipiente_original.shape
    for i in range(dim[0]):
        for j in range(dim[1]):
            recipiente = mover_muchas_particulas(recipiente, (i, j), recipiente_original[i, j])

    return recipiente


def evolucionar_recipiente(recipiente, k):
    for i in range(k):
        recipiente = mover_particulas_recipiente(recipiente, np.copy(recipiente))

    return recipiente


def simular_difusion_horizontal():
    recipiente = crear_recipiente(35, 35)
    for i in range(10):
        visualizar_recipiente(recipiente)
        recipiente = evolucionar_recipiente(recipiente, 30)

    return recipiente


def inicializar_particulas(recipiente, cantidad):
    for i in recipiente.shape[1]:
        if not es_borde(recipiente, (1, i)):
            recipiente[1, i] = cantidad

    return recipiente


def Testing():
    r = crear_recipiente(5, 5)
    es_borde(r, (1, 1))  # False
    es_borde(r, (0, 1))  # True
    es_borde(r, (2, 4))  # True
    es_borde(r, (2, 2))  # False


# Esto deberia dar siempre 250, porque no se pierden particulas

def visualizar_recipiente(recipiente):
    plt.figure()
    cmap = plt.cm.Blues  # inicializar mapa de colores azules
    cmap.set_under("black")  # darle color negro a las posiciones con valor menor a vmin
    plt.imshow(recipiente, cmap=cmap, vmin=0)  # graficar el heatmap usando vmin = 0
    plt.colorbar()  # graficar la barra de escala de colores
    plt.show()  # terminar de graficar y mostrar la figura
