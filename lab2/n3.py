a=int(input())
b=int(input())
c=int(input())
if a > b and a > c:
    print(a)
elif b>a and b>c:
    print(b)
elif c>a and c>b:
    print(c)
elif (a==b and a>c) or (a==c and a>b):
    print(a)
elif (b==a and b>c) or (b==c and a<b):
    print(b)
elif (c==b and a<c) or (a==c and c>b):
    print(c)
else:
    print('idk what happened but it is your fault')