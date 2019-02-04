#Identifies the common elements in two lists and prints them out

def intersected_items(a,b):
    a_set = set(a)
    b_set = set(b)
    #Find if there are any common elements using '&' function
    if (a_set & b_set):
        print("The common elements are: ",a_set & b_set)
    else:
        print("There are no common elements in the lists")

list_a = [1,2,3,4,5,6,7,8,9,9,4,22]
list_b = [2,3,9,6]

intersected_items(list_a,list_b)
