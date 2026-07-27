a = [ 1, 2, 3]
print(id(a))
b = a
print(id(b))
b.append(4)
print(a)
print(id(a), id(b))

a = 1
print(id(a))
b = a 
print(id(b))
b = 2
print(a)
print(id(a), id(b))