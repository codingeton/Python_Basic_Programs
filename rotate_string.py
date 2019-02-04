#Program to rotate the given string
def rotate(str, n):
    return str[n:]+str[:n]

string_to_rotate = "PythonDjangoFlask"

print("Rotated string is::",rotate(string_to_rotate,1))
