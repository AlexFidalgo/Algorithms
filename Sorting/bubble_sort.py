def bubble_sort(l):
    """
    Sorts the input list ascendingly.

    Parameters
    ----------
    l : list
        Inputted list

    Returns
    -------
    l:list
        Sorted List

    """
    
    sorted_list = l.copy()
    
    n = len(l)
    
    for i in range(0, n-1):
        for j in range(n-1, i, -1):
        
            if sorted_list[j-1] > sorted_list[j]:
                sorted_list[j], sorted_list[j - 1] = sorted_list[j-1], sorted_list[j]

        
    return sorted_list


l = [4,2,7,4,9,1,-5,8,0,2,-5,11,1,-13,-9,0]

sorted_list = bubble_sort(l)

print(f"\nInitial list:\n{l}\n\nSorted list:\n{sorted_list}\n")

# Test case 1: Empty list
input_list = []
expected_output = []
assert bubble_sort(input_list) == expected_output

# Test case 2: List with one element
input_list = [5]
expected_output = [5]
assert bubble_sort(input_list) == expected_output

# Test case 3: List with duplicate elements
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert bubble_sort(input_list) == expected_output

# Test case 4: List already sorted in ascending order
input_list = [1, 2, 3, 4, 5]
expected_output = [1, 2, 3, 4, 5]
assert bubble_sort(input_list) == expected_output

# Test case 5: List already sorted in descending order
input_list = [5, 4, 3, 2, 1]
expected_output = [1, 2, 3, 4, 5]
assert bubble_sort(input_list) == expected_output

# Test case 6: List with negative numbers
input_list = [10, -5, 8, -2, 0, -3]
expected_output = [-5, -3, -2, 0, 8, 10]
assert bubble_sort(input_list) == expected_output

# Test case 7: List with large numbers
input_list = [1000, 5000, 2000, 3000, 4000]
expected_output = [1000, 2000, 3000, 4000, 5000]
assert bubble_sort(input_list) == expected_output

# Test case 8: List with repeated large numbers
input_list = [999, 999, 1000, 1000, 1001, 1001]
expected_output = [999, 999, 1000, 1000, 1001, 1001]
assert bubble_sort(input_list) == expected_output

# Test case 9: List with negative and positive numbers
input_list = [10, -5, 8, -2, 0, -3, 15, 1, -10]
expected_output = [-10, -5, -3, -2, 0, 1, 8, 10, 15]
assert bubble_sort(input_list) == expected_output


print("All test cases passed!")
