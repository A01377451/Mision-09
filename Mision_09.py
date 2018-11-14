#Autor: Jocelyn lópez Ortíz
#Misión 9 - listas


def extraerPares(lista):
    nuevaLista =[]
    for dato in lista:
         if dato%2==0:
             nuevaLista.append(dato)
    return nuevaLista


def extraerMayoresPrevio(lista):
    nuevaLista=[]
    for k in range(1, len(lista)):
        if lista[k]>lista[k-1]:
            nuevaLista.append(lista[k])
    return nuevaLista


def intercambiarParejas(lista):
    nuevaLista =[]
    if len(lista)%2==0:
        for k in range(0, len(lista),2):
            nuevaLista.append(lista[k + 1])
            nuevaLista.append(lista[k])
    else:
        for k in range(0, len(lista)-1, 2):
            nuevaLista.append(lista[k + 1])
            nuevaLista.append(lista[k])
        nuevaLista.append(lista[-1])
    return nuevaLista


def intercambiarMM(lista):
    if len(lista)>0:
        mayor = lista[0]
        indiceMayor = 0
        menor = lista[0]
        indiceMenor=0
        for k in range(1, len(lista)):
            if lista[k]>mayor:
                mayor=lista[k]
                indiceMayor = k
        for k in range(1, len(lista)):
            if lista[k]<menor:
                menor=lista[k]
                indiceMenor = k
        lista[indiceMayor] = menor
        lista[indiceMenor] = mayor
    return lista


def promediarCentro(lista):
    if len(lista)>2:
        mayor = lista[0]
        menor = lista[0]
        for k in range(1, len(lista)):
            if lista[k] > mayor:
                mayor = lista[k]
        for k in range(1, len(lista)):
            if lista[k] < menor:
                menor = lista[k]
        promedio = (sum(lista)-mayor-menor)//(len(lista)-2)
    else:
        promedio=0
    return promedio


def calcularEstadistica(lista):
    if len(lista)>0:
        promedio = sum(lista)/len(lista)
        suma = 0
        for dato in lista:
            suma += (dato-promedio)**2
        desviacion = (suma/(len(lista)-1))**0.5
    else:
        promedio = 0
        desviacion = 0
    return (promedio, desviacion)


def calcularSuma(lista):
    suma = sum(lista)
    if len(lista) < 1:
        return suma
    elif len(lista) ==1:
        if lista [0]==13:
            suma-=lista[0]
        return suma
    else:
        for k in range (0, len(lista)):
            if lista[k] == 13:
                suma -= lista[k]
                if not k == 0:
                    suma-= lista[k-1]
                if not k==len(lista):
                    suma -= lista[k+1]
    return suma
