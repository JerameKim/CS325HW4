def merge_sort(my_list, sort_func=lambda left, right: left < right):
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
    right = merge_sort(my_list[middle_idx:], sort_func )

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
        # if left[left_idx] < right[right_idx]:
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

'''
result = merge_sort(tup_array, lambda left, right: left[1] > right[1])  # ordering descending by the second number in the tuple 
result = merge_sort(tup_array, lambda left, right: left[0] < right[0]) # ordering ascending by the first number in the tuple

arr = [6, 5, 7, 5, 8, 43, 9, 4, 8, 9, 12]

result = merge_sort(arr, lambda left, right: left > right) # left > right descending
print(result)

result = merge_sort(arr, lambda left, right: left < right)  # left < right ascending
print(result)
#''' 


def hotelTravel(distance_day, hotels_distances):
    # start at 0 hotel 
    hotels_distances.append(0)
    # sort the hotels array 
    hotels_distances = merge_sort(hotels_distances)

    # starting location 
    current_hotel_idx = 0

    # where we've been 
    visited_hotels = []

    num_hotels = len(hotels_distances)
 
    # loop over all the hotels to check their distance in relation to current location 
    for check_hotel_idx, _ in enumerate(hotels_distances): 

        # check if we're at last hotel 
        if check_hotel_idx + 1 == num_hotels: 
            # if we're at last hotel, append that hotel as the most recently vistied
            visited_hotels.append(check_hotel_idx)
            break
        
        # check next hotel 
        next_hotel_distance = hotels_distances[check_hotel_idx + 1]

        # check if i can make it to the next hotel 
        if distance_day < next_hotel_distance - hotels_distances[current_hotel_idx]:
            # can't make it, change current hotel 
            current_hotel_idx = check_hotel_idx
            # include that hotel as visited hotel 
            visited_hotels.append(current_hotel_idx)


    return visited_hotels

hotelDistances = [12,3,4,2,12,2,3,5,7,8,4,3,6,8,9,5,9,6,4,6,8,13,15,17,19,20]

distPerDay = 3
print(hotelTravel(distPerDay, hotelDistances))
