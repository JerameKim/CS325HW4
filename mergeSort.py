def merge_sort(my_list, sort_func: lambda x, y: x < y):

    # 1. Exit Statement
    #   only gets called n number of times
    if len(my_list) <= 1:
        return my_list

    middle_idx = len(my_list) // 2

    # 2. Recurse
    # left = merge_sort(my_list[0:middle_idx])
    # will return a sorted list from "left side"
    left = merge_sort(my_list[:middle_idx], sort_func)

    # right = merge_sort(my_list[middle_idx:len(my_list)-1])
    # will return a sorted list from "right side"
    right = merge_sort(my_list[middle_idx:], sort_func)

    # 3. Resolve Recursion
    sorted_list = merge(left, right, sort_func)
    return sorted_list


def merge(left, right, sort_func) -> []:

    combined = []

    left_idx = 0
    right_idx = 0

    # Run while there's uncompared values in both lists
    while left_idx < len(left) and right_idx < len(right):

        # if left's value smaller than right's value
        if sort_func(left[left_idx], right[right_idx]):
            # add the left value in
            combined.append(left[left_idx])

            # increment to compare to next left element
            left_idx += 1

        else:
            combined.append(right[right_idx])
            right_idx += 1

    # If there's uncompared values in right list, add the uncompaed values into combined
    while right_idx < len(right):
        combined.append(right[right_idx])
        right_idx += 1

    # if there's uncompared values values in left list, add the uncompared values into combined
    while left_idx < len(left):
        combined.append(left[left_idx])
        left_idx += 1
    return combined

#'''

arr = [6, 5, 7, 5, 8, 43, 9, 4, 8, 9, 12]

result = merge_sort(arr, lambda left, right: left > right) # left > right descending
print(result)

result = merge_sort(arr, lambda left, right: left < right)  # left < right ascending
print(result)
#'''