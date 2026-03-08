def busqueda_lineal(arr, elemento):
    for i in range(len(arr)):
        if arr[i] == elemento:
            return i
    return -1


def busqueda_binaria_interativa(arr, elemento, izq=0, der=None):
    if not der:
        der = len(arr) - 1
    while izq <= der:
        print(arr[izq:der + 1])
        medio = (izq + der) // 2
        if arr[medio] == elemento:
            return medio
        elif arr[medio] < elemento:
            izq = medio + 1
        else:
            der = medio - 1
    return -1


def busqueda_binaria_recursiva(arr, elemento, izq=0, der=None):
    if not der:
        der = len(arr) - 1
    if izq > der: return -1
    medio = (izq + der) // 2
    if arr[medio] == elemento:
        return medio
    elif arr[medio] < elemento:
        return busqueda_binaria_recursiva(arr, elemento, medio + 1, der)
    else:
        return busqueda_binaria_recursiva(arr, elemento, izq, medio - 1)



arr = [20, 10, 40, 30, 50, 60, 70, 80, 90, 100, 110, 120, 130]
print(busqueda_lineal(arr, 30))

arr.sort()
print(busqueda_binaria_interativa(arr, 40))
print(busqueda_binaria_recursiva(arr, 40))

