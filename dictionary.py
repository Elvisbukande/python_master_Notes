# Dictionaries are used to store data values in key:value pairs.
"""
– When you need a logical association between a key:value pair.
The value could be an integer, a list, a float, a string
"""

# student = {
#     "name": "Benard",
#     "age": "25 years", 
#     "college":"abc-college"
#     }, 

# print (student)
# Nested dictionary example
nested_dict = {
    'person1': {
        'name': 'Alice',
        'age': 30,
        'job': 'Engineer'
    },
    'person2': {
        'name': 'Bob',
        'age': 25,
        'job': 'Designer'
    }
}

# Accessing values in a nested dictionary
print(nested_dict['person1']['name'])  # Output: Alice
print(nested_dict['person2']['job'])   # Output: Designer





# fruits = {"apple": 5, "banana": 3.50, "watermelon": 2.75}
# friends = {"class-1": ["david", "ricci"], "class-2": ["john", "matheus"]}

# print dictionary
# print('\n # print dictionary') # note that \n(newline character) means move to next line before printing
# print(student)
# print(fruits)
# print(friends)


# access dictionary items
# print('\n #access dictionary' )
# print(student["name"])
# print(fruits["apple"])
# print(friends["class-2"])

# check if key exists in a dictionary
# print('\n check if key exixts in a dictionary ')
# if "apple" in fruits:
#     print(fruits["apple"])
# else:
#     print("request not found")
    
# if 'class' in student:
#     print(student['college'])
# else:
#     print('requested key not found')

# check the data structure type of these values
# print('\n # check the data structure type of these values')
# print(type(student))
# print(type(fruits))
# print(type(friends))

# # check the methods and attributes available for the dictionary variable
# print('\n # check the methods and attributes available for the dictionary variable')
# print(dir(student))

# modify an existing key value in dictionary
# print('\n # modify an existing key value in dictionary')
# student['name'] = 'Ben Ngwa'
# print(student)
# friends["class-1"] = "Form-one"
# print(friends)

# # check dictionary length
# print('\n # check dictionary length')
# print(len(student))
# print(len(friends))
# print(len(fruits))

# delete a key from the dictionary
# print('\n # delete a key from the dictionary')
# if 'college' in student:
#     student.pop('college')
#     print(student)
# else:
#     print('key not found')
    
# if "apple" in fruits:
#     fruits.pop("apple")
#     print(fruits)
# else:
#     print("output not found")

# iterate over a dictionary values
# print('\n # iterate over a dictionary values')
# for val in student.values():
#     print(val)

# # iterate over a dictionary key,value pairs
# print('\n # iterate over a dictionary key,value pairs')
# for key,val in student.items():
#     print(key, val)


# # clear all key-value from dictionary
# print('\n # clear all key-value from dictionary')
# student.clear()
# print(student)

# # delete the complete dictionary
# print('\n # delete the complete dictionary')
# del student
# print(student)