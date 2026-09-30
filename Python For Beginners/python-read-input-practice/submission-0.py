def add_two_numbers() -> int:
    num_str = input()
    str_list = num_str.split(",")
    num_list = []
    for num in str_list:
        num_list.append(int(num))
    return sum(num_list)
    


# do not modify below this line
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
print(add_two_numbers())
