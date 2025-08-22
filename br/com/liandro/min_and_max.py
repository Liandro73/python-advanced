a = [6, 2, 3, 8, 1, 4]

# Worse way to get the minimum value
a.sort()
print(a[0])

# Better way to get the minimum value
print(min(a))


# Worse way to get the maximum value
a.sort()
index = len(a)
print(a[index-1])

# Better way to get the maximum value
print(max(a))