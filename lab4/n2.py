l = [int(i) for i in input().split()]
a = list()
for i in range(1, len(l)):
    if l[i] > l[i - 1]:
        a.append(l[i])
print(" ".join(str(i) for i in a))