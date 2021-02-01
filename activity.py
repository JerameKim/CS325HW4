import os
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

def activityMaker(activities):
    activities_sorted = merge_sort(activities, lambda x, y: x[1] > y[1])  # sort in descending order on start time

    activities_selected = []

    # loop over the activities
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
    # create list of the activity indexes we selected
    for activity in activities_selected:
        activity_idxs.append(activity[0])

    # sort to return in correct order
    activity_idxs = merge_sort(activity_idxs, sort_func=lambda x, y: x < y)
    activity_count = len(activity_idxs)

    return activity_idxs, activity_count


def open_file(filename):
    # open file
    with open(filename, 'r') as reader:
        content = reader.read().splitlines()
    # number of times we should be running activityMaker
    number_of_sets = int(content.pop(0).strip())

    # gets re-written for new set, holds activities 
    activity_sets = []
    for _ in range(number_of_sets):
        activities_in_set = int(content.pop(0).strip())

        activities = []
        # create object for each set
        for _ in range(activities_in_set):
            activity_data = content.pop(0).strip() # '1 1 4'
            numbers = [int(i) for i in activity_data.split()] # [1, 1, 4]
            activities.append(numbers) # [[1,1,4], [2,3,5]]
        activity_sets.append(activities)
    return activity_sets # returns set of sets with each activity 


if __name__ == "__main__":
    read_file = "act.txt"
    activity_sets = open_file(read_file)

    for activity_set_idx, activity_set in enumerate(activity_sets): 
        results = activityMaker(activity_set)

        print(f"Set {activity_set_idx + 1}")
        print(f"Number of activities seleted = {results[1]}")

        activities_selected = " ".join([str(i) for i in results[0]])
        print(f"Activities: {activities_selected}")

