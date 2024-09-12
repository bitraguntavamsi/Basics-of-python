# "if" statement:

'''syntax:
if condition:
    #statements'''

# percentage of three subjects and grades

'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=((a+b+c)/300)*100
print(d)
if d>=90 and d<=99:
    print("d got A grade")
elif d<=89 and d>=70:
    print("d got a B grade")
elif d<=69 and d>=50:
    print("d got a C grade")
elif d<=49 and d>=30:
    print("d got a D grade")

else:
    print("d is fail")'''

# wheather the year is leap year or not 
'''a=int(input("a:"))
print(a)
if a%4==0 and a%100!=0:
    print("a is leap year")
elif a%400==0:
    print("100th year")
else:
    print("not a leap year")'''
 
a=int(input("enter the age:"))
print(a)
if a>=1 and a<=9:
    print("a is child")
elif a>=10 and a<=19:
    print("a is teen ager")
elif a>=20 and a<=59:
    print("a is adulter")
else:
    print("a is senior citizen")







