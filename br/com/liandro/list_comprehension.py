x = [1, 2, 3, 4, 5, 6]
y = [i**2 for i in x]
z = [i for i in y if i%2==1]
w = [i for i in y if i%2==0]

print("Working with list comprehension")
print(x)
print(y)
print(z)
print(w)