x = {"a" ,"b", "c"}
print(x)
print(type(x))

y = set()
print(y)

y.add(1)

print(y)

x = {1, 2, 3}
y = {3, 4, 5}

# Intersection
# Common between x and y

print(x & y)

# Union
# All unique values of set x and y

print (x | y)

#Set Difference
# Remove anything in x , that is  in y
print(x - y)


# Symetric Difference

print({1,2,4} ^ {2, 5,6})


# Check if set on left is superset of set on right

print({1,2,3,4,5} >= {2,3,4})


# Check if set on right is superset of set on left

print({1,2,3,4,5} <= {2,3,4})



x = {20,30,40}
x.discard(60)
print(x)
