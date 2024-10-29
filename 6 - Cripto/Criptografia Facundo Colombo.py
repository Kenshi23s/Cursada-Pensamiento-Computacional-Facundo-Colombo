import os

vocals = {"á": "a", "é": "e", "í": "i", "ó": "o", "ú": "u"}


# para buscar en una coleccion while
# para recorrer toda una coleccion for
# los breaks y returns en ciclos aumentan la complejidad matematica

def leer_archivo(nombre):
    with open(nombre, "r", encoding='utf-8') as archivo:
        return archivo.read()


def crear_archivo(nombre, contenido):
    """
      con esto puedo decir q solo pasen strings
    :type nombre: str
    :type contenido: str
    """
    with open(nombre, "w", encoding='utf-8') as archivo:
        return archivo.write(contenido)


def codificar_caracter(letra, alfabeto, k):
    i = obtener_indice(letra, alfabeto)
    return alfabeto[(i + k) % len(alfabeto)]


def obtener_indice(letra, alfabeto):
    i = 0
    while i < len(alfabeto) and alfabeto[i] != letra:
        i += 1
    return i


# buscar la funcion replace
def normalizar(mensaje):
    normalizado = ""

    for i in range(len(mensaje)):
        letra = mensaje[i]
        letra = letra.lower()
        if letra in vocals.keys():  # in se fija si existe en la coleccion
            letra = vocals[letra]
        normalizado += letra

    return normalizado


def decodificar_caracter(letra, alfabeto, k):
    return codificar_caracter(letra, alfabeto, -k)


def decodificar(mensaje, alfabeto, k):
    mensaje = normalizar(mensaje)
    codificado = ""
    for caracter in mensaje:
        if caracter in alfabeto:
            codificado += decodificar_caracter(caracter, alfabeto, k)
        else:
            codificado += " "
    return codificado


def codificar(mensaje, alfabeto, k):
    mensaje = normalizar(mensaje)
    codificado = ""
    for caracter in mensaje:
        if caracter in alfabeto:
            codificado += codificar_caracter(caracter, alfabeto, k)
        else:
            codificado += " "
    return codificado


def codificar_archivo(archivo, alfabeto, k):
    texto = leer_archivo(archivo)
    texto = codificar(texto, alfabeto, k)
    nuevonombre = archivo.replace(".txt", ".enc")
    return crear_archivo(nuevonombre, texto)

def decodificar_archivo(nombre,alfabeto,k):
    archivo = leer_archivo(nombre)
    archivo= decodificar(archivo, alfabeto, k)
    return crear_archivo(nombre.replace(".enc", ".dec"), archivo)