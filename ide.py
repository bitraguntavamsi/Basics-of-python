 # identity "is,is not"

# verify the 'ids' of the variable

a=10
print(id(a))
A=10
print(id(A))
# both are same ids

a=10
b=20
c=30
print(a is b)
print(a is c)
print(a is not b)
print(a is not c)
