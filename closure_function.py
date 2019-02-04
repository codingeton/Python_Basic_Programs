# Python closures are function objects returned by another function.
# We use them to eliminate code redundancy.
def multiply_number(num):
    def product(number):
        #product is the closure function here.
        return num * number
    return product

num_1 = multiply_number(10)
print(num_1(10)) #prints 100
