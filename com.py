# List comprehension:
# syntax:list=[value for loop if condition]


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
# s='krishna'
# l1=[i for  i in s]
# print(l1)


#Tuple comprehension:::

# Tuple comphresion is not possible if try to acheive return generator object and expression is called generator expression
#t=( x for x in range(1,10))
#print(t)                              #<generator object <genexpr> at 0x000002039A384940>


#Set comprehension:::
#syntax=set={value for loop if condition}

# s={x for x in range(1,11)}
# print(s)                                #{1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
 
# n=int(input('a:'))                                          
# s={int(input(f"value{x}:")) for x in range(1,n+1)}          #a:4
# print(s)                                                    #value1:3
                                                              #value2:4
                                                              #value3:5
                                                              #value4:6
                                                              #{3, 4, 5, 6}


#Dictionary comprehension:
#syntax:dictionary={key:value for loop if condition}

#d={x:x**2 for x in range(1,10)}
#print(d)                                                     #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

# n=int(input("n:"))
# d={x:x**2 for x in range(1,n+1)}                             #n:5
#print(d)                                                      #{1: 1, 2: 4, 3: 9, 4: 16, 5: 25}

#d={x:chr(x) for x in range(65,91)}
#print(d)                                                      #{65: 'A', 66: 'B', 67: 'C', 68: 'D', 69: 'E'-------90:'z'}


# Dictionary comphrenhension using two itearbles and zip:

# first=[1,2,3,4,5,6,7,8]
# last=[10,20,30,40,50,60,70,80]
# d={x:y for x,y in zip(first,last)}
# print(d)                                                       #{1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60, 7: 70, 8: 80}


# first=[1,2,3,4,5,6,6]
# last=[10,20,30,40,50,60,60]
# res=zip(first,last)
# print(res)                                                      #<zip object at 0x000002291085CC40> beacuse list not mentioned:



# first=[1,2,3,4,5,6,6]
# last=[10,20,30,40,50,60,70]
# res=zip(first,last)
# print(list(res))                                                    #[(1, 10), (2, 20), (3, 30), (4, 40), (5, 50), (6, 60), (6 70)]


# first=[1,2,3,4,5]
# last=[10,20,30,40,50]
# res=zip(first,last,'abcdef',[10,20])                                  #[(1, 10, 'a', 10), (2, 20, 'b', 20)]
# print(list(res))