
# one can do tuple and list unpacking  into vairables

x = (1)
print(type(x))


x = (1,)
print(type(x))

print(x + (4,5,6,7))
print(x)

a, *b, c =  [1, 2, 3, 4]
print(a,b,c)

a, *b, c = (1,2,3,4)
print(a, b, c)

print((1,2,4)[0])

a,*b, c = [10,20,30,40]
print(a,b,c)