from django.shortcuts import redirect, render
from home.models import Tejido
import numpy as np
import math
#------------------------------------------------------------------------------------------
distancias = []
#------------------------------------------------------------------------------------------
def grafo(request):
    global distancias
    matriz = getTabla()
    
    dimension = len(matriz)
    distancias = getDistancias(matriz)

    diccionario = {"distancias": distancias}
    return render(request, "grafo.html", diccionario)
#------------------------------------------------------------------------------------------
def getTabla():
    datos = Tejido.objects.get_queryset()
    matriz = []
    for i in datos:
        i = vars(i)
        keys = [key for key in i if not key.startswith('_') and not key.startswith('id') and not key.endswith('id')]
        aux = []
        for k in keys:
            aux.append(i[k]);
        matriz.append(aux)
    return matriz
#------------------------------------------------------------------------------------------
def getDistancias(matriz):
    dimension = len(matriz)
    distancias = np.zeros((dimension,dimension))
    for i in range(dimension):
        for j in range(i,dimension):
            if i != j:
                distancia = math.dist(matriz[i], matriz[j])
                distancias[i][j] = distancia # se manejan los indices arriba de la diagonal
                distancias[j][i] = distancia # se ivierten los indices para la parte de abajo de.
    return distancias
#------------------------------------------------------------------------------------------
def getGrafo(request):
    umbral = request.GET["umbral"]
    sizee = len(distancias)

    if not(umbral):
        umbral = 0
    else:
        umbral = float(umbral)

    umbrales = []
    for i in range(sizee):
        for j in range(i, sizee):
            dist = float(distancias[i,j])
            if dist == 0 or (dist > umbral) :
                umbrales.append([i,j,dist, "True" ])
            else:
                umbrales.append([i,j,dist, "False" ])
    
    diccionario = {"umbrales": umbrales}
    return render(request, 'umbral.html', diccionario)
#------------------------------------------------------------------------------------------