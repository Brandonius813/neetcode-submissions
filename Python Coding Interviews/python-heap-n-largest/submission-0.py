import heapq
from typing import List


def get_max_element(arr: List[int]) -> int:
    output = heapq.nlargest(1, arr)
    return output[0]


def get_max_4_elements(arr: List[int]) -> List[int]:
    # Return elements in *decreasing* order
    output = heapq.nlargest(4, arr)
    return output


def get_max_2_elements(arr: List[int]) -> List[int]:
    # Return elements in *increasing* order
    output = []
    decreasing = heapq.nlargest(2, arr)
    output.append(decreasing[1])
    output.append(decreasing[0])

    return output



# do not modify below this line
print(get_max_element([1, 2, 3]))
print(get_max_element([3, 2, 1, 4, 6, 2]))
print(get_max_element([1, 9, 7, 3, 2, 1, 4, 6, 2]))

print(get_max_4_elements([4, 9, 7, 3, 2, 7, 4, 6, 2]))
print(get_max_4_elements([4, 9, 7, 2, 1, 3, 2, 3, 4, 6, 2, 3]))
print(get_max_4_elements([4, 7, 2, 3, 2, 4, 6, 2]))

print(get_max_2_elements([4, 5, 3, 7]))
print(get_max_2_elements([8, 8, 7, 9]))
print(get_max_2_elements([1, 2, 3, 9, 8, 7, 6]))

