def find_min(l):
    """
    Find the minimum value and its index in the input list.

    Parameters
    ----------
    l : list
        The input list in which the minimum value needs to be found.

    Returns
    -------
    min_value : any
        The minimum value found in the input list.
    min_idx : int
        The index of the first occurrence of the minimum value in the input list.

    """
    
    min_value, min_idx = l[0], 0
    
    for idx, value in enumerate(l):
        
        if value < min_value:
            min_value = value
            min_idx = idx
            
    return min_value, min_idx

def selection_sort(l):
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
    
    for idx in range(len(l)-1):
        
        min_idx = find_min(sorted_list[idx:])[1] + idx
        
        sorted_list[idx], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[idx]
        
    return sorted_list


l = [4,2,7,4,9,1,-5,8,0,2,-5,11,1,-13,-9,0]

sorted_list = selection_sort(l)

print(f"\nInitial list:\n{l}\n\nSorted list:\n{sorted_list}")

# Test case 1: Empty list
input_list = []
expected_output = []
assert selection_sort(input_list) == expected_output

# Test case 2: List with one element
input_list = [5]
expected_output = [5]
assert selection_sort(input_list) == expected_output

# Test case 3: List with duplicate elements
input_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
expected_output = [1, 1, 2, 3, 3, 4, 5, 5, 5, 6, 9]
assert selection_sort(input_list) == expected_output

# Test case 4: List already sorted in ascending order
input_list = [1, 2, 3, 4, 5]
expected_output = [1, 2, 3, 4, 5]
assert selection_sort(input_list) == expected_output

# Test case 5: List already sorted in descending order
input_list = [5, 4, 3, 2, 1]
expected_output = [1, 2, 3, 4, 5]
assert selection_sort(input_list) == expected_output

# Test case 6: List with negative numbers
input_list = [10, -5, 8, -2, 0, -3]
expected_output = [-5, -3, -2, 0, 8, 10]
assert selection_sort(input_list) == expected_output

# Test case 7: List with large numbers
input_list = [1000, 5000, 2000, 3000, 4000]
expected_output = [1000, 2000, 3000, 4000, 5000]
assert selection_sort(input_list) == expected_output

# Test case 8: List with repeated large numbers
input_list = [999, 999, 1000, 1000, 1001, 1001]
expected_output = [999, 999, 1000, 1000, 1001, 1001]
assert selection_sort(input_list) == expected_output

# Test case 9: List with negative and positive numbers
input_list = [10, -5, 8, -2, 0, -3, 15, 1, -10]
expected_output = [-10, -5, -3, -2, 0, 1, 8, 10, 15]
assert selection_sort(input_list) == expected_output

print("All test cases passed!")
