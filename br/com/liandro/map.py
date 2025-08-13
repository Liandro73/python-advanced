
def multiply_by_two(x):
    return x * 2

values = [1, 2, 3, 4, 5]

# It only duplicates the list
# Output: [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
print(multiply_by_two(values))

# Correct approach
# Output: [2, 4, 6, 8, 10]
new_value = map(multiply_by_two, values)
new_values = list(new_value)
print(new_values)