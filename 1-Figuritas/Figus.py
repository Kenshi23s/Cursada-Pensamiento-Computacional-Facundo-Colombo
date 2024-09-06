import random


# Facundo Colombo
def llenar_album(cantfigus):
    album = [0] * cantfigus
    contador_figus = 0

    while (sum(album) < cantfigus):
        album = pegar_figu(album, cantfigus)
        contador_figus = contador_figus + 1

    return album


def pegar_figu(album, cantfigus):
    figu = random.randint(0, cantfigus - 1)
    album[figu] = 1
    return album


def cuantas_figus_para_llenar_album(figus_total):
    album = [0] * figus_total
    contador_albumes = 0

    while (sum(album) < figus_total):
        album = pegar_figu(album, figus_total)
        contador_albumes += 1

    return contador_albumes


def cuantas_figus_para_llenar_albumes(figus_total, n_albumes):
    albumesActuales = [0] * n_albumes
    contador = 0
    while (len(albumesActuales) > contador):
        albumesActuales[contador] = cuantas_figus_para_llenar_album(figus_total)
        contador += 1

    return albumesActuales


def promedio_figus_para_llenar_album(figus_total, n_albumes):
    resultado = sum(cuantas_figus_para_llenar_albumes(figus_total, n_albumes))
    return resultado / n_albumes


# album lleno => lista de ints. cantidad maxima => int
def chance_llenar_album(resultados_album_lleno, cantidad_maxima_figus):
    index = 0
    resultadosFavorables = 0
    while (len(resultados_album_lleno) > index):

        elem = resultados_album_lleno[index]
        index += 1
        if (elem <= cantidad_maxima_figus):
            resultadosFavorables += 1

    return resultadosFavorables / len(resultados_album_lleno)


# lo multiplico por 100 ya que el resultado sino estaria normalizado


def llenar_y_devolver_chance(figus_total_album, cantidad_maxima_figus, n_albumes):
    chances = 0

    for i in range(n_albumes):
        chances += chance_llenar_album(llenar_album(figus_total_album), cantidad_maxima_figus)
        
    return chances / n_albumes
