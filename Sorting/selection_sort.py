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
    
    for idx in range(len(l)):
        
        min_idx = find_min(sorted_list[idx:])[1] + idx
        
        sorted_list[idx], sorted_list[min_idx] = sorted_list[min_idx], sorted_list[idx]
        
    return sorted_list



l = [4,2,7,4,9,1,-5,8,0,2,-5,11,1,-13,-9,15]

sorted_list = selection_sort(l)

print(f"\nInitial list:\n{l}\n\nSorted list:\n{sorted_list}")


