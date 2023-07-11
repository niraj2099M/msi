# FD related to lists

def remove_duplicates(arr): #time complexity is O(n)
    """
    This function removes duplicate elements in an array
    """
    unique_arr = []
    # Create a dictionary to store unique elements as keys
    element_dict = {}

    for element in arr:
        # Check if the element is already in the dictionary
        if element not in element_dict: #**lookup/search time complexity for list is O(1)
            element_dict[element] = True
            unique_arr.append(element)
    return unique_arr

arr=[1,4,2,1,5,3]

sorted_arr = sorted(arr)
sorted_arr_des = sorted(arr, reverse=True)

"""
The sorted() built-in function in Python uses an algorithm called Timsort. Timsort is a hybrid sorting algorithm derived from 
merge sort and insertion sort. It was designed to perform well on many kinds of real-world data.

Timsort is a stable sorting algorithm, which means that it preserves the relative order of elements with equal values. 
It has a best-case time complexity of O(n), a worst-case time complexity of O(n log n), and an average-case time complexity of 
O(n log n), where n is the number of elements to be sorted.
"""


print(sorted_arr)
print(sorted_arr_des)
print(*remove_duplicates(arr))