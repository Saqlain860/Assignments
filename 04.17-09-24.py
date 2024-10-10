# Create a dictionary where the keys are tuples representing coordinates (x, y) and the values are city 
# names. Write a Python program to print the city name for a given coordinate. Example Dictionary: 
# #{(40.7128, -74.0060): "New York", (34.0522, -118.2437): "Los Angeles"} # Input: (40.7128, -74.0060) 
# # Expected Output: "New York"
coordinates_to_city = {
    (40.7128, -74.0060): "New York",
    (34.0522, -118.2437): "Los Angeles",
}
def get_city_name(coordinate):
    return coordinates_to_city.get(coordinate, "Coordinate not found")
coordinate = (40.7128, -74.0060)
city_name = get_city_name(coordinate)
print(f"The city at coordinate {coordinate} is {city_name}.")

# Write a Python program to sort a tuple of tuples based on the second element of each tuple. 
# python # Example Tuple: ((1, 2), (3, 1), (5, 0)) # Expected Output: ((5, 0), (3, 1), (1, 2))

def sort_tuple(tuples):
    return tuple(sorted(tuples,key=lambda x:x[-1]))
tupl = ((1, 2), (3, 1), (5, 0))
sort = sort_tuple(tupl)
print(sort)

# Write a Python program to find the minimum and maximum elements in a tuple of integers. 
# python # Example Tuple: (10, 20, 5, 40, 25) # Expected Output: Min: 5, Max: 40

exam_tup = (10, 20, 5, 40, 25)
min_of = min(exam_tup)
max_of = max(exam_tup)
print(f"min: {min_of}, max: {max_of}")

# Given a tuple containing nested tuples, write a Python program to flatten it into a single tuple. 
# python # Example Tuple: (1, (2, 3), (4, 5, 6)) # Expected Output: (1, 2, 3, 4, 5, 6)
 
nested_tuple = (1, (2, 3), (4, 5, 6))
flattened_tuple=[]
for i in nested_tuple:
 if isinstance(i,tuple):
  flattened_tuple.extend(i)
 else:
  flattened_tuple.append(i)
print(tuple(flattened_tuple))
 

 