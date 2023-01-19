list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
list2 = [11, 12, 13, 14, 15, 16, 17]
joined_list = []
for element in list1:
    if element % 2:
        joined_list.append(element)
for element in list2:
    if not element % 2:
        joined_list.append(element)
print(joined_list)