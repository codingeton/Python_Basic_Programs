# import os
# '''
# Prints the base path
# '''
# print(os.path.expanduser('~'))
while True:
    try:
        number = int(input("Enter the number::"))
        if number%2 == 0:
            raise ValueError("Number is even. Please enter an odd number.")
        else:
            print(number)
    except ValueError as ex:
        print(ex)
        break
