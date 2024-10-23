from typing import List

def unique_permutations(nums: List[int]) -> List[List[int]]:
    """
    Generate all unique permutations of a list that may contain duplicates.
    
    :param nums: List of integers (may contain duplicates)
    :return: List of unique permutations
    """
    # Sort the list to handle duplicates
    nums.sort()
    result = []
    visited = [False] * len(nums)

    def backtrack(permutation):
        # If the current permutation is the same length as nums, we found a valid permutation
        if len(permutation) == len(nums):
            result.append(permutation[:])  # Make a copy of the current permutation
            return
        
        for i in range(len(nums)):
            # Skip if the number is already used or if it's a duplicate of a previous unused number
            if visited[i] or (i > 0 and nums[i] == nums[i - 1] and not visited[i - 1]):
                continue
            
            # Mark the number as used
            visited[i] = True
            # Include nums[i] in the current permutation
            permutation.append(nums[i])
            # Continue building the permutation
            backtrack(permutation)
            # Undo the choice (backtrack)
            permutation.pop()
            visited[i] = False

    # Start the backtracking with an empty permutation
    backtrack([])

    return result

# Example usage
input_list = [1, 1, 2]
result = unique_permutations(input_list)
for perm in result:
    print(perm)
