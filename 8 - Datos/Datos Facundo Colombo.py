import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

# pd.dataframe(listadetuplas) devuelve data frame
# listadetuplas.columns =["DNI","Cuenta"] se sete columnas
# dataframe.head() los primeros 5 items del data frame
# dataframe.tail() la ultima fila
import cumples


# Ejercicio 1 En cumples


# Ejercicio2


def SeleccionMasGoles():
    return copaAmericaData.groupby("Seleccion")["Cant_goles"].max().head(1)


def SeleccionMasConvocados():
    return copaAmericaData.groupby("Seleccion").size().idxmax()


def SeleccionMasCara():
    data = copaAmericaData.groupby("Seleccion")["Valor_mill_euros"].sum()  # suma todos los valores intenros
    return data.idxmax()  # me devuelve el mas alto


def ObtenerGoleador():
    id = copaAmericaData["Cant_goles"].idxmax()
    return copaAmericaData.iloc[id]


def CrearColumnaDeGoles():
    copaAmericaData["GolesXPartido"] = copaAmericaData["Cant_goles"] / copaAmericaData["Cant_partidos"]


def ObtenerMasGolesPorPartido():  # creo q esta mal, esperaba a messi y me dio Guillermo Martínez
    id = copaAmericaData["GolesXPartido"].idxmax()
    return copaAmericaData.iloc[id]


def JugadoresEnSeleccionConMasGolesXPartido():  # nombre largo
    return copaAmericaData.groupby("Seleccion")["GolesXPartido"].sum().idxmax()


def AlturaPromedioSeleccion():  # nombre largo
    return copaAmericaData.groupby("Seleccion")["Altura"].mean()


def AlturaMaximaSeleccion():  # nombre largo
    return copaAmericaData.groupby("Seleccion")["Altura"].max()


def ObtenerZurdos():  # nombre largo
    return copaAmericaData[copaAmericaData["Destreza_pie"] == "zurdo"]


def PosicionConMasZurdos():
    return ObtenerZurdos().groupby("Posicion").size().idxmax()


def RelacionZurdos():
    porPosicion = copaAmericaData.groupby("Posicion").size()
    zurdosEnPosicion = ObtenerZurdos().groupby("Posicion").size()

    return zurdosEnPosicion / porPosicion


# ejercicio3
def ConvertirADatetime():
    copaAmericaData["Fecha_nac"] = pd.to_datetime(copaAmericaData["Fecha_nac"], format="%d/%m/%Y")
    copaAmericaData["MesNacimiento"] = copaAmericaData["Fecha_nac"].dt.month  # para agruparlos por mes (hay otra forma?)
    copaAmericaData["Trimestre"] = copaAmericaData["Fecha_nac"].dt.quarter


def GraficarNacimientos():
    plt.plot(range(12), copaAmericaData.groupby("MesNacimiento").size())
    plt.show()

def GraficarNacimientosPorSeleccion():
    plt.plot(range(12), copaAmericaData.groupby("MesNacimiento").size())
    plt.show()

copaAmericaData = pd.read_csv('CopaAmerica_equipos.tsv', sep='\t')
CrearColumnaDeGoles()
ConvertirADatetime()
