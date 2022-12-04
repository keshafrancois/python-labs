list = []
k = int(input('Введите количество элементов\n'))
for n in range(1,k + 1):
	list.append(n)
print(list)

def f(l):
	l1 = []
	for num in l:
		if l.index(num) % 2 != 0:
			l1.append(num)
	return(print(l1))				
f(list)