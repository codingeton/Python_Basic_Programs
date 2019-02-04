#Python program to print the reverse of a String

stuff = input("Enter the string you want to reverse: ")
'''
l = list(stuff)
l.reverse()
print("Reversed of the given string is -> ",''.join(l))
'''
#Using sliced syntax
def reverse(string):
    string = string[::-1]
    return string

print("Reverse of the given string is:: ",reverse(stuff))
