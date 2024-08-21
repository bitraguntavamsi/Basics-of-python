# Logical operator

a,b,c=10,20,10
print(a==b and a==c)
print(a==b or a==c)
print(not a==c)

# based on preccedence table 
a,b,c=10,20,10
print(a==c and not a==b or not a*2==c-10 or not a<b and b+10)