a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=((a+b+c)/300)*100
print(d)
if a>=1 and a<100 and b>=1 and b<100 and c>=1 and c<100:
    if a>90:
        print("A Grade")
    elif b>80:
        print("b Grade")
    elif c>70:
        print("c Grade")
    else:
        print("fail")    
else:
    print("you entred a worng number")
      











             