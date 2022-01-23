# Creating empty lists
al = list()
be = []

# Initalizing lists
ga = [1, 2, 3]
de = list([1, 2, 3])
th = list(range(1, 4)) # Same as above two lists

# Store anything 
recipie = ["Pi", 3, 0.14, True] # Valid list
duplicates = [1, 1, 1, 1, 1, 1, 1, 1, 1, 1] # Valid list

# Slicing lists
bread = list("bread") # initailize list similar to de 
sliced = bread[1:4:2] # slice from index 1 to 4, step of 2
payment = bread[-3:-1] # slice from index -3 to -1

# List Comprehensions
ones = [1, 2, 3, 4, 5]
twos = [2 * x for x in ones] # [2, 4, 6, 8, 10]

# Nested Lists
nested = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
print(nested[1][1]) # 5

# To find more, use help(list) or google search any feature you wish to know more about