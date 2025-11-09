list1 = [1, 2, 3, 4, 5, 10, 20, 43, 28, 19, 100, 54]
list2 = [6, 7, 8, 9, 10, 11, 12, 13, 14]


# first
def new_list_sum(list1, list2):
    difference = abs(len(list1) - len(list2))
    list_slice = list1[-difference:] if len(list1) > len(list2) else list2[-difference:]
    result = [a + b for a, b in zip(list1, list2) if a or b is not None]
    return result + list_slice


# second
def new_list(list1, list2):
    new_list = []
    difference = abs(len(list1) - len(list2))
    list_slice = list1[-difference:] if len(list1) > len(list2) else list2[-difference:]
    length = len(list1) if len(list1) < len(list2) else len(list2)
    for i in range(length):
        new_list.append(list1[i] + list2[i])

    return new_list + list_slice


print(new_list_sum(list1, list2))
print(new_list(list1, list2))
