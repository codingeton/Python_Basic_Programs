'''
Program to identify if a given String is number or not “2e10”,”2100”,”2.2e10” etc
Note: Does not validate the decimal
'''
user_input = input("Enter the string::")
try:
    value = int(user_input)
    print(user_input, " is an integer.")
except ValueError:
    print(user_input, "is not an integer.")
