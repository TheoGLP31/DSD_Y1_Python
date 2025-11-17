def lup(number):
    for i in range(0, number):
        newNumber = print(i, ".", ((i * number) + (i * number) + (i * number) + (i * i)))

num = input("give number")

lup(int(num))