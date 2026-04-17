def quicksort(array):
    if len(array) < 2:
        return array

    pivo = array[0]
    array_numeros_menores = [ i for i in array[1:] if i < pivo ]
    array_numeros_maiores = [ i for i in array[1:] if i > pivo ]
    return quicksort(array_numeros_menores) + [pivo] + quicksort(array_numeros_maiores)


array = [14, 22, 444, 2, 6, 8, 10]
print(quicksort(array))
