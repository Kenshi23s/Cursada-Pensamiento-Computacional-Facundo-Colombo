def mejor_puntuada(diccionario):
    masAlto = 0
    mejor = ''
    for keys in diccionario.keys():
        atributos = diccionario[keys]
        puntos = atributos[2]
        if puntos < masAlto: continue
        mejor = atributos[1]
        masAlto = puntos
    return mejor
