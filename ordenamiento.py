def ordenamiento_burbuja(arr):
    n = len(arr)
    for i in range(n):
        for j in range(n - i - 1):
            print(arr)
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    return arr


def ordenamiento_seleccion(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    return arr


def ordenamiento_insercion(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]
        j = i - 1
        print(f"key: {key}, i: {i}, j: {j}")
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
            print(arr)
        arr[j + 1] = key
    return arr


def ordenamiento_mezcla(arr):
    if len(arr) <= 1:
        mitad = len(arr) // 2
        arr_izq = arr[:mitad]
        arr_der = arr[mitad:]

    ordenamiento_mezcla(arr_izq)
    ordenamiento_mezcla(arr_der)

    i = j = k = 0
    while i < len(arr_izq) and j < len(arr_der):
        if arr_izq[i] < arr_der[j]:
            arr[k] = arr_izq[i]
            i += 1
        else:
            arr[k] = arr_der[j]
            j += 1
        k += 1

    while i < len(arr_izq):
        arr[k] = arr_izq[i]
        i += 1
        k += 1

    while j < len(arr_der):
        arr[k] = arr_der[j]
        j += 1
        k += 1

    return arr


def ordenamiento_rapido(arr):
    if len(arr) <= 1:
        return arr
    pivote = arr[len(arr) // 2]
    arr_izq = [x for x in arr if x < pivote]
    arr_mitad = [x for x in arr if x == pivote]
    arr_der = [x for x in arr if x > pivote]
    return ordenamiento_rapido(arr_izq) + arr_mitad + ordenamiento_rapido(arr_der)



#arr = [10, 5, 20, 30, 40, 10]
#print(ordenamiento_burbuja(arr))

arr = [50,10,40,5,30,10]
#print(ordenamiento_seleccion(arr))
#print(ordenamiento_insercion(arr))
#print(ordenamiento_mezcla(arr))
print(ordenamiento_rapido(arr))