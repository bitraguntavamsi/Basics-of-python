# Tuple
# syntax:var=(val1,val2,val3,____valn)


# t1=(10,'don',30,10.0,4+9j,50)
# print(t1)
# print(type(t1))
# print(len(t1))

# tuple builtin functions
#1.count(): ------>integer
# t1=(10,20,'don',8+9j,9.7,10,10,10,10)
# c=t1.count(10)
# print(c)

#2.index():

# t1=(10,20,30,40,10,10,10,30)
# c=t1.index(10)
# c=t1.index(10,1,6)
# print(c)

# fetching of elements in the tuple:

# By using for loop:
# t1=(10,20,30,40,10,10,10,30,'krishna',8+9j)
# for i in range(0,len(t1)):
#     print(t1[i])

# By using iterable:
# t1=(10,20,30,40,10,10,10,30,'krishna',8+9j)
# for i in t1:
#     print(i)

# By using while loop:
# t1=(10,20,30,40,10,10,10,30,'krishna',8+9j)
# i=0
# while i<len(t1):
#     print(t1[i])
#     i+=1


