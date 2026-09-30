from typing import List

def read_integers() -> List[int]:
    num_str = input()
    str_list = num_str.split(",")
    num_list = []
    for num in str_list:
        num_list.append(int(num))
    return num_list


# do not modify the code below
print(read_integers())
print(read_integers())
print(read_integers())
