from typing import List

def reverse_by_n_elements(lst: List[int], n: int) -> List[int]:
   
    result = []
    result1=[]
    i = 0

    while i < len(lst):
        group = []
        # Collect a group of n elements (or fewer if at the end)
        for j in range(i, min(i + n, len(lst))):
            group.append(lst[j])
        
        # Reverse the collected group manually
        for j in range(len(group) - 1, -1, -1):
            result.append(group[j])
        
        i += n
    return result
