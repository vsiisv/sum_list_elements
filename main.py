list1 = [1, 2, 3, 4, 5, 10, 20, 43, 28, 19, 100, 54, 4, 6, 1]
list2 = [8, 9, 10, 1, 3, 11, 12, 13, 14, 3, 5, 1]


# first
def new_list_sum(list1, list2):
    min_length = min(len(list1), len(list2))
    result = [list1[i] + list2[i] for i in range(min_length)]
    if len(list1) > len(list2):
        result.extend(list1[min_length:])  # result += list1[min_length:]
    elif len(list2) > len(list1):
        result.extend(list1[min_length:])  # result += list2[min_length:]
    return result


# second
def new_list(list1, list2):
    min_length = min(len(list1), len(list2))
    return [list1[i] + list2[i] for i in range(min_length)] + (
        list1[min_length:] or list2[min_length:]
    )


print(new_list_sum(list1, list2))
print(new_list(list1, list2))
