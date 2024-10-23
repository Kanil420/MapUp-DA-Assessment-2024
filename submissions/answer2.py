from typing import List, Dict

def group_by_length(lst: List[str]) -> Dict[int, List[str]]:

    length_dict = {}

    for word in lst:
        length = len(word)
        if length not in length_dict:
            length_dict[length] = []
        length_dict[length].append(word)
    
    sorted_length_dict = dict(sorted(length_dict.items()))
    
    return sorted_length_dict

print(group_by_length(["apple", "bat", "car", "elephant", "dog", "bear"]))

print(group_by_length(["one", "two", "three", "four"]))
