def fat(num):
    if num == 1:
        return 1
    else: 
        return num * fat(num - 1)

num = int(input("enter a number: "))
print(fat(num))
