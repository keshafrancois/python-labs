def CountList(x):
    count=0
    list = [int(input()) for i in range(x)]
    for i in list:
        if i == 0:
            count +=  1
    print(count)

CountList(10)