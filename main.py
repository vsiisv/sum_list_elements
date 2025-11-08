list1 = [1, 2, 3, 4, 5]
list2 = [6, 7, 8, 9, 10]

# first
result = [a + b for a, b in zip(list1, list2)]
print(result)


# second
def new_list(list1, list2):
    new_list = []
    for i in range(len(list1)):
        new_list.append(list1[i] + list2[i])
    return new_list


print(new_list(list1, list2))
