def list_depth(lst):
    if not isinstance(lst, list):
        return 0

    nested_depths = [list_depth(item) for item in lst]
    return max(nested_depths) + 1

nested_list = [1, [2, [3, 4], 5], 6, [7, 8, [9, 10, [11, 12]]]]
print("List nesting depth:", list_depth(nested_list))