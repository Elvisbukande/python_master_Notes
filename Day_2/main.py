#the input function is used to ask for the users input
# the input function always returms a string
#example write a program to calculate your pay

# rate = 10.0 
# hours = 10.0
# pay = rate * hours
# print("Pay:" , pay) # this is hard coding

# rate = input("Please enter your rate")
# print("Rate:  ",rate)
# hours = input("Please enter your hours")
# print(": ", hours)
# pay = rate * hours # the print function will always return a string
# print("Pay:" , pay) # so you need to convert to be able to multiple

#Type Conversion
"""
If you want to carry out any numerical operations with the input function
then you have to convert it because you cannot multiply two strings"""
#two ways to convert
# rate = input("Please enter your rate: ")
# rate = float(rate)
# print (type(rate))
# print("Rate: ", rate)  #preferable  with ease to understand

# #or 
# rate = float(input("Please enter your rate: "))
# print(type(rate))
# print("Rate:  ",rate) #not very clear to understand

# rate = input("Please enter your rate: ")
# rate = float(rate)
# print (type(rate))
# print("Rate: ", rate) 

# hours = input("Please enter your rate: ")
# hours = float(hours)
# print (type(hours))
# print("Rate: ", hours) 

# pay = hours * rate
# print ("Pay, Rate X Hours =: ", pay)

"""
Write a python code that takes the user's name , age and height as 
input and displays the information back to the user

"""
# name = input("Please provide your name:  ")
# print("My name is: ", name)

# age = input("Please enter your age: ")
# age = int(age)
# print("My age is: ", age)

# height = input("Please provide your height: ")
# height = float(height)
# print (" My height is: ", height, "feet")

# """Error Handling
# There are three main types of errors in Python
# -Synthax Errors
# -Runtime errors
# -Logical Errors"""
#  #try and except example
 
# try:
#     name = input("Please provide your name:  ")
#     print("My name is: ", name)

#     age = input("Please enter your age: ")
#     age = int(age)
#     print("My age is: ", age)

#     height = input("Please provide your height: ")
#     height = float(height)
#     print (" My height is: ", height, "feet")
# except ValueError: 
#     print("You enter an invalid value")
#     print ("Try again")

# rate = input("Please enter your rate:  ")
# try:
#     rate = float(rate)
#     print("my Rate is:", rate)
# except ValueError:
#     print("You entered a wrong value")
#     print("Try again")
    
    
    
# try:
#     name = input("Please provide your name:  ")
#     print("My name is: ", name)

#     age = input("Please enter your age: ")
#     age = int(age)
#     print("My age is: ", age)

#     height = input("Please provide your height: ")
#     height = float(height)
#     print (" My height is: ", height, "feet")
# except ValueError: 
#     print("You enter an invalid value")
#     print ("Try again")
# except KeyboardInterrupt:
#     print("Goodbye")
""" In case you anticipates an error but you do
not know the error you can use the try and except as follows
"""
# try:
#     rate = input("Please provide your rate: ")
#     rate = float(rate)
#     print (rate)
#     Print("Benard")
# except ValueError:
#     print("You entered an invalid value")
#     print("Try again")
# except:
#     print("something went wrong")
    
"""
If you anticipates an error and you want to know the error
then the code will be as follows at the level of the except and you will capture your error without a 
stack trace(the long path)
"""
# try:
#     rate = input("Please provide your rate: ")
#     rate = float(rate)
#     print (rate)
#     Print("Benard")
# except ValueError:
#     print("You entered an invalid value")
#     print("Try again")
# except Exception as e:
#     print("something went wrong")
#     print(e)
    
# """
# The use of finally
# Finally is used to conclude the code where all the exceptions have been handled and the try block runs.
# If all exceptions are not handled , the finally will not run"""    
# try:
#     rate = input("Please provide your rate: ")
#     rate = float(rate)
#     print (rate)
#     Print("Benard")
# except ValueError:
#     print("You entered an invalid value")
#     print("Try again")
# except Exception as e:
#     print("something went wrong")
#     print(e)
# finally:
#     print("Thanks and goodbye")