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
    
    any_swap = True
    
    while(any_swap):
    
        any_swap = False
    
        for idx in range(len(l)-1):
            
            
            if sorted_list[idx+1] < sorted_list[idx]:
                sorted_list[idx], sorted_list[idx + 1] = sorted_list[idx+1], sorted_list[idx]
                any_swap = True
        
    return sorted_list


l = [4,2,7,4,9,1,-5,8,0,2,-5,11,1,-13,-9,0]

sorted_list = bubble_sort(l)

print(f"\nInitial list:\n{l}\n\nSorted list:\n{sorted_list}")
