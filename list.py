#  List will be helpful to store multiple items in a single variable.

"""
 Use lists if you have a collection of data that does not need random access. Try to choose lists when you need a simple, iterable collection that is modified frequently.
"""


# list variables
fruits = ["banana", "apple", "watermelon", "kiwi", "grapes"]
# print(fruits)

prices = ["$100", "$150", "$10.50"]

numbers = [1, 2, 3, 4, 5]

my_list = [1, "car", 10.40, True]
print(fruits, 
      prices, 
      numbers,
      my_list)


# printing the list items
# print('\n# printing the list items')
# print(fruits, id(fruits)) #id(fruits) ,python gives the memory address on ur local where the friuts is stored
# print(prices, id(prices))
# print(numbers)
# print(my_list)

# # # check the data type
# print('\n# check the data type')
# print(type(fruits))
# print(type(numbers))


# # # nested list
# print('\n# nested list')
# my_custom_list = [fruits, prices, [6, 10, 2]]
# print(my_custom_list)


# # # length of list
# print('\n# length of the list')
# print(len(fruits))

# # access a specific element in list
# print('\n# access a specific element in list')
# print(fruits[2])
# print(fruits[0])
# print(fruits[-1])
# print(fruits[-2])
# print(prices[1])

# # nested list
# print('\n# nested list')
# my_custom_list = [fruits, prices, [6, 10, 2]]
# print(my_custom_list)

# new_list =[prices, numbers, fruits]
# print(new_list)

# # slicing lists
"""Note that in slicing frutis[start:end]
start is first index and inclusive while end 
is the last index and exclusive
print(fruits[0:2]) 
print(fruits[1:4])
However if the start orn the ends are not indicated they are inclusive
print(numbers[:2])
print(numbers[2:])
"""

# print('\n# slicing lists')
# print(fruits[0:2]) 
# print(fruits[1:4])
# print(fruits[1:])
# print(numbers[:2])
# print(numbers[2:4])

# # peform actions on list
# # return attributes and methods of an object
# print('\n# dir() method')
# print(dir(fruits))

# # modify particular index of list with new item
# print('\n # modify particular index of list with new item')
# print(prices)
# prices[1] = '$200'
# print(prices)

"""note the following
.appemd(item) to add am item to a list
.insert(2, item) to insert an item at a particular index
.remove(item) to remove an item from a list
.clear(list) to clear a list
.sort(list) to sort a list
"""

# # append items to existing list
# print('\n# append() method')
# fruits.append("mango")
# print(fruits)

# # # insert item at a particular index
# print('\n# insert item at a particular index')
# fruits.insert(2,'grapes')
# print(fruits)

# # remove an item from the list
# print('\n# remove an item from the list')
# fruits.remove('watermelon')
# print(fruits)

# fruits.clear()
# print(fruits)

# # delete the complete list
# print('\n # delete the complete list')
# del(fruits)
# print(fruits)

# sort the list
# print('\n# sort() the list')
# fruits.sort()
# print(fruits)