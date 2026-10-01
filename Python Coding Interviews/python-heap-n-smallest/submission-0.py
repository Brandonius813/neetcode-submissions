import heapq
from typing import List


def get_min_element(arr: List[int]) -> int:
    
    output = heapq.nsmallest(1, arr)
    return output[0]



def get_min_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    output = heapq.nsmallest(4, arr)
    return output


def get_min_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    output = []
    smallest = heapq.nsmallest(2, arr)

    output.append(smallest[1])
    output.append(smallest[0])

    return output



# do not modify below this line
print(get_min_element([1, 2, 3]))
print(get_min_element([3, 2, 1, 4, 6, 2]))
print(get_min_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_min_4_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_4_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_4_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

print(get_min_2_elements([1, 9, 7, 3, 2, 1, 4, 6, 2]))
print(get_min_2_elements([1, 9, 7, 2, 1, 3, 2, 1, 4, 6, 2, 1]))
print(get_min_2_elements([1, 9, 7, 2, 3, 2, 4, 6, 2]))

