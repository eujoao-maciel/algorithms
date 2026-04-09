def buscaMenorIndice(arr):
    menor_valor = arr[0]
    menor_indice = 0

    for i in range(1, len(arr)):
        if arr[i] < menor_valor:
            menor_valor = arr[i]
            menor_indice = i
    return menor_indice

def ordenacaoPorSelecao(arr):
    novoArr = []

    for i in range(len(arr)): 
        menor_indice = buscaMenorIndice(arr)
        novoArr.append(arr.pop(menor_indice))

    return novoArr

array = [5, 3, 6, 2, 10]
print(ordenacaoPorSelecao(array))
