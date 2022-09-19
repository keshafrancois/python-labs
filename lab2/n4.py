a=int(input())
b=int(input())
c=int(input())
if a!=b and a!=c and b!=c:
    print('There are 3 unique numbers')
elif (a==b and a!=c) or (a==c and a!=b) or (b==c and a!=b):
    print('There is 1 unique numbers')
elif a==b==c:
    print('There are no unique numbers')
else:
    print('There can not be any mistake \nMy code is perfect')
print('There can not be any mistake \nMy code is perfect')