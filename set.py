#Set
# syntax---set={val1,val2,val3,____valn}

# s1={1,2,3+9j,5.0,8,9}
# print(s1,type(s1))
# print(len(s1))
# s1={}----> empty set becomes a DICTIONARY

# s1={1,2,3,4,5,(1,2,3,4),9,"krishna",10.5,8+9j}

# BUILT IN FUNCTIONS

#1.clear():
#set.clear():
# print(s1)
# s1.clear()
# print(s1)

#2.copy():
#set.copy():---> return type set
# print(s1)
# s2=s1.copy()
# print(s2)

#3.add():
#set.add(value)
# s1.add(1000)
# s1.add(2)
# print(s1)

# 4.pop()
# set.pop()
# print(s1)
# s2=s1.pop() # inside pop we cannot return any thing
# s3=s1.pop()
# s4=s1.pop() 
# print(s2)
# print(s3)
# print(s4)

#5.remove()
#set.remove(value)--->none
# print(s1)
# s1.remove(8+9j)
# s1.remove(10.5)
# s1.remove(1000) # error 1000 is not present----> keyerror
# print(s1)

#6.discard()
#discard(value)---->none
# s1.discard(5)
# s1.discard(1000) # in discard error not come but in remove key error should be came:
# print(s1)

# s1={1,2,3,4,5,100,6,7,8,9}
# s2={1,2,3,4,10,12,34,55}
# s3={1,2,3,7,12,100,35,55}

#7.union:---------> display the all the elements
#set.union(*set)
# res=s1.union(s2)
# print(res)
# res1=s1.union(s2,s3)
# print(res1)


#8.update:--------> display the all the elements nothing but a union
#set.update(*set)
# print(s1)
# s1.update(s2)
# print(s1)

#9.intersection:----> display the common elements
#set.intersection(*set)
# res=s1.intersection(s2)
# print(res)

#10.intersection_updtae:----> nothing but a intersection
#set.intersection_update(*set)---> returns None
# s1.intersection_update(s2)
# print(s1)

#11.difference----> remove all common elements from s1 and display the remaining elements from s1:
#set.differenece(*set)---> returns SET
# res=s1.difference(s2)
# print(res)

#12.difference_update----. similar to difference
#set.difference-update(set)
# s1.difference_update(s2)
# print(s1)

#13.symmetric_difference----->remove the all common elements and display the remaining elements from s1 and s2
#set.symmetric_difference(set)--->returns SET
# res=s1.symmetric_difference(s2)
# print(res)

#14.symmetric_difference_update----->similar to symmetric_difference
#set.symmetric_difference_update(set)
# s1.symmetric_difference_update(s2)
# print(s1)

# s1={1,2,3,4,5,6,7,8,100,300,600,900}
# s2={1,2,3}
# s3={100,300,600,900}

#15. issubset
#set.issubset(set)-----returns boolean
# print(s1.issubset(s2))
# print(s2.issubset(s1))
# print(s3.issubset(s1))

#16.superset
#set.issuperset(set)----->returns boolean
# print(s1.issuperset(s2))
# print(s2.issuperset(s1))
# print(s1.issuperset(s3))


#17.disjoint
#set.disjoint(set)--->boolean
# s1={1,2,3,4,5}
# s2={10,20,30,40,50,}
# s3={100,200,300,400,500,30}
# print(s1.isdisjoint(s2))
# print(s2.isdisjoint(s3))