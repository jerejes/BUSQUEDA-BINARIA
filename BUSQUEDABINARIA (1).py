
def busquedaBinario(tupla, x):
    inicio = 0
    final = len(tupla)-1
    while inicio <= final:
        centro = (inicio+final)//2
        if tupla[centro] == x:
            print(f"El índice del inicio luego de la búsqueda es:  {inicio}")
            print(f"El índice del centro luego de la búsqueda es: {centro}")
            print(f"El índice del final luego de la búsqueda es: {final}")
            print(f"El término buscado {x} SÍ está dentro de la lista.")
            break
        elif tupla[centro] > x:
            final = centro-1

        else:
            inicio = centro+1
    else:
        print(f"El índice del inicio luego de la búsqueda es:  {inicio}")
        print(f"El índice del centro luego de la búsqueda es: {centro}")
        print(f"El índice del final luego de la búsqueda es: {final}")
        print("El número NO está en la tupla.")


lista = list(range(0, 300))
dato = int(input("Ingrese el número a buscar: "))
busquedaBinario(lista, dato)
