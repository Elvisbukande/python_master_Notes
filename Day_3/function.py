# def greetings() :
#     print("Gretings friend")
# greetings()

""" Mote that the above function does not have a parameter. The code below now has a parameter(variable)
then at runtime you can pass a value to the variable"""

# def greetings(name) :
#     print(f"Gretings {name}!")
    
# greetings("Ben") #assign a value
# print("ELVIS")
# print("Awah")
"""Note that the above code you have to run three times to get the result. To solve that we can customize in order not to repeat"""

""" Return value"""
def user_input(message, error_message="invalid entry."): 
    while True:
        try:   
            value= input(message)
            value= float(value)
            break
        except ValueError:
            print(error_message)
            print("please try again")
    return value
            
hours = user_input("Enter hours worked:", "Invalid entry for hours")
rate = user_input("Enter hourly rate:")
over_time_pay = 0

if hours > 40:
    over_time_hours = hours - 40
    over_time_rate = 1.5*rate
    over_time_pay = over_time_hours*over_time_rate
    print(over_time_pay)
    
pay = (rate * hours) * over_time_pay
print("Pay: ", pay)
