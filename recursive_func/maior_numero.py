def maior_numero(array):
    if len(array) == 1:
        return array[0]

    maior_do_resto = maior_numero(array[1:])

    if array[0] > maior_do_resto:
        return array[0]
    else:
        return maior_do_resto

array = [ 1, 2, 3, 4, 5, 33, 6, 7 ]
print(maior_numero(array))
