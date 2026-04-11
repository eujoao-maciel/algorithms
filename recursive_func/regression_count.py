
def regression_count(num):
    print(num)

    if (num <= 1):
        return
    else:
        regression_count(num - 1)

regression_count(10)

