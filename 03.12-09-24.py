# 1.Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple.
# Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)
nested_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple = []
for num in nested_tuple:
    if isinstance(num,tuple):
        flattened_tuple.extend(num)
    else:
        flattened_tuple.append(num)
print (tuple(flattened_tuple))

# 2.Write a Python program to sort a tuple of tuples based on the second element of each tuple.
# Example Tuple: ((1, 2), (3, 1), (5, 0))Expected Output: ((5, 0), (3, 1), (1, 2))"""

tup = ((1, 2), (3, 1), (5, 0))
sort = tuple(sorted(tup ,key=lambda x:x[1]))
print(sort)