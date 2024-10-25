# numbers = [2,4,5,8,6,3,10]
# for num in numbers:
#     if num%2 == 0:
#         print("This is an even number", num)
#     else:
#         print("This is an odd number", num)
# print("this is not part of the for loop")

# numbers = [2,4,5,8,6,3,10,30,100]
# for number in numbers:
#     if number == 2:
#         print(f"{number} is 2") #f"{} is string formatting
#     elif number > 10:
#         print("{number} is greater than 10") #note that the first positive condition will be executed
#     elif number > 5:
#         print(f"{number} is greater than 5")
#     else:
#         print(f"{number}")
        
"""nested if statement: makes your code more easy to read depending on the use case"""
        
# numbers = [2,4,5,8,6,3,10,30,100]
# for number in numbers:
#     if number == 2:
#         print(f"{number} is 2")
#         continue #stops and go back to the next item in the sequence
#     if number > 5: # start with the least restrictive
#         if number > 10:
#             print(f"{number} is greater than 10")
#         else:
#             print(f"{number} is greater than 5")
#     else:
#         print(f"{number} is not greater than 5")
        
# numbers = [2,4,5,8,6,3,10,30,100]
# for number in numbers:
#     if number == 2:
#         print(f"{number} is 2")
#         continue   #note
#     if number > 5: # start with the least restrictive
#         if number > 10:
#             print(f"{number} is greater than 10")
#         else:
#             print(f"{number} is greater than 5")
#     else:
#         print(f"{number} is not greater than 5")
        
# numbers = [2,4,5,8,6,3,10,30,100]
# for number in numbers:
#     if number == 2:
#         print(f"{number} is 2")
#         break   #note stops the that particular "for loop" 
#     if number > 5: # start with the least restrictive
#         if number > 10:
#             print(f"{number} is greater than 10")
#         else:
#             print(f"{number} is greater than 5")
#     else:
#         print(f"{number} is not greater than 5")