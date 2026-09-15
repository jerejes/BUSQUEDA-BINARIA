
def ordenamientoSeleccion(lis):

    for i in range(len(lis) - 1):
        min = i

        for j in range(i + 1, len(lis)):
            if lis[j] < lis[min]:
                min = j

        lis[i], lis[min] = lis[min], lis[i]


def ordenamientoburbuja(lis):

    for i in range(1, len(lis)):
        for j in range(len(lis)-1):
            if lis[j] > lis[j+1]:
                lis[j], lis[j + 1] = lis[j + 1], lis[j]


def ordenamientoInserccion(lis):

    for i in range(1, len(lis)):
        j = i
        while j > 0 and lis[j - 1] > lis[j]:
            lis[j], lis[j - 1] = lis[j - 1], lis[j]
            j -= 1


lista = [2, 8, 5, 3, 9, 4, 1]
lista2 = [2, 8, 5, 3, 9, 4, 1]
lista3 = [2, 8, 5, 3, 9, 4, 1]
print(f"Lista desordenada:{lista}")
ordenamientoSeleccion(lista)
print(f"LISTA ORDENADA POR SELECCION{lista}")

ordenamientoburbuja(lista2)
print(f"LISTA ORDENADA POR BURBUJA{lista2}")

ordenamientoInserccion(lista3)
print(f"LISTA ORDENADA POR INSERCION{lista3}")
