





#Description: Develop a function called  sort_list that takes
# a list of numbers as input and returns a new list containing
# the same elements sorted in ascending order.

#function
def sort_list(list1, list2):
    sort_list1 = sorted (list1)
    sort_list2 = sorted (list2)
    return sort_list1, sort_list2

#list
list1 = [1,22,83,41,25,96,77,101,]
list2 = [5,3,2,6,7,1]

#sort them

results = sort_list (list1, list2)
print(results)

