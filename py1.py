'''a=int(input('a:'))
b=int(input('b:'))
c=int(input('c:'))
d=int(input('d:'))
if a>b:
    if a>c:
        if a>d:
            print('a is greater ')
        else:
            print('d is greater ')
elif b>a:
    if b>c:
        if b>d:
            print('b is greater')
        else:
            print('d is greater')
    else:
        if c>a:
            if c>b:
                if c>d:
                 print('c is greater')
        else:
            print('d is greater')
else:
    if d>a:
        if d>c:
            if d>b:
                print('d is greater')
        else:
            print('b is greater')'''

a="vamsi"
i=0
while i<=len(a):
    if i%2==0:
        print(a[i])
    i+=1


a="vamsi"
i=0
while i<len(a):
    if i%2 != 0:
        print(a[i])
    i+=1