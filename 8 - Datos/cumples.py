# la paradoja de los cumpleaños
import random


def leer_csv(ruta):
    coleccion = []
    with open(ruta, 'r', encoding='utf-8') as archivo:
        for linea in archivo:
            coleccion.append(linea.split(","))
    return coleccion

#CLASE DATOS EJERCICIO 1
def agrupar_filas_por(filas, columna):
    equipos = sin_repetidos(convertir_en_lista(filas, 'Equipo'))
    return equipos


def contar_jugadores(filas, lista_equipos):
    jugadoresEquipos = {}
    for equipo in lista_equipos:
        jugadoresEquipos[equipo] = len(filtrar_filas(filas, 'Equipo', equipo))

    return jugadoresEquipos

def obtener_equipos_y_transformar():
    return lista_de_listas_a_dicc(leer_csv("datos_jugadores.csv"))


def lista_de_listas_a_dicc(lista_de_listas):
    keys = lista_de_listas[0]
    diccionarios = []
    for i in range(1, len(lista_de_listas)):
        listaActual = lista_de_listas[i]
        diccionarios.append(dict(zip(keys, listaActual)))

    return diccionarios



filasArchivo = obtener_equipos_y_transformar()

def coincidencia(lista):
    i = 0
    encontrado = False
    while not encontrado and i < (len(lista) - 1):
        encontrado = lista[i] in lista[i + 1:]
        i += 1

    return encontrado


def sin_repetidos(lista):
    if not coincidencia(lista):
        return lista

    sinrepe = []
    for item in lista:
        if item not in sinrepe:
            sinrepe.append(item)

    return sinrepe


def filtrar_filas(filas, columna, valor):
    dics = []
    for fila in filas:
        if fila[columna] == valor:
            dics.append(fila)

    return dics


def convertir_en_lista(filas, columna):
    lista = []
    for fila in filas:
        lista.append(fila[columna])

    return lista


def hay_coincidencia_en_equipo(filas, equipo):
    filtrado = filtrar_filas(filas, "Equipo", equipo)

    col = convertir_en_lista(filtrado, 'dia_mes')

    return coincidencia(col)


def todos_los_equipos(filas):
    nombre = "Equipo"
    col = convertir_en_lista(filas, nombre)
    return sin_repetidos(col)


def porc_equipos_con_coincidencia(filas, equipos):
    contador = 0
    for equipo in equipos:

        if hay_coincidencia_en_equipo(filas, equipo):
            contador += 1

    print(contador)
    maximosEquipos = len(equipos)
    print(maximosEquipos)
    return contador / maximosEquipos


def fechas_cumples(n):
    fechas = [] * n
    for i in range(n):
        fechas[i] = random.randint(1, 365)
    return fechas


def chances_coincidencia(n, n_rep):
    casosfavorables = 0
    for repes in range(n_rep):
        cumples = fechas_cumples(n)
        if coincidencia(cumples):
            casosfavorables += 1

    return casosfavorables / n_rep


def VelezJugadorViejo(filas):
    jugadores = filtrar_filas(filas, "Equipo", "Velez")
# 15. ¿Cuál es el jugador más viejo de Velez?
 #16. ¿Cuál es el jugador más petiso de cada equipo?
# 17. ¿Cuál es el promedio de edad de los delanteros de Talleres de Córdoba