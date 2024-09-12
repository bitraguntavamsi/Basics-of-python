# Built in methods in list:
  #list has 11 built in methods

#1.clear:
#list.clear()
# l1=[1,2,3,4,5]
# print(l1)
# l1.clear()
# print(l1)

#2.copy:
#list.copy()
# l1=[1,2,3,4,5]
# print(l1)
# l2=l1.copy()
# print(l2)

#3.count:
#list.count(value)
# l1=[1,1,2,2,2,3,4,4,4,5,9,6.0,6.1,6.0]
# c1=l1.count(6)
# print(c1)

#4.append:
#list.append(object)
# l1=[1,2,3,4]
# print(l1)
# l1.append(1000)
# l1.append('don')
# l1.append([10,20])
# print(l1)

#5.extend:
#list.extend(iterable)
# l1=[1,2,3,4,5]
# l1.extend([10,20,30])
# l1.extend('don')
# print(l1)

#6.insert:
# list.insert(index,object)
# l1=[1,2,3,4,5]
# l1.insert(1,100)
# print(l1)
# l1.insert(-2,1000)
# print(l1)

#7. pop:
#list.pop(index)
# l1=[1,2,3,4,5]
# l1.pop(3)
# print(l1)

#8.remove:
# list.remove(value)
# l1=[1,2,3,4,5]
# l1.remove(3)
# print(l1)

#9.index:
#list.index(value,start,stop)
# l1=[10,20,30,60,50,20,30]
# l2=l1.index(20,2,6) #5
# l3=l1.index(100,0,6) # value error: 100 is not in list
# print(l2)
# print(l3)


#10.reverse:
#list.reverse()
# l1=[10,20,30,60,50,20,30]
# l1.reverse()
# print(l1)

#11.sort:
#list.sort()
# l1=[10,20,30,60,50,20,30]
# l1.sort() # ascending order
# print(l1)
# l1.sort(reverse=True) # descending order
# print(l1)

#list  concatination:
# l1=[1,8+9j,7,9,0]
# l2=['don',3.0,8+9j,29]
# l3=l1+l2
# print(l3)

# list repeation:
# l1=[1,3,5,7]
# l2=l1*3
# print(l2)

