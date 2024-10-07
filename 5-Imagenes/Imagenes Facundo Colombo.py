from turtle import Shape

import numpy
import numpy as np
import matplotlib.pyplot as plt
arr = np.random.random((10, 12, 3))
DimensionColores = {"rojo": 0, "verde": 1, "azul": 2}


def obtener_imagen(nom_arch):
    return plt.imread(nom_arch)


def separar_canales(imagen):
    return imagen[:, :, 0], imagen[:, :, 1], imagen[:, :, 2]


def seleccionar_canal(imagen, nombre_canal):
    return imagen[:, :, DimensionColores[nombre_canal]]


def convertir_a_grises(imagen):
    colores = separar_canales(imagen)
    gris = 0.299 * colores[0]  # Averiguar en casa
    gris += 0.587 * colores[1]
    gris += 0.114 * colores[2]
    return gris


def multiplicar_y_sumar(array1, array2):
    return np.sum(array1 * array2)


# consultar en clase, dudas sobre resolucion
def aplicar_stencil_a_pos(array, posicion, stencil):
    limx = stencil.shape[0] + 1 // 2
    limy = stencil.shape[
               1] + 1 // 2  # // es division entera, sin decimales. lo hago para agarrar todo lo de arriba y de abajo en las dimension y no lo hago con la division normal porque me daba numero con decimales

    esquinainferiorX = (posicion[0] - limx) // 2
    esquinaSuperiorX = (posicion[0] + limx) // 2
    esquinainferiorY = (posicion[1] - limy) // 2
    esquinaSuperiorY = (posicion[1] + limy) // 2

    # pos2 = posicion[0] - limx:posicion[0] + limx esto se puede hacer de alguna forma?
    print(posicion)
    print("X desde " + str(esquinainferiorX) + " Hasta " + str(esquinaSuperiorX))
    print("Y desde " + str(esquinainferiorY) + " Hasta " + str(esquinaSuperiorY))
    nuevoarray = array[esquinainferiorX: esquinaSuperiorX, esquinainferiorY: esquinaSuperiorY]
    return multiplicar_y_sumar(stencil, nuevoarray)  # sera asi?


def aplicar_stencil(array, stencil):
    copia = array.copy()

    shapeX = stencil.shape[0]
    shapeY = stencil.shape[1]
    copyShapeX = copia.shape[0]
    copyShapeY = copia.shape[1]
    for i in range(shapeX, copyShapeX):
        for j in range(shapeY, copyShapeY):
            if i + shapeX < copyShapeX and j + shapeY < copyShapeY:
                copia[i, j] = aplicar_stencil_a_pos(copia, (i, j), stencil)
    return copia


