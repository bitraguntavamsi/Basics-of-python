# List comprehension:
# syntax:list=[value for loop if condition]

# l1=[]
# for i in range(1,51,1):             }
#     l1.append(i)          ----------} not 
#     print(l1,end=" ")               }


# By using list comprehension we should write code in single line:

# print 1 to 50 numbers by using list comprehension:
#  l1=[i for i in range(1,51,1)]
# print(l1)

# print even numbers by using list comprehension:
# l1=[i for i in range(1,11,1) if i%2==0 ]
# print(l1)

# printing 1 to n :
# n=int(input("n:"))
# l1=[i  for i in range(1,n+1)]
# print(l1)

# printing string:
# n=int(input("n:"))
# l1=['krishna'  for i in range(1,n+1)]
# print(l1)

# printing alaphabets:
# l1=[chr(i) for i in range(97,123)]
# print(l1)
# l1=[chr(x) for x in range(ord("A"),ord('Z'))]
# print(l1)

# nested loop using:
# l1=[x for x in range(1,4) for y in range(1,4)]
# print(l1)

# string using
s='krishna'
l1=[i for  i in s]
print(l1)

