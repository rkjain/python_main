#create a dict 
# Keys should be immutable
# Float, int, string, tuple, 
x = {}
x["name"] = "bob"
x["age"] = 26

print(list(x.keys()))

print("name" in x)

print(x.get("name") if x.get("name") else x.get("age"))
print(x.get("name") if x.get("height") else x.get("age"))


sentence = "Hi  my name is rishabh is  How are you ? \
I am writing logic to count the occurence of each word"

y = {}
sl = sentence.split()
print(sl)

for i in sl:
	if y.get(i) is not None:
		y[i] += 1
	else:
		y[i] = 1

print(list(y.values()))
print(y)


x = {"a": 1, **{"b": 2, "c":3} }
print(x)
