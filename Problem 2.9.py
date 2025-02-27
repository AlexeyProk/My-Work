


#Explain the Merge Sort algorithm and demonstrate its implementation in Python to sort a list of strings in ABC order

def merge_sort(array):
    # if there is only one element then the list is sorted
    if len(array) <= 1:
        return array
    # Divide the list into two halves
    mid = len(array) // 2
    left_half = array[:mid]
    right_half = array[mid:]

    #sort the half recursively
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)

    #Merge Everything
    return merge(left_sorted, right_sorted)

def merge(left, right):
    sorted_list = []
    while left and right:
        if left[0] < right[0]:
            sorted_list.append(left.pop(0))
        else:
            sorted_list.append(right.pop(0))

    sorted_list.extend(left)
    sorted_list.extend(right)

    return sorted_list

string = ["banana", "pear", "apple", "orange", "kiwi"]
sorted_strings = merge_sort(string)

print("Sorted Strings: ", sorted_strings)


