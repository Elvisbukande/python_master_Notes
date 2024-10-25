# The input function
# Note that what ever you ask for the input function, it returns a string

# name = "Terry"
# greetings = "Hi there, " + name
# print(greetings)

# If you want the user to give his name (an input), use the input function
# name = input("enter your name: Ben")
# greetings = "Hi there, " + name
# print(greetings)

# Note that what ever you ask for the input function, it returns a string. So you will ues contatination to achieve certain things
name = input("enter your name: Ben")
age = input("enter your age : ")
greetings = "Hi there, " + name
print(greetings)
print(name + " is " + age + " years old.")