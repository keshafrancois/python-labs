def SumList(x):
    sum = 0
    list = [int(input()) for i in range(x)]
    for i in range(x):
        sum += list[i]
    print(sum)
    print()

SumList(10)
