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


# order the activities from latest to earliest start time 
# loop over the activities 
def activityMaker(activities):
    activities_sorted = merge_sort(
        activities, lambda x, y: x[1] > y[1])  # sort in descending order on start time 

    activities_selected = []

    for new_activity in activities_sorted:
        activities_selected_length = len(activities_selected)

        if activities_selected_length == 0:
            # always add first activity
            activities_selected.append(new_activity)
            continue
        last_activity = activities_selected[activities_selected_length - 1]

        # new end time greater than last start time, invalid
        if new_activity[2] > last_activity[1]:
            continue

        # is in valid range, add
        activities_selected.append(new_activity)
    
    activity_idxs = []
    # create list of the activity indexes 
    for activity in activities_selected: 
        activity_idxs.append(activity[0])
    # sort to return in correct order 
    activity_idxs = merge_sort(activity_idxs, sort_func = lambda x, y: x < y)
    activity_count = len(activity_idxs)
    return activity_idxs, activity_count


# activity = (start Time, finish Time)
activities = [(1,1,4), (2,3,5), (3,0,6), (4,5,7), (5,3,9), (6,5,9), (7,6,10), (8,8,11), (9,8,12), (10, 2,14), (11, 12,16)]

print(activityMaker(activities))

# activities = [(6,8), (7,9), (1,2)]
# print(activityMaker(activities))

# [(12, 15), (8, 12), (5, 7), (3, 5)]
# return activities numbers
