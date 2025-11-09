# first
def new_list_sum(list_1, list_2):
    min_length = min(len(list_1), len(list_2))
    result = [list_1[i] + list_2[i] for i in range(min_length)]
    if len(list_1) > len(list_2):
        result.extend(list_1[min_length:])  # result += list_1[min_length:]
    elif len(list_2) > len(list_1):
        result.extend(list_2[min_length:])  # result += list_2[min_length:]
    return result


# second
def new_list(list_1, list_2):
    min_length = min(len(list_1), len(list_2))
    return [list_1[i] + list_2[i] for i in range(min_length)] + (
        list_1[min_length:] or list_2[min_length:]
    )


list_1 = [1, 2, 3, 4, 5, 10, 20, 43, 28, 19, 100, 54, 4, 6, 1]
list_2 = [8, 9, 10, 1, 3, 11, 12, 13, 14, 3, 5, 1]

print(new_list_sum(list_1, list_2))
print(new_list(list_1, list_2))
