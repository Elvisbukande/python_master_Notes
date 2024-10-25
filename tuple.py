# A Tuple is a collection of Python objects separated by commas. In someways a tuple is similar to a list in terms of indexing, nested objects and repetition but a tuple is immutable unlike lists which are mutable.
"""
– Use tuples when your data cannot change.
"""

numbers = (1, 2, 3)
names = ['Ben', 'Jones', 'showmik'] #this is a list
fruits = ('apple', 'banana', 'orange')
my_tuple = (10, 20, 30, {"name": "Benard", "age": 22},
            ['car', 'bike', 'bus'], 10)

# print tuples
# print('\n # print tuples')
# print(numbers)
# print(names)
# print(fruits)
# print(my_tuple)

# print(names)
# names[1]= "John" # this will work for a list and not a tuple
# print(names)

# access tuple items
# print('\n# access tuple items')
# print(names[0])
# print(numbers[1])
# print(my_tuple[4])

# check if item exists in the tuple
# print('\n # check if item exists in the tuple')
# print(10 in numbers)

# if 'banana' in fruits:
#     print("yes")
# else:
#     print("no")

# check tuple length
# print('\n # check tuple length')
# print(len(names))
# print(len(my_tuple))


# # get number of times an items is present in the tuple
# print('\n # get number of times an items is present in the tuple')
# print(my_tuple.count(10))
# print(names.count("Jones"))

# # get the index of an item in the tuple
# print('\n # get the index of an item in the tuple')
# print(names.index("Ben"))
# print(fruits.index("orange"))