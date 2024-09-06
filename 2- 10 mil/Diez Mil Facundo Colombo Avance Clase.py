# suman puntos los unos y cinco
# se empieza con 0 punto
# en cada ronda cada jugador realiza una jugada
# por cada 1 obtenido se suman 100 puntos
# por cada 5 obtenido se suman 50 puntos
# se podria usar una tupla o diccionario para redirigir los valores(?)
# bucle: hasta que alguno llegue a 10 000
# tirar dados
# tiro dados
# anotar resultados
# sumo resultados
# chequeo si alguien gano
# !/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Sep  6 07:27:33 2024

@author: Facundo Colombo
"""
import random


def tirar_cubilete():
    # se puede ir al reves? de 5 a 0?
    cubilete = [0] * 6
    for i in range(0, len(cubilete) - 1):
        cubilete[i] = random.randint(1, 6)

    return cubilete


def cuantos_hay(elemento, lista):
    cantidad = 0

    for num in lista:
        if num == elemento:
            cantidad += 1

    return cantidad


# por cada uno obtenido, se suman 100 puntos, mientras que 3 unos suman 1000 puntos, 4
# unos suman 1100, y 5 unos suman 10000 puntos.

# es una buena practica tener un solo return en las funciones en lo posible,
# lo tengo en cuenta para las siguientes ejercitacions / casos donde me encuentre este problema
def puntos_por_unos(lista_dados):
    cantidad = cuantos_hay(1, lista_dados)

    if cantidad <= 0: return 0

    if cantidad < 3: return cantidad * 100

    if cantidad < 5: return 1000 + (cantidad - 3) * 100

    return 10000


# por cada cinco obtenido se suman 50, mientras
# que 3 cincos suman 500, 4 cincos suman 550, y 5 cincos suman 600 puntos
# se podria ver alguna otra forma de agregar condiciones infinitas?
def puntos_por_cincos(lista_dados):
    cantidad = cuantos_hay(5, lista_dados)

    if cantidad <= 0: return 0

    if cantidad < 3: return cantidad * 50

    if cantidad < 5: return 500 + (cantidad - 3) * 50

    return 600


def total_puntos(lista_dados):
    return puntos_por_unos(lista_dados) + puntos_por_cincos(lista_dados)


def hay_10mil(puntajes_jugadores):
    for puntaje in puntajes_jugadores:
        if puntaje >= 10000: return True

    return False


def acumular_puntos(puntajes_acumulados, puntajes_ronda_actual):
    for i in range(len(puntajes_acumulados)):
        puntajes_acumulados[i] += puntajes_ronda_actual[i]

    return puntajes_acumulados


def jugar_ronda(cant_jugadores):
    puntajes_ronda = [0] * cant_jugadores
    for i in range(cant_jugadores):
        puntajes_ronda[i] = total_puntos(tirar_cubilete())

    return puntajes_ronda


def partida_completa(cant_jugadores):
    puntajes_jugadores = [0] * cant_jugadores
    rondas_jugadas = 0
    while not hay_10mil(puntajes_jugadores):  # deberia poner un watchdog por las dudas
        puntajes_ronda = jugar_ronda(cant_jugadores)
        puntajes_jugadores = acumular_puntos(puntajes_jugadores, puntajes_ronda)
        rondas_jugadas += 1

    return rondas_jugadas


def cant_rondas_promedio(cant_jugadores, cant_partidas):
    cant_rondas = 0
    for _ in range(0, cant_partidas):
        cant_rondas += partida_completa(cant_jugadores)

    return cant_rondas / cant_partidas


def chance_de_terminar(cant_jugadores, max_rondas, cant_partidas):
    rondasAcertadas = 0
    for i in range(cant_partidas):
        if partida_completa(cant_jugadores) < max_rondas:
            rondasAcertadas += 1

    return rondasAcertadas / cant_partidas 
