def len_array(array):
    if len(array) == 0:
        return 0

    return 1 + len_array(array[1:])

array = [ 3, 4, 5, 6, 7 ]
print(len_array(array))
