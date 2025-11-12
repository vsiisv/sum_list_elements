# first
def new_list_sum(list_1, list_2):
    min_length = min(len(list_1), len(list_2))
    longer_function = max([list_1, list_2], key=len)
    result = [list_1[i] + list_2[i] for i in range(min_length)] + longer_function[
        min_length:
    ]
    return result


# second
def new_list(list_1, list_2):
    min_length = min(len(list_1), len(list_2))
    longer_function = max([list_1, list_2], key=len)
    return [list_1[i] + list_2[i] for i in range(min_length)] + longer_function[
        min_length:
    ]


list_1 = [20, 43, 28, 19, 100, 54, 4, 6, 1]
list_2 = [8, 9, 10, 1, 3, 11, 12, 13, 14]

print(new_list_sum(list_1, list_2))
print(new_list(list_1, list_2))
