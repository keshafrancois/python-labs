l = [int(i) for i in input().split(' ')]

m1 = max(l)
m0 = min(l)

for i in range(len(l)):
    if l[i] == m1:
        l[i] = m0
    elif l[i] == m0:
        l[i] = m1
print(l)