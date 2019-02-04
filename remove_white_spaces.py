#Program that removes the whitespaces from a given string

given_string = "This is a        string "
another_string = "   Hello there    "
print("String before::",given_string)
nice_string = given_string.split()
nice_string = ' '.join(nice_string)
print("String after::",nice_string)

#Remove any leading or trailing spaces using strip() function
print("Corrected another string::",another_string.strip())
