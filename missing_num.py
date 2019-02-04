#Prints the missing number in the sequence.
'''
Get the sum of numbers total = (n+1)*(n+2)/2
Subtract all the numbers from sum and you will get the missing number.
'''
def missing_number(a_list):
    n = len(a_list)
    total = (n+1)*(n+2)/2
    sum_of_list = sum(a_list)
    return int(total - sum_of_list)

l = [1,2,3,5]
print(missing_number(l))
