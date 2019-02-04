#Prints the duplicate elements in a list.

def contains_duplicates(a_list):
    neat_set = set()
    for i in a_list:
        if i in neat_set:
            return True
        neat_set.add(i)
    return False

master_list = [1,2,3,4,1,2,4,5]
neat_list= [1,2,3]
print(contains_duplicates(master_list))
print(contains_duplicates(neat_list))
