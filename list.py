# LIST
'''l1=[10,20.5,True,'don',(1+9j)]
print(l1)
print(len(l1))
print(type(l1))

# list support indexing both postive and negative values:
l1=[1,3,6,9,10]
print(l1[2])
print(l1[-2])
print(l1[-5])
print(l1[0])'''

#list support's slicing:
'''l1=[10,20,80,60,40,10,80,90,100]
print(l1)
print(l1[1:4:1])
print(l1[2:7:1])
print(l1[4:8:1])
print(l1[:4:1])
print(l1[1:4])
print(l1[::])
print(l1[1:100])
print(l1[::2])
print(l1[-1:-5:-1])
print(l1[-1:-6:-1])
print(l1[6:1:-1])
print(l1[1:9:0]) #slice step cannot be zero
print(l1[1:4.9]) #TypeError: slice indices must be integers or None or have an __index__ method
print(l1[::-1])
print(l1[-1:-4:-1])'''


# list are mutable collection
'''l1=[10,20,30]
print(l1)
l1[-1]='iron man'
print(l1)'''

#looping list
'''l1=[10,20,30,40,50,60]
for i in l1:
    print(i,end=" ")

for i in range(len(l1)):
    print(l1[i],end=' ')

i=0
while len(l1)>i:
    print(l1[i],end=' ')
    i+=1
for i in range(-1,-5,-1):
    print(l1[i],end=' ')
for i in range (len(l1)-1,-1,-1):
    print(l1[i],end=' ')'''
