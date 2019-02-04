#Python decorator gives us the ability to add new behavior to the given objects dynamically.
def sample_decorator(func):
    """This is a demonstration of a simple decorator."""
    def decorator_hook(*args,**kwargs):
        print("Before the function call")
        result = func(*args,**kwargs)
        print("After the function call")
        return result
    return decorator_hook

@sample_decorator
def prod(x,y):
    return x*y

print(prod(2,4))

#Printing the doc string
print(sample_decorator.__doc__)
