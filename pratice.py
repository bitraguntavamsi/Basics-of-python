# a=int(input("a:"))
# b=int(input("b:"))
# c=a<<b
# print(c)
# d=a>>b
# print(d)
# if (c>d):
#     print("c is greater")
# else:
#     print("d is greater")

# a=int(input("a:"))
# b=int(input("b:"))
# c=int(input("c:"))
# d=int(input("d:"))
# e=a+b+c+d
# print(e)
# if (e/400)*100<=400:
#     print("he is pass")
# else:
#     print("he is fail")


# gender=input("enter the Gender\nmale\tfemale\tother\noption:")
# if gender in["male","female","other"]:
#     age=int(input("enter the age:"))
#     if gender in ["male","other"]:
#         if age>=18 and age<=65:
#             print("eligable for vote")
#         else:
#             print("not eligiable to vote")
#     else:
#         if age>=21 and age<=45:
#             print("eligiable")
#         else:
#             print("not eligible")
# else:
#     print("invaild gender")


'''operation=input("select the operation\n +/t-/t*/t/t\noption:")
if operation  in ["+","-","*","/"]:
    value1=int(input("a:"))
    value2=int(input("b:"))
    if operation in "+":
        print(value1+value2)
    elif operation in "-":
        print(value1-value2)
    elif operation in "*":
        print(value1*value2)
    else:
        print(value1/value2)'''


'''gender=input("enter the gender:\nmale\tfemale\tother\noption:")
if gender in["male","female","other"]:
   age=int(input("enter the age:"))
    if gender  in ("male","other") and age>=18 and age<=65 or gender in "female" and age>=21 and age<=45:
         print("eligible for vote")
    else:
        print("not eligiable for vote")
else:
    print("invaild gender")'''


# a=input("enter your char:")
# if a in ('aeiou'):
#     print("vowels")
# else:
#     print("it is consonent")





# a=int(input("enter the number:"))
# b=int(input("enter the number:"))
# c=a+b
# if c%2==0:
#     print("it is even number")
# else:
#         print("it is odd number")

# a=int(input("enter the a:"))
# b=int(input("enter the b:"))
# print(a is b)

# a=input("enter the char:")
# if (a>='a' and a<='z'):
#     print("it is lower case")
# elif a>='A' and b<='Z':

# n=int(input("n:"))
# for i in range (5,0,-1):
#         print(i)

# a=int(input("num1:"))
# b=int(input("num2:"))
# c=int(input("num3:"))
# d=int(input("num4:"))
# if a>b:
#     if a>c:
#         if a>d:
#             print('num1 is greater')
#         else:
#             print("num4 is greater")
#     else:
#         if b>c:
#             if b>d:
#                 if b>a:
#                     print("num2 is greater")
#                 else:
#                     print("num4 is greater")
# else:
#     if c>a:
#         if c>b:
#             if c>d:
#                 print("num3 is greater")
#             else:
#                  print("num4 is greater")
                    
'''a=int(input("a:"))
b=int(input("b:"))
c=int(input("c:"))
d=int(input("d:"))
if (a>b or a>c or a>d) or (b>a or b>d or b>c) or (c>a or c>b or c>d) or (d>a or d>b or d>c):
    if a>b and a>c and a>d:
        print("a is greater")
    elif b>a and b>c and b>d:
        print("b is greater")
    elif c>a and c>b and c>d:
        print("c is greater")
    else:
        print("d is greater")'''

'''a="siva krishna"
for i in a:
    print(i,end=" ")'''

'''i=1
while i<=10:
    print(i)
    i+=1

i=9
while i>=0:''i=
    print(i,end=" ")
    i-=1'''


# i=1
# while i<=20:
#     if i%2==0:
#      print(i,end=" ")
#     i+=1

# i=1
# while i<=20:
#     if (i//2)*2==i:
#        print(i,end="")
#        i+=1


# a="vamsi"
# i=0
# while i<len(a):
#     print(a[i])
#     i+=1
          
# while loop for all the even index characters:
# a="sivakrishna"
# i=0
# while i<=len(a):
#     if i%2==0:
#         print(a[i])
#     i+=1

# usins " f string  " printing the tables 
'''a=int(input("a:"))
i=1
while i<=10:
    print(f"{a}*{i}={a*i}")
    i+=1

a=5
i=1
while i<=10:
    print(f"{a}*{i}={a*i}")
    i+=1'''
# printing the table in reverse in table:
'''a=9
i=10
while i>=1:
    print(f"{a}*{i}={a*i}")
    i-=1'''

# using for loop printing the table
'''a=5
for val in range(10,0,-1):
    print(f"{a}*{val}={a*val}")

a=int(input("a:"))
for i in range(1,11):
    print(f"{a}*{i}={a*i}")'''

# Break keyword using for loop:

# for i in range(1,11):
#     if i==7:
#      break
#     print(i)

# Break keyword using while loop:

# i=1
# while i<=10:
#    if i==9:
#       break
#    print(i)
#    i+=1

# Continue keyword using for loop:            

# for i in range(1,11):
#   if i==5 or i==8:
#      continue
#   print(i)

# Continue keyword using while loop:
# i=1
# while i<=10:
#     if i==4:
#         i+=1
#         continue
#     print(i)
#     i+=1

# Pass keyword 

# n=int(input("a:"))
# if n==1:
#     pass
# else:
#     print("sai room")


# Pass keyword using while loop printing odd numbers:
# for i in range(1,11):
#  if i%2==0:
#     pass
#  else:
#     print(i)

# Pass keyword using while loop printing even numbers:
#i=1
# while i<=10:
#     if i%2!=0:
#         i+=1
#         pass
#     else:
#         print(i)
#         i+=1

# ASCii values:
# print(ord("i"))
# print(chr(65))

# Nested for loop:
# for i in range(1,11):
#     for j in range(1,9):
#         print(i,end=" ")

# printing matrix multiplication:
# for i in range(1,4):
#     for j in range(1,5):
#         print(f"{i}*{j}={i*j}",end=" ")

# n=int(input("n:"))
# num=1
# for i in range (1,n+1):
#     num=num*i
# print(num)



   



          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
          
           
          
          
          
          
          
          
          
    










































