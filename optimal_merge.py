# Assuming the lists are sorted

# Merge smallest lists first.



def merge_two_sorted_lists(list_a, list_b):
    """Merge two lists and return a sorted list"""
    cursor_a = 0
    cursor_b = 0
    a_length = len(list_a)
    b_length = len(list_b)
    merged_list = []
    while cursor_a < a_length or cursor_b < b_length:
        if cursor_a >= a_length:
            merged_list.append(list_b[cursor_b])
            cursor_b += 1
        elif cursor_b >= b_length:
            merged_list.append(list_a[cursor_a])
            cursor_a += 1
        elif list_a[cursor_a] < list_b[cursor_b]:
            merged_list.append(list_a[cursor_a])
            cursor_a += 1
        else:
            merged_list.append(list_b[cursor_b])
            cursor_b += 1
    return merged_list


# These lists must be sorted beforehand
list_a = [3, 4, 6, 8, 7, 9, 10]
list_b = [1, 2, 4, 5, 6, 8]
list_c = [1, 2, 3, 4, 12, 32]
list_d = [3, 8, 7, 6]
mergedlist = merge_two_sorted_lists(list_a, list_b)
print(mergedlist)

def multi_merge(*lists):
    """Merge lists optimally using merge_two_sorted_lists()"""
    index_length_dict = {}
    number_of_lists = len(lists)
    for index, lst in enumerate(lists):
        index_length_dict[index] = (len(lst), lst)
    sorted_indices = sorted(index_length_dict.keys(), key=lambda k: index_length_dict[k][0])
    merged_list = []
    for i in range(number_of_lists - 1):
        if i == 0:
            merged_list = merge_two_sorted_lists(index_length_dict[sorted_indices[i]][1], index_length_dict[sorted_indices[i + 1]][1])
        else:
            merged_list = merge_two_sorted_lists(merged_list, index_length_dict[sorted_indices[i + 1]][1])
    
    
    print(index_length_dict)
    print(sorted_indices)
    print(merged_list)

multi_merge(list_a, list_b, list_c, list_d)