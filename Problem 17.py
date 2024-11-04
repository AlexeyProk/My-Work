



def find_common_element(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements

lista = [1,2,3,4,5,6,7,8,]
listb = [5,3,2,6,7,1]

results = find_common_element(lista, listb)
print(results)
