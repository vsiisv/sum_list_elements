list1 = [1, 2, 3, 4, 5, 10, 20]
list2 = [6, 7, 8, 9, 10, 11, 12, 13, 14]

# first
result = [a + b for a, b in zip(list1, list2) if a or b is not None]
print(result)


# second
def new_list(list1, list2):
    new_list = []
    length = len(list1) if len(list1) < len(list2) else len(list2)
    for i in range(length):
        new_list.append(list1[i] + list2[i])

    return new_list


print(new_list(list1, list2))
